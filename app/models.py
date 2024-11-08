from django.db import models

# Extend the default user model
class UserProfile(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    weight = models.FloatField(help_text="Weight in kg")
    height = models.FloatField(help_text="Height in cm")

    def __str__(self):
        return f"{self.username}'s Profile"

class WorkoutGoal(models.TextChoices):
    WEIGHT_LOSS = 'WL', 'Weight Loss'
    MUSCLE_GAIN = 'MG', 'Muscle Gain'
    TONING = 'TN', 'Toning'

class WorkoutSession(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    gym_frequency = models.PositiveIntegerField(help_text="Gym visits per week")
    workout_goal = models.CharField(max_length=2, choices=WorkoutGoal.choices)
    walking_distance_to_gym = models.FloatField(help_text="Distance to gym in km", null=True, blank=True)
    time_spent_at_gym = models.DurationField(help_text="Average time spent at the gym per session")

    def __str__(self):
        return f"Workout for {self.user.username} - {self.get_workout_goal_display()}"

