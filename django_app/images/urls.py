from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^$', views.Feed.as_view(), name='feed'),
    url(r'^(?P<image_id>\d+)/like/$', views.LikeImage.as_view(), name='like_image'),
    url(r'^(?P<image_id>\d+)/comment/$', views.CommentOnImange.as_view(), name='comment_image'),
]
