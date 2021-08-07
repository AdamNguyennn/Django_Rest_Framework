from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	description = models.TextField()
	data_enrolled = models.DateTimeField(auto_now=True)

def __str__(self):
	return self.name