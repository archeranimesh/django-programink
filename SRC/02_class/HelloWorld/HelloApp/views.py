from django.shortcuts import render, redirect
from .forms import HelloCandidateForm
from .models import HelloCustomer

# Create your views here.
def index(request):
    return render(request, "index.html", {})


# Add Candidate
def addcandidate(request):
    form = HelloCandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "addcandidate.html", {"form": form})


# View Candidate
def viewcandidates(request):
    candidates = HelloCustomer.objects.all()
    return render(request, "viewcandidates.html", {"candidates": candidates})
