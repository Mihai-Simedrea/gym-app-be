from django.db import models


class UserWorkoutProfile(models.Model):
    SEX_CHOICES = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    WORKOUT_GOAL_CHOICES = [
        ("WL", "Weight Loss"),
        ("MG", "Muscle Gain"),
        ("TN", "Toning"),
    ]

    # Fields corresponding to the form controls
    name = models.CharField(max_length=100, help_text="User's name")
    gender = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    weight = models.FloatField(help_text="Weight in kg")
    height = models.FloatField(help_text="Height in cm")
    how_many_times_per_week = models.PositiveIntegerField(
        help_text="Gym visits per week"
    )
    how_much_time_in_gym = models.DurationField(
        help_text="Average time spent at the gym per session"
    )
    reason = models.CharField(
        max_length=2, choices=WORKOUT_GOAL_CHOICES, help_text="Workout goal"
    )
    body_part = models.CharField(
        max_length=100,
        help_text="Focused body part (e.g., arms, legs, etc.)",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}'s Workout Profile"
