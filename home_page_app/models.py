from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField(unique=True)
    likes = models.ManyToManyField(User, related_name='questions_likes')
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions_user')

    def total_likes(self):
        return self.likes.count()


class Comments(models.Model):

    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='comments_likes')
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user')

    def total_likes(self):
        return self.likes.count()
