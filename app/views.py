from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserWorkoutProfile
from .serializers import UserWorkoutProfileSerializer


@api_view(["POST"])
def add_user_workout_profile(request):
    serializer = UserWorkoutProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def generate_exercises(frequency, goal):
    # Sample workout plan based on frequency and goal
    exercises_data = {
        "Weight Loss": [
            {"name": "Running", "reps": "30"},
            {"name": "Jump Rope", "reps": "3"},
            {"name": "Burpees", "reps": "3"},
        ],
        "Muscle Gain": [
            {"name": "Squats", "reps": "4"},
            {"name": "Deadlifts", "reps": "4"},
            {"name": "Bench Press", "reps": "4"},
        ],
        "Toning": [
            {"name": "Pilates", "reps": "45"},
            {"name": "Yoga", "reps": "45"},
            {"name": "Light Weights", "reps": "3"},
        ],
        "Endurance": [
            {"name": "Running", "reps": "5"},
            {"name": "Cycling", "reps": "10"},
            {"name": "Swimming", "reps": "30"},
        ],
    }

    # Default exercises if the goal is not matched
    exercises = exercises_data.get(goal, [
        {"name": "General Fitness", "reps": "30"}
    ])

    # Adjust workout based on frequency
    workout_plan = []
    for day in range(frequency):
        daily_workout = {
            "name": f"Day {day + 1}",
            "exercises": [],
        }

        # Add exercises to the workout for this day
        for exercise in exercises:
            daily_workout["exercises"].append(exercise)

        workout_plan.append(daily_workout)

    return workout_plan


@api_view(["GET"])
def generate_workout_plan(request, user_id):
    try:
        user_profile = UserWorkoutProfile.objects.get(id=user_id)
    except UserWorkoutProfile.DoesNotExist:
        return Response(
            {"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND
        )

    # Get workout frequency and goal from user profile
    frequency = user_profile.how_many_times_per_week
    goal = user_profile.get_reason_display()

    # Generate a tailored workout plan based on frequency and goal
    workout_plan = generate_exercises(frequency, goal)

    return Response(
        workout_plan,
        status=status.HTTP_200_OK,
    )
