from django.urls import path, include
from .views import (
    register, 
    dashboard, 
    profile,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    # path('create/', create_booking, name='create_booking')
    # path('', include('users.urls')),
]
