from django import forms


class ListingForm(forms.Form):
    title = forms.CharField(max_length=16, widget = forms.TextInput)
    cat = [('1', 'Fashions'), ('2', 'Toys'), ('3', 'Electronics'), ('4', 'Home')]
    category = forms.ChoiceField(widget=forms.Select, choices=cat)
    description = forms.CharField(max_length=100, widget = forms.Textarea)
    price = forms.IntegerField(widget = forms.NumberInput)
    imageURL = forms.URLField(label='Image URL', required=False, widget = forms.URLInput)

    title.widget.attrs.update({'class': 'form-control'})
    category.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control', 'rows': '2'})
    price.widget.attrs.update({'class': 'form-control'})
    imageURL.widget.attrs.update({'class': 'form-control'})

class BidForm(forms.Form):
    comment = forms.CharField(max_length=64, widget = forms.NumberInput)

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=64, required=False, widget = forms.Textarea)