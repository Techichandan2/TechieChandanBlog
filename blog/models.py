from django.db import models

from django.contrib.auth.models import User

from django.utils.timezone import now

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# class Category(models.Model):
#     title = models.CharField(max_length=30)
#     def __str__(self):
#         return self.title
    
class Post(models.Model):
    thumbnail = models.ImageField(null=True, blank=True, upload_to='media')
    sno= models.AutoField(primary_key=True)
    author = models.CharField(max_length = 100)
    category = models.CharField(max_length=100)
    title= models.CharField(max_length=250)
    slug = models.CharField(max_length=150)
    content = RichTextUploadingField()
    time_stamp= models.DateTimeField()
    
    def __str__(self):
        return self.title +' by ' + self.author
    
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')
    time_stamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:15] + "..." + "by " + self.user.username