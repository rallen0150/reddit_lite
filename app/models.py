from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
class Subreddit(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def current_count(self):
        return Post.objects.filter(subreddit=self).count()

    def today_count(self):
        day = datetime.now() - timedelta(days=1)
        return Post.objects.filter(subreddit=self).filter(post_created__gte=day).count()

    def daily_avg(self):
        day = datetime.now() - timedelta(days=7)
        return round((Post.objects.filter(subreddit=self).filter(post_created__gte=day).count())/7, 3)

    def get_recent(self):
        return Post.objects.filter(subreddit=self).order_by('-post_created')[:20]

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
        last_day = datetime.now() - timedelta(days=1)
        if Post.objects.filter(post_created__gte=last_day):
            return True
        else:
            return False

    def is_hot(self):
        past_hour = datetime.now() - timedelta(hours=3)
        if Comment.objects.filter(comment_post=self).filter(comment_edit__gt=past_hour).count() > 3:
            return True
        else:
            return False

    def get_comment(self):
        return Comment.objects.filter(comment_post=self)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_edit = models.DateTimeField(auto_now=True)
    comment_user = models.ForeignKey(User)
    comment_post = models.ForeignKey(Post)

    def __str__(self):
        return self.comment
