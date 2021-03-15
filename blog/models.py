from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=200)
    timeStamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timeStamp']

    def __str__(self):
        return self.title + " by " + self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.comment[0:13] + "..." + "by " + self.user.username
