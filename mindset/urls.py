from django.urls import path

from . import views

app_name = 'mindset'

urlpatterns = [
    path("", views.mindset, name="mindset"),
]
