from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField()
	date = models.DateField()
	content = models.TextField()
