from django.shortcuts import render
from app.models import Subreddit, Post, Comment

# Create your views here.
def index_view(request):
    context = {
        "all_sub": Subreddit.objects.all(),
        "all_post": Post.objects.all()
    }
    return render(request, "index.html", context)
