from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    url(r'^search/$', views.SearchView.as_view(), name="google-search-view"),
]