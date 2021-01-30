from django import forms


class ListingForm(forms.Form):
    title = forms.CharField(max_length=16, widget = forms.TextInput)
    cat = [
        ('1', 'No Category'), 
        ('2', 'Electronics'), 
        ('3', 'Fashions'), 
        ('4', 'Home'), 
        ('5', 'Toys')
    ]
    category = forms.ChoiceField(widget=forms.Select, choices=cat)
    description = forms.CharField(max_length=100, widget = forms.Textarea)
    price = forms.IntegerField(widget = forms.NumberInput)
    imageURL = forms.URLField(label='Image URL (optional)', required=False, widget = forms.URLInput)
    # Widget
    title.widget.attrs.update({'class': 'form-control'})
    category.widget.attrs.update({'class': 'form-control', 'id': 'title'})
    description.widget.attrs.update({'class': 'form-control', 'id': 'description', 'rows': '3'})
    price.widget.attrs.update({'class': 'form-control', 'id': 'price'})
    imageURL.widget.attrs.update({'class': 'form-control', 'id': 'image'})

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