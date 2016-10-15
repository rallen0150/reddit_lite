from django.shortcuts import render
from app.models import Subreddit, Post, Comment

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index_view(request):
    return render(request, "index.html")

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/subreddit"

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

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    success_url = '/subreddit'
    fields = ('title', 'post_description')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    success_url = '/subreddit'
    fields = ('title', 'post_description')


class CommentCreateView(CreateView):
    model = Comment
    success_url = '/subreddit'
    fields = ('comment', )

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.comment_user = self.request.user
        instance.comment_post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    success_url = '/subreddit'
    fields = ('comment', )
