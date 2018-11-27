from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^all/$', views.ListAllImages.as_view(), name='all_images')
]