from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 30)
	rnum = models.CharField(max_length= 25)
	email = models.EmailField()
	mobile = models.CharField(max_length = 10)
	age = models.IntegerField(null=True)
	def __str__(self):
		return self.name