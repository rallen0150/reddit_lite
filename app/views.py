from django.shortcuts import render
from app.models import Subreddit, Post, Comment

from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.

def index_view(request):
    return render(request, "index.html")

class SubredditView(ListView):
    model = Subreddit

class SubredditCreateView(CreateView):
    model = Subreddit
    success_url = "/subreddit"
    fields = ('name', 'description')

class SubredditUpdateView(UpdateView):
    model = Subreddit
    success_url = "/subreddit"
    fields = ('name', 'description')

class SubredditDetailView(DetailView):
    model = Subreddit
