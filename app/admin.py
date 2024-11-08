from django.contrib import admin
from .models import UserProfile, WorkoutSession

admin.site.register(UserProfile)
admin.site.register(WorkoutSession)
