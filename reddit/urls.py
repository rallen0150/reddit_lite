
from django.conf.urls import url, include
from django.contrib import admin

from app.views import index_view, SubredditView, SubredditDetailView, SubredditCreateView, SubredditUpdateView, \
                      PostDetailView, PostCreateView, CommentCreateView, UserCreateView, PostUpdateView, CommentUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index_view"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^subreddit$', SubredditView.as_view(), name="subreddit_view"),
    url(r'^subreddit/create/$', SubredditCreateView.as_view(), name="subreddit_create_view"),
    url(r'^subreddit/(?P<pk>\d+)/update/$', SubredditUpdateView.as_view(), name="subreddit_update_view"),
    url(r'^subreddit/(?P<pk>\d+)/$', SubredditDetailView.as_view(), name="subreddit_detail_view"),
    url(r'^subreddit/(?P<pk>\d+)/create/$', PostCreateView.as_view(), name="post_create_view"),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name="post_update_view"),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_detail_view"),
    url(r'^post/(?P<pk>\d+)/create/$', CommentCreateView.as_view(), name="comment_create_view"),
    url(r'^(?P<pk>\d+)/update/$', CommentUpdateView.as_view(), name="comment_update_view"),
]
