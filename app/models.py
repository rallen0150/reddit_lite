from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Subreddit(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def current_count(self):
        return Post.objects.filter(subreddit=self).count()

    def today_count(self):
        x = datetime.datetime.now() - datetime.timedelta(days=1)
        return Post.objects.filter(subreddit=self).filter(post_created__gte=x).count()

    def daily_avg(self):
        x = datetime.datetime.now() - datetime.timedelta(days=7)
        return round((Post.objects.filter(subreddit=self).filter(post_created__gte=x).count())/7, 3)

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_description = models.CharField(max_length=255)
    url_page = models.URLField(null=True, blank=True)
    post_created = models.DateTimeField(auto_now_add=True)
    post_edit = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def is_recent(self):
        pass

    def is_hot(self):
        pass

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_edit = models.DateTimeField(auto_now=True)
    comment_user = models.ForeignKey(User)
    comment_post = models.ForeignKey(Post)
