from django.db import models

# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=30)
    detail = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    provider = models.ForeignKey('auth.User', related_name='message',
                                 on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
