from django.db import models
from django.contrib.auth.models import User

from simple_history.models import HistoricalRecords


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = models.PositiveBigIntegerField()
    history = HistoricalRecords()


#class Moderator(models.Model):
#    pass


#class Admin(models.Model):
#    pass
