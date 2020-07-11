from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("addcandidate/", views.addcandidate),
    path("viewcandidates/", views.viewcandidates),
    path("register/", views.register),
    path("logout/", views.logout_req),
    path("login/", views.login_req),
]
