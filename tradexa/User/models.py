from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor


class User(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

    def __repr__(self):
        return self.first_name
    
    def __str__(self):
        return self.first_name

class Post(models.Model):
    text = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __repr__(self):
        return self.text
    
    def __str__(self):
        return self.text