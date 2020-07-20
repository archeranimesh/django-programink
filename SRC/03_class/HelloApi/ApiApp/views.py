from django.shortcuts import render
from rest_framework import viewsets
from .models import Blogs
from .serializers import BlogSerializer


def index(request):
    return render(request, "index.html", {})


class BlogView(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
