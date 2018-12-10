from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^$', views.Feed.as_view(), name='feed'),
    url(r'^(?P<image_id>\d+)/$', views.ImageDetail.as_view(), name='image_detail'),
    url(r'^(?P<image_id>\d+)/like/$', views.LikeImage.as_view(), name='like_image'),
    url(r'^(?P<image_id>\d+)/unlike/$', views.UnLikeImage.as_view(), name='unlike_image'),
    url(r'^(?P<image_id>\d+)/comments/$', views.CommentOnImange.as_view(), name='comment_image'),
    url(r'^comments/(?P<comment_id>\d+)/$', views.CommentDelete.as_view(),name='comment'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^(?P<image_id>\d+)/comments/(?P<comment_id>\d+)/$', views.ModerateComments.as_view(), name='moderate_comment'),
]
