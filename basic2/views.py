from django.shortcuts import render

# Access Database
from .models import Paragraph

# HOME


def home(request):
    paragraph = Paragraph.objects.all
    return render(request, "home.html", {'paragraph': paragraph})
