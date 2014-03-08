from django.db import models
from rege.models import Customer
# Create your models here.


class Book(models.Model):
    isbn = models.CharField(max_length=15, unique=True, null=False)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    translator = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=20, null=False)
    publisher = models.CharField(max_length=50, null=False)
    publish_time = models.CharField(max_length=50, null=False)
    page_num = models.CharField(max_length=10, null=True)
    zhuangzhen = models.CharField(max_length=20, null=True)
    introduct = models.TextField(null=True)
    pic_name_big = models.CharField(max_length=100)
    pic_name_small = models.CharField(max_length=100)
    score = models.CharField(max_length=5, null=False)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(Customer)
    title = models.CharField(max_length=20)
    content = models.TextField()
    com_time = models.TimeField()

    def __unicode__(self):
        return self.book.title

