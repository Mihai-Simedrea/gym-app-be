from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileWorkoutDTO


class UserProfileWorkoutView(APIView):
    def post(self, request):
        serializer = UserProfileWorkoutDTO(data=request.data)

        if serializer.is_valid():
            user_profile = serializer.save()
            return Response(
                {
                    "message": "User profile and workout session created successfully.",
                    "user_id": user_profile.id,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
