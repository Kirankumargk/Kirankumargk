from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=20)
	dob = models.CharField(max_length=20)
	 
class Employee(Person):
	eno = models.IntegerField()
	esalary = models.IntegerField()

class Manager(Employee):
	no_of_project = models.IntegerField()