from django.urls import path

from .views import loginView

urlpatterns = [
    path('login', loginView, name='loginView')
]