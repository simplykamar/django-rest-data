from django.db import models

# Create your models here.


class Employee(models.Model):
	name=models.CharField(max_length=30)
	sal=models.IntegerField()
	city=models.CharField(max_length=30)
	def __str__(self):
		return self.name