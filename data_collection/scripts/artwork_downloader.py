
import requests
from lxml import html
import time
import urllib.request

class ArtworkDownloader:
    def __init__(self, base_url, artist_name):
        self.base_url = base_url
        self.artist_name = artist_name

    def save_artworks(self):
        painting_count = 0
        print("Trying to find grid of links to artwork pages...")
        listing_grid = self.get_listing_grid()
        for a in listing_grid.cssselect("a"):
            href = a.get("href")
            if href and "/artworks/" in href:
                print("Looking for artwork_url in", href)
                artwork_url = self.get_artwork_url(href)
                if artwork_url:
                    print("Trying to save file from", artwork_url)
                    self.save_file(artwork_url, painting_count)
                painting_count += 1


    def get_listing_grid(self):
        response = requests.get(self.base_url)
        grid_html = html.fromstring(response.text)
        return grid_html.cssselect(".listing-grid")[0]

    def get_artwork_url(self, href):
        painting_response = requests.get(href)
        painting_html = html.fromstring(painting_response.text)
        time.sleep(1)
        artwork_url = False
        try:
            artwork_url = painting_html.cssselect(".artwork")[0].cssselect("img")[0].get("src")
        except:
            print("artwork_url not found")
        time.sleep(1)
        return artwork_url

    def save_file(self, artwork_url, painting_count):
        save_to = "./images/{}_{}.jpg".format(self.artist_name, painting_count)
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
        urllib.request.install_opener(opener)
        try:
            urllib.request.urlretrieve(artwork_url, save_to)
        except:
            print("save file failed", artwork_url, save_to)
        time.sleep(1)
