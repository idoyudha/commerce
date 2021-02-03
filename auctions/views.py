from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms.models import modelformset_factory


from .models import User, AuctionListing, Bid, Comment
from .forms import ListingForm, BidForm, CommentForm


def index(request):
    data = AuctionListing.objects.all()
    context = {
        'data': data,
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return HttpResponseRedirect('/')
    else:
        form = ListingForm()
    context = {
        "form": form
    }
    return render(request, "auctions/new_listing.html", context)

# should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
def specific(request, title):
    x = title.replace("+", " ")
    data = AuctionListing.objects.filter(title=x)
    if request.method == 'POST':
        bid_form = BidForm(request.POST)
        comment_form = CommentForm(request.POST)
        if bid_form.is_valid():
            bid_data = bid_form.save(commit=False)
            bid_data.user = request.user
            bid_data.title = request.title 
            bid_data.save()
            return HttpResponseRedirect('specific')
        if comment_form.is_valid():
            comment_data = comment_form.save(commit=False)
            comment_data.user = request.user
            comment_data.title = request.title 
            comment_data.save()
            return HttpResponseRedirect('specific')
    else:
        bid_form = BidForm()
        comment_form = CommentForm()

    context = {
        "data": data,
        "title": x,
        "bid_form": bid_form,
        "comment_form": comment_form
    }
    return render(request, "auctions/specific.html", context)
