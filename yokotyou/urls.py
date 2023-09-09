from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("match/", include("match.urls")),
    path("admin/", admin.site.urls),
]