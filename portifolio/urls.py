from django.urls import path
from .views import dark_views

urlpatterns = [
    path('', dark_views, name='home'),
    path('dark/', dark_views, name='dark'),
]

