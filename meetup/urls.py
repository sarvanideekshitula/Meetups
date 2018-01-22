from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from meetup import views
from Meetups import settings
from meetup.views import index, upcoming, Info

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'meetup/login.html'}, name='login'),
    url(r'^index/$', index.as_view()),
    url(r'^(?P<pk>\d+)/$', Info.as_view(), name="Info"),
    url(r'^create/$', views.upcoming, name="create"),
    url(r'^editevent/(?P<pk>\d+)/$', views.editevent, name="edit"),
]
