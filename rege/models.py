from django.db import models

# Create your models here.

class Customer(models.Model):
    userid = models.CharField(max_length=30, unique=True)
    passwd = models.CharField(max_length=64)
    email = models.CharField(max_length=30)
    reg_time = models.DateTimeField()

    def __unicode__(self):
        return self.userid
