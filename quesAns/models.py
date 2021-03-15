from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.


class Question(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_stamp']

    def __str__(self):
        return self.title + " -by- " + self.author


class answer(models.Model):
    question = models.ForeignKey(Question, default=None, on_delete=CASCADE)

    answer = models.TextField(default=None)
    author = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question)
