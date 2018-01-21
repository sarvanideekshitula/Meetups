from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from meetup import views
from Meetups import settings
from django.contrib.auth import views as auth_views
from meetup.views import index, upcoming

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'meetup/login.html'}, name='login'),
    url(r'^index/$', views.index, name="index"),
    url(r'^upcoming/$', views.upcoming, name="upcoming"),
]
