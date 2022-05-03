from django.shortcuts import render

# Access Database
from .models import Paragraph
from .models import Skill1
from .models import Skill2
from .models import Skill3
from .models import Skill4

# HOME


def home(request):
    paragraph = Paragraph.objects.all
    skill1 = Skill1.objects.all
    skill2 = Skill2.objects.filter(pk=2)
    skill3 = Skill3.objects.filter(pk=2)
    skill4 = Skill4.objects.filter(pk=3)
    skills1 = "Skill One"
    skills2 = "Skill Two"
    skills3 = "Skill Three"
    skills4 = "Skill Four"
    return render(request, "home.html", {'paragraph': paragraph, 'skill1': skill1,
                                         'skills1': skills1, 'skill2': skill2, 'skills2': skills2, 
                                                'skill3': skill3, 'skills3': skills3, 'skills4': skills4, 'skill4': skill4})
