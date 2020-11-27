from pickle import TRUE

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    objects = None
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Read(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=TRUE)
    create_date = models.DateTimeField()

    @property
    def __str__(self):
        return self.subject
