from django.contrib.auth.models import AbstractUser
from django.db import models

# This model behaves identically to the default user model
class User(AbstractUser):
    pass

# All of listing product
class AuctionListings(models.Model):
    pass

class Bids(models.Model):
    pass 

class Comment(models.Model):
    pass 


