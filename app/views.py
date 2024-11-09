# views.py
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
    exercises = {
        "Weight Loss": ["Cardio", "HIIT", "Circuit Training"],
        "Muscle Gain": ["Weight Lifting", "Strength Training", "Compound Movements"],
        "Toning": ["Pilates", "Yoga", "Light Weights"],
    }

    # Adjust workout based on the frequency
    workout_plan = []
    for day in range(frequency):
        workout_plan.append(
            {
                "day": f"Day {day + 1}",
                "exercise": exercises.get(goal, ["General Fitness"])[
                    day % len(exercises[goal])
                ],
            }
        )
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
        {"user": user_profile.name, "goal": goal, "workout_plan": workout_plan},
        status=status.HTTP_200_OK,
    )
