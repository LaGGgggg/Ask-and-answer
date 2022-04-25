from django.db import models


class Questions(models.Model):

    title = models.CharField(max_length=31)
    content = models.TextField()
    likes_value = models.IntegerField()
    pub_date = models.DateTimeField()
