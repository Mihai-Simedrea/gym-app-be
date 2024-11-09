# urls.py in your app
from django.urls import path
from .views import add_user_workout_profile, generate_workout_plan

urlpatterns = [
    path(
        "api/add-workout-profile/", add_user_workout_profile, name="add-workout-profile"
    ),
    path(
        "api/generate-workout/<int:user_id>/",
        generate_workout_plan,
        name="generate-workout-plan",
    ),
]
