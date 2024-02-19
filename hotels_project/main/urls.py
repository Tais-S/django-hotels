from django.urls import path
from .views import browse_hotels, redirect_to_admin, register_view, login_view

urlpatterns = [
    path('api/hotels/', browse_hotels, name='browse_hotels'),
    path('', redirect_to_admin, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login')
]