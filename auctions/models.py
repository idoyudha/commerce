from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# This model behaves identically to the default user model
class User(AbstractUser):
    pass

# All of listing product
class AuctionListing(models.Model):
    user_auction = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    active_bid = models.BooleanField(default=True)
    #category
    cat = [
        ('No Category', 'No Category'),
        ('Automotive', 'Automotive'),
        ('Electronics', 'Electronics'),
        ('Fashions', 'Fashions'),
        ('Home', 'Home'),
        ('Toys', 'Toys')
    ]
    category = models.CharField(max_length=64, choices=cat, default=1)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    imageURL = models.URLField(null=True, blank=True)
    time = models.DateTimeField(default=datetime.now)
    watchlist = models.ManyToManyField(User, related_name='user_watchlist', blank=True)

    def __str__(self):
        return f"{self.title} - {self.category}"


class Bid(models.Model):
    amount_bid = models.PositiveIntegerField(default=0)
    user_bid = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    
class Comment(models.Model):
    comment_user = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


