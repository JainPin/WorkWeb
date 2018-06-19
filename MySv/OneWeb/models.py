from django.db import models
# Create your models here.
class OneWeb(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True) 
    def __str__(self):
        return self.title
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.title