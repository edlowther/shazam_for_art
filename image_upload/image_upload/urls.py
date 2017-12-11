
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from uploader import views as uploader_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/$', uploader_views.home, name='imageupload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# from django.urls import path
# from django.contrib import admin
# from . import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('about/', views.about),
#     path('', views.homepage),
# ]
