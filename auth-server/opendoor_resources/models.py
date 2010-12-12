from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    uid = models.CharField(max_length=255)
    public_key = models.CharField(max_length=255)
    resources = models.ManyToManyField(Resource, through='user_resource')

class user_resource(models.Model):
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource)
    level = models.IntegerField()
