# gym_app/urls.py

from django.urls import path
from .views import UserProfileWorkoutView

urlpatterns = [
    path("add-profile-workout/", UserProfileWorkoutView.as_view(), name="add-profile-workout"),
]
