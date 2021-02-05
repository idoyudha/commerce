from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import User, AuctionListing, Bid, Comment
from .forms import ListingForm, BidForm, CommentForm



def index(request):
    data = AuctionListing.objects.all()
    # watchlist button config
    user = request.user.id
    data_watchlist = AuctionListing.objects.filter(watchlist=user).values_list('id', flat=True)
    context = {
        'data': data,
        'data_watchlist': data_watchlist
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

@login_required(login_url='/login/')
def new_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_auction = request.user
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
    data = AuctionListing.objects.filter(title=title)
    bid_form = BidForm()
    comment_form = CommentForm()
    # query id of auction
    pk = AuctionListing.objects.values('pk').get(title=title)
    id = pk.get('pk')
    # query bid
    bid_queryset = Bid.objects.values_list('amount_bid', flat=True).filter(listing=id)
    highest_bid = bid_queryset.order_by('amount_bid').last()
    # query comment
    comment_queryset = Comment.objects.filter(listing=id)
    comments = comment_queryset.order_by('-time')
    # watchlist button config
    user = request.user.id
    data_watchlist = AuctionListing.objects.filter(watchlist=user).values_list('id', flat=True)
    context = {
        "data": data,
        "title": title,
        "data_watchlist": data_watchlist,
        "bid_form": bid_form,
        "comment_form": comment_form,
        "bid": highest_bid,
        "comments":comments
    }
    return render(request, "auctions/specific.html", context)

def bid(request, title):
    data = AuctionListing.objects.filter(title=title)
    price = AuctionListing.objects.values_list('price', flat=True).filter(title=title).last()
    # bid query
    pk = AuctionListing.objects.values('pk').get(title=title)
    id = pk.get('pk')
    bid_queryset = Bid.objects.values_list('amount_bid', flat=True).filter(listing=id)
    highest_bid = bid_queryset.order_by('amount_bid').last()
    highest_bid = 0 if highest_bid is None else highest_bid
    # query comment
    comment_queryset = Comment.objects.filter(listing=id)
    comments = comment_queryset.order_by('-time')
    if request.method == 'POST':
        bid_form = BidForm(request.POST)
        bid = int(request.POST.get('amount_bid'))
        if bid_form.is_valid() and bid > highest_bid and bid > price:
            bid_data = bid_form.save(commit=False)
            bid_data.user_bid = request.user
            bid_data.listing = AuctionListing.objects.get(title=title)
            bid_data.save()
            # return highest bid after saving
            highest_bid = bid_queryset.order_by('amount_bid').last()
            context = {
                "data": data,
                "title": title,
                "bid_form": BidForm(),
                "comment_form": CommentForm(),
                "bid": highest_bid,
                "message1": 'Bid success!',
                "comments": comments
            }
            return render(request, "auctions/specific.html", context)
        else:
            context = {
            "data": data,
            "title": title,
            "bid_form": bid_form,
            "bid": highest_bid,
            "comment_form": CommentForm(),
            "message2": 'Bid must be greater than last bid or starting price',
            "comments": comments
            }
            return render(request, "auctions/specific.html", context)

    else:
        context = {
            "data": data,
            "title": title,
            "bid_form": BidForm(),
            "bid": highest_bid,
            "comment_form": CommentForm()
        }
        return render(request, "auctions/specific.html", context)

@login_required(login_url='/login/')
def watchlist(request):
    user = request.user.id
    data = AuctionListing.objects.filter(watchlist=user)
    context = {
        'data': data
    }
    return render(request, 'auctions/watchlist.html', context)
    

@login_required(login_url='/login/')
def comment(request, title):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_data = comment_form.save(commit=False)
            comment_data.user = request.user
            comment_data.listing = AuctionListing.objects.get(title=title)
            comment_data.save()
            return redirect('specific', title=title)
    else:
        comment_form = CommentForm()
    return redirect('specific', title=title)