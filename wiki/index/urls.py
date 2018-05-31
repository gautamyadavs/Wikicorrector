from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', views.search, name='search'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    ]
