from django.db import models

# Create your models here.

class Message(models.Model):
    s_no = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Message = models.TextField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return 'message from : ' + self.Name
    