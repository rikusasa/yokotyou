from django.urls import path

from . import views
from django.views.generic import TemplateView

from .views import IndexView,MatchingView

urlpatterns = [
    path('', IndexView.as_view()),
    path('matching/', MatchingView.as_view()),
]