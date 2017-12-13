from django.http import HttpResponse
from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from sklearn.externals import joblib
from skimage import io
from skimage.transform import resize

def images(request):
    return render(request, 'image_uploader/images.html')

def new(request):
    default_storage.delete('tmp/image_to_test.jpg')
    painting = request.FILES['painting']
    image_relative_filepath = default_storage.save('tmp/image_to_test.jpg', ContentFile(painting.read()))
    image_absolute_filepath = os.path.join(settings.MEDIA_ROOT, image_relative_filepath)
    painting_data = load_image(image_absolute_filepath)
    grid_colour_means = get_grid_colour_means(painting_data)
    predicted_artist_name = make_prediction(grid_colour_means)
    predicted_movement = get_movement(grid_colour_means)
    return render(request, 'image_uploader/success.html', {'name': predicted_artist_name, 'movement': predicted_movement})

def load_image(image_absolute_filepath):
    return io.imread(image_absolute_filepath)

def get_grid_colour_means(painting_data):
    GRID_WIDTH = 20
    resized_painting = resize(painting_data, (200, 200))
    result = []
    for i in range(10):
        for j in range(10):
            grid = resized_painting[
                i*GRID_WIDTH:i*GRID_WIDTH+GRID_WIDTH,
                j*GRID_WIDTH:j*GRID_WIDTH+GRID_WIDTH,
                :
            ]
            result.append(grid[:, :, 0].mean())
            result.append(grid[:, :, 1].mean())
            result.append(grid[:, :, 2].mean())
    return result

def make_prediction(grid_colour_means):
    ARTISTS = ["Cezanne", "Gauguin", "Kandinsky" ,"Rembrandt", "Rothko"]
    clf = joblib.load(os.path.join(settings.MEDIA_ROOT, 'neural_network_grid_colour_means_v7.pkl'))
    result = clf.predict([grid_colour_means])
    return ARTISTS[result[0]]

def get_movement(grid_colour_means):
    MOVEMENTS = ['Expressionistic cubism',
                 'Romantic colour fields',
                 'Impressionistic cloisonnism',
                 'Expressionistic colour fields',
                 'Cloisonnism-cubism',
                 'Baroque colour fields',
                 'Cloisonnistic colour fields',
                 'Expressionistic-cloisonnistic colour fields',
                 'Orangey-red colour fields',
                 'Paler colour fields'
                 ]

    clf = joblib.load(os.path.join(settings.MEDIA_ROOT, 'unsupervised.pkl'))
    result = clf.predict([grid_colour_means])
    return MOVEMENTS[result[0]]
