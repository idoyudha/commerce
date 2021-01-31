from django import forms
from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import TextInput, Textarea
from auctions.models import AuctionListing, Bid, Comment
from django.utils.translation import gettext_lazy as _


class ListingForm(ModelForm):
    class Meta(object):
        model = AuctionListing
        # we can use exclude or __all__ in this field below
        exclude = ('user',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': 3 }),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price'}),
            'imageURL': forms.URLInput(attrs={'class': 'form-control', 'id': 'image'})
        }

class BidForm(forms.Form):
    bid = forms.IntegerField(widget = forms.NumberInput)
    bid.widget.attrs.update({'class': 'form-control'})
    # Widget
    bid.widget.attrs.update({'class': 'form-control', 'id': 'bid'})

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=64, required=False, widget = forms.Textarea)
    comment.widget.attrs.update({'class': 'form-control'})
    # Widget
    comment.widget.attrs.update({'class': 'form-control', 'id': 'comment'})