from django.urls import path

from .views import *
app_name = 'account'

urlpatterns = [
	path('<user_id>/', account_view, name="view"),
]