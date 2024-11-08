from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.urls")),  # Include the URLs from gym_app
]
