from django import forms
from django.forms import ModelForm
from auctions.models import AuctionListing, Bid, Comment


class ListingForm(ModelForm):
    class Meta(object):
        model = AuctionListing
        # we can use exclude or __all__ in this field below
        exclude = ('user_auction', 'time', 'watchlist', 'active_bid')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': 3 }),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price'}),
            'imageURL': forms.URLInput(attrs={'class': 'form-control', 'id': 'image'})
        }

class BidForm(ModelForm):
    class Meta(object):
        model = Bid
        fields = ['amount_bid']
        widgets = {
            'amount_bid': forms.NumberInput(attrs={'class': 'form-control', 'id': 'amount_bid'})
        }

class CommentForm(ModelForm):
    class Meta(object):
        model = Comment
        fields = ['comment_user']
        widgets = {
            'comment_user': forms.Textarea(attrs={'class': 'form-control', 'id': 'comment_user', 'rows': 2 })
        }
