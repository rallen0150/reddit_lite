from django.shortcuts import render
from app.models import Subreddit, Post, Comment

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
# Create your views here.

def index_view(request):
    return render(request, "index.html")

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_view")

class SubredditView(ListView):
    model = Subreddit

class SubredditCreateView(CreateView):
    model = Subreddit
    success_url = reverse_lazy('subreddit_view')
    fields = ('name', 'description')

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('subreddit_detail_view', args=[int(self.kwargs['pk'])])


class SubredditUpdateView(UpdateView):
    model = Subreddit
    # success_url = "/subreddit"
    fields = ('name', 'description')

    def get_success_url(self, **kwargs):
        return reverse_lazy('subreddit_detail_view', args=[int(self.kwargs['pk'])])


class SubredditDetailView(DetailView):
    model = Subreddit

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    # success_url = '/subreddit'
    # success_url = reverse_lazy("subreddit_view")
    fields = ['title', 'post_description', 'url_page']

    def get_success_url(self, **kwargs):
        return reverse_lazy('subreddit_detail_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.subreddit = Subreddit.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    # success_url = '/subreddit'
    fields = ('title', 'post_description')

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_update_view', args=[int(self.kwargs['pk'])])


class CommentCreateView(CreateView):
    model = Comment
    # success_url = '/subreddit'
    fields = ('comment', )

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.comment_user = self.request.user
        instance.comment_post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    # success_url = '/subreddit'
    fields = ('comment', )

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail_view', args=[int(self.kwargs['pk'])])
