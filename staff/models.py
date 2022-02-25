from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Staff(models.Model):
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Direction(models.Model):
    direction_name = models.CharField(max_length=100)


class Office(models.Model):
    office_name = models.CharField(max_length=100)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)


class Department(models.Model):
    department_name = models.CharField(max_length=100)


class DepartmentOffice(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)


class Post(models.Model):
    post_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class UserPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)