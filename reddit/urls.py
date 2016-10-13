"""reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app.views import index_view, SubredditView, SubredditDetailView, SubredditCreateView, SubredditUpdateView, \
                      PostDetailView, PostCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index_view"),
    url(r'^subreddit$', SubredditView.as_view(), name="subreddit_view"),
    url(r'^subreddit/create/$', SubredditCreateView.as_view(), name="subreddit_create_view"),
    url(r'^subreddit/(?P<pk>\d+)/update/$', SubredditUpdateView.as_view(), name="subreddit_update_view"),
    url(r'^subreddit/(?P<pk>\d+)/$', SubredditDetailView.as_view(), name="subreddit_detail_view"),
    url(r'^subreddit/(?P<pk>\d+)/create/$', PostCreateView.as_view(), name="post_create_view"),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_detail_view"),

]
