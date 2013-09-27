from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Employee(models.Model):
	emp_name = models.CharField(max_length=200)
	emp_age  = models.IntegerField()
	created_by = models.OneToOneField(User)
	created_on = models.DateTimeField(auto_now=True, auto_now_add=True)
	slug = models.SlugField(blank=True)
	title = models.CharField(max_length=200, blank=True)
	blog_title = models.CharField(max_length=200, blank=True)
	col1 = models.CharField(max_length=200, blank=True)


admin.site.register(Employee)