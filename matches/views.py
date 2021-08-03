from django.shortcuts import render
from django.views.generic import ListView
from .models import Match


class MatchListView(ListView):
    model = Match
    template_name = "match_list.html"

    context_object_name = 'list_of_matches'