from django.urls import path
from .views import *

app_name = 'friend'

urlpatterns = [
    path('friend_request/', send_friend_request, name='friend-request'),
    path('friend_requests/<user_id>/', friend_requests, name='friend-requests'),
]