from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("addcandidate/", views.addcandidate),
    path("viewcandidates/", views.viewcandidates),
]
