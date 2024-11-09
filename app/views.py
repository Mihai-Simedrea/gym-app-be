# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserWorkoutProfile
from .serializers import UserWorkoutProfileSerializer


@api_view(["POST"])
def add_user_workout_profile(request):
    serializer = UserWorkoutProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
