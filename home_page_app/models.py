from django.db import models


class User(models.Model):

    # defne id to change BigInteger to Integer, because I don't need too big numbers.
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


#class Moderator(models.Model):
#    pass


#class Admin(models.Model):
#    pass
