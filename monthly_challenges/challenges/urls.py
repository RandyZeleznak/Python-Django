from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  # generates "/challenges/" path
    path("<int:month>", views.monthly_challenge_number),
    path("<str:month>", views.monthly_challenge, name="monthly-challenges")
]
