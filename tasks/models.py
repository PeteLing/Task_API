from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    finished_time = models.DateTimeField(blank=True, null=True)
    excerpt = models.CharField(max_length=200, blank=True)
    tags = models.ForeignKey(Tag, blank=True)
    provider = models.ForeignKey('auth.User', related_name='tasks',
                                 on_delete=models.CASCADE)
    acceptor = models.ForeignKey('auth.User', related_name='accepted_tasks',
                                 blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('created_time', )
