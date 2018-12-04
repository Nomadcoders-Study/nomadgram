from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^explore/$', view=views.ExploreUsers.as_view(), name='explore_user'),
]
