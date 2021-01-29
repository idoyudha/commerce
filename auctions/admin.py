from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, AuctionListing, Bid, Comment

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
