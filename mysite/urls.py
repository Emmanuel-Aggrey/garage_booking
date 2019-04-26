from django.urls import path, include
from .views import home, about, ServiceCreateView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('dashboard/new/', ServiceCreateView.as_view(), name='create_booking'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('user/', profile, name='profile')
]
