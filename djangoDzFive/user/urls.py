
from django.urls import path
from user.views import info_client
app_name = 'user'

urlpatterns = [
    path('', info_client, name='user'),
]
