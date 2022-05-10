from django.shortcuts import render

# Access Database
from .models import Paragraph, Project
from .models import Skill1
from .models import Skill2
from .models import Skill3

# HOME


def home(request):
    paragraph = Paragraph.objects.all
    skill1 = Skill1.objects.all
    skill2 = Skill2.objects.all
    skill3 = Skill3.objects.all
    skills1 = "Skill One"
    skills2 = "Skill Two"
    skills3 = "Skill Three"
    project = Project.objects.all
    return render(request, "home.html", {'paragraph': paragraph, 'skill1': skill1,
                                         'skills1': skills1, 'skill2': skill2, 'skills2': skills2,
                                         'skill3': skill3, 'skills3': skills3, 'project': project})
