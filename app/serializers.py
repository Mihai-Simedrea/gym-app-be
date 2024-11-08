from rest_framework import serializers
from .models import UserProfile, WorkoutSession, WorkoutGoal


class UserProfileWorkoutDTO(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.ChoiceField(choices=UserProfile.SEX_CHOICES)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    height = serializers.FloatField()
    howManyTimesPerWeek = serializers.IntegerField()
    howMuchTimeInGym = serializers.DurationField(
        help_text="Expected format: 'HH:MM:SS'"
    )
    reason = serializers.ChoiceField(choices=WorkoutGoal.choices)
    bodyPart = serializers.CharField(
        help_text="Optional specific body part focus", required=False, allow_blank=True
    )

    def create(self, validated_data):
        # Create UserProfile
        user_profile = UserProfile.objects.create(
            username=validated_data["name"],
            sex=validated_data["gender"],
            age=validated_data["age"],
            weight=validated_data["weight"],
            height=validated_data["height"],
        )

        # Create WorkoutSession
        WorkoutSession.objects.create(
            user=user_profile,
            gym_frequency=validated_data["howManyTimesPerWeek"],
            workout_goal=validated_data["reason"],
            time_spent_at_gym=validated_data["howMuchTimeInGym"],
        )

        return user_profile  # Returning user_profile as the main object created
