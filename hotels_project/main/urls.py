from django.contrib import admin
from django.urls import path
from .views import browse_hotels

urlpatterns = [
    path('api/hotels/', browse_hotels, name='browse_hotels'),
    path('', admin.site.urls),
]