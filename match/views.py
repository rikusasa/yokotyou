from django.views.generic import TemplateView
from django.views import generic
import logging

from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"

class MatchingView(TemplateView):
    template_name = "matching.html"

class WorldmapView(TemplateView):
    template_name = "worldmap.html"

class MemoryView(TemplateView):
    template_name = "memory.html"

class ZasekiView(TemplateView):
    template_name = "zaseki.html"