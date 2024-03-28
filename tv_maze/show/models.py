from django.db import models

class Show(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tvshow_id = models.IntegerField()
    name = models.CharField(max_length=200)
    channel = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    summary = models.TextField()
    genres = models.CharField(max_length=200)
    show_object = models.JSONField()