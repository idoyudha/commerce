from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:category>", views.category, name="category"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("view/<str:title>", views.specific, name="specific"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("watchlist/add/<str:title>", views.add_watchlist, name="add_watchlist"),
    path("watchlist/remove/<str:title>", views.remove_watchlist, name="remove_watchlist"),
    path("bid/<str:title>", views.bid, name="bid"),
    path("close_bid/<str:title>", views.close_bid, name="close_bid"),
    path("comment/<str:title>", views.comment, name="comment"),
]
