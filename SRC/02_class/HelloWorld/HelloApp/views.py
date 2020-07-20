from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import HelloCandidateForm, NewUserForm
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
@login_required
def viewcandidates(request):
    candidates = HelloCustomer.objects.all()
    # only 2 request per page
    page = Paginator(candidates, 2)
    try:
        # ?page=2 url, comes as 2 to below
        page_number = request.GET.get("page")
        page_object = page.page(page_number)
    except:
        page_object = page.page(1)
    return render(request, "viewcandidates.html", {"page_object": page_object})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            œlogin(request, user)
            return redirect("/")
    else:
        form = NewUserForm()
    return render(request, "register.html", {"form": form})


def logout_req(request):
    logout(request)
    messages.info(request, "Logged out sucessfully")
    return redirect("/")


def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# View Candidate query
# Below code is for query sets.
# q = HelloCustomer.objects.values("full_name", "phone", "email", "dob")
# And , OR
# q = HelloCustomer.objects.filter(full_name__contains="Animesh")
# p = HelloCustomer.objects.filter(full_name__contains="Aru")
# Order By
# q = HelloCustomer.objects.all().order_by("full_name")
# order-by reverse
# q = HelloCustomer.objects.all().order_by("-full_name")
# return render(request, "viewcandidates.html", {"candidates": q})
