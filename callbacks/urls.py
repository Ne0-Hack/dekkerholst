from django.urls import path
from .views import create_callback

urlpatterns = [
    path('', create_callback, name='callback_api')
]
