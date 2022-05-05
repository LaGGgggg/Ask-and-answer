from django.db import models


class Questions(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField(unique=True)
    likes_value = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150)


class Comments(models.Model):

    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    content = models.TextField()
    likes_value = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=150)
