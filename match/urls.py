from django.urls import path

from . import views
from django.views.generic import TemplateView

from .views import IndexView,MatchingView,WorldmapView,MemoryView,ZasekiView

app_name = "match"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('matching/', MatchingView.as_view(), name='matching'),
    path('worldmap/', WorldmapView.as_view(), name='worldmap'),
    path('memory/', MemoryView.as_view(), name='memory'),
    path('zaseki/', ZasekiView.as_view(), name='zaseki'),
]