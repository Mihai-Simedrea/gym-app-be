# urls.py in your app
from django.urls import path
from .views import add_user_workout_profile

urlpatterns = [
    path('api/add-workout-profile/', add_user_workout_profile, name='add-workout-profile'),
]
