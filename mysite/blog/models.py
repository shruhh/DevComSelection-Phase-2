from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 140) #columns --- metadata
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

