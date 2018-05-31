from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.auth.models import User


class SomeObject(models.Model):
    args = PickledObjectField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
