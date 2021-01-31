from django.contrib.auth.models import AbstractUser
from django.db import models

# This model behaves identically to the default user model
class User(AbstractUser):
    pass

# All of listing product
class AuctionListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    #category
    cat = [
        ('1', 'No Category'),
        ('2', 'Automotive'),
        ('3', 'Electronics'),
        ('4', 'Fashions'),
        ('5', 'Home'),
        ('6', 'Toys')
    ]
    category = models.CharField(max_length=64, choices=cat, default=1)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    imageURL = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.title} - {self.category}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")
    title = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="title_bid")
    bid = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.bid}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    title = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="title_comment")
    comment = models.CharField(max_length=64, null=True)
    def __str__(self):
        return f"{self.user}"


