from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^explore/$', view=views.ExploreUsers.as_view(), name='explore_user'),
    url(r'^(?P<user_id>\d+)/follow/$', view=views.FollowUser.as_view(), name='follow_user'),
]
