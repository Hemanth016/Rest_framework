from django.db import models# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=230)
    lastname=models.CharField(max_length=230)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.firstname
