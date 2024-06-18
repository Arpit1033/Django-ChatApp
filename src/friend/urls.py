from django.urls import path

from .views import *

app_name = 'friend'

urlpatterns = [
	path('friend_remove/', remove_friend, name='remove-friend'),
    path('friend_request/', send_friend_request, name='friend-request'),
    path('friend_requests/<user_id>/', friend_requests, name='friend-requests'),
    path('friend_request_accept/<friend_request_id>/', accept_friend_request, name='friend-request-accept'),
]