from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^explore/$', view=views.ExploreUsers.as_view(), name='explore_user'),
    url(r'^(?P<user_id>\d+)/follow/$', view=views.FollowUser.as_view(), name='follow_user'),
    url(r'^(?P<user_id>\d+)/unfollow/$', view=views.UnFollowUser.as_view(), name='unfollow_user'),
    url(r'^(?P<username>\w+)/$', view=views.UserProfile.as_view(), name='user_profile'),
]
