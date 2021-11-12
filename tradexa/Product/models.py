from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    weight = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.CharField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name