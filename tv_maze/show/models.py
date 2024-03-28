from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, verbose_name="show_comment")
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
