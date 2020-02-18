from django.urls import path, include
from .views import u_register

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('u_register/', u_register, name='u_register')
]

