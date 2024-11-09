# serializers.py
from rest_framework import serializers
from .models import UserWorkoutProfile


class UserWorkoutProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutProfile
        fields = [
            "name",
            "gender",
            "age",
            "weight",
            "height",
            "how_many_times_per_week",
            "how_much_time_in_gym",
            "reason",
            "body_part",
        ]
