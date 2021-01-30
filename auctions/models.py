from django.contrib.auth.models import AbstractUser
from django.db import models

# This model behaves identically to the default user model
class User(AbstractUser):
    pass

# All of listing product
class AuctionListing(models.Model):
    title = models.CharField(max_length=16, null=True)
    #category
    cat = [
        ('1', 'Fashions'),
        ('2', 'Toys'),
        ('3', 'Electronics'),
        ('4', 'Home'),
    ]
    category = models.CharField(max_length=64, choices=cat, default=1)
    description = models.CharField(max_length=64, null=True)
    price = models.FloatField(null=True)
    imageURL = models.URLField(null=True)

    def __str__(self):
        return f"{self.title} - {self.category}"


class Bid(models.Model):
    bid = models.FloatField(null=True)

    def __str__(self):
        return f"{self.price}"


class Comment(models.Model):
    comment = models.CharField(max_length=64, null=True)

    def __str__(self):
        return f"{self.comment}"


