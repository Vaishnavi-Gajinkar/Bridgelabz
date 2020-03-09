from django.contrib import admin
from django.urls import path, re_path

from .views import index, room

app_name = 'chat'
urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    # re_path('<str:room_name>/', room, name='room'),
]
