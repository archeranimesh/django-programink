from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    # only 2 request per page
    page = Paginator(candidates, 2)
    try:
        # ?page=2 url, comes as 2 to below
        page_number = request.GET.get("page")
        page_object = page.page(page_number)
    except:
        page_object = page.page(1)
    return render(request, "viewcandidates.html", {"page_object": page_object})


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
