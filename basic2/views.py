from django.shortcuts import render

# Access Database
<<<<<<< HEAD
from .models import Paragraph, Project
=======
from .models import Paragraph

#Skills
>>>>>>> e77928d5266963a203a859326f0fecd73b032041
from .models import Skill1
from .models import Skill2
from .models import Skill3
from .models import Skill4

#Projects
from .models import Project1



# HOME
def home(request):
    paragraph = Paragraph.objects.all

    #Skills
    skill1 = Skill1.objects.all
    skill2 = Skill2.objects.filter(pk=2)
    skill3 = Skill3.objects.filter(pk=2)
    skill4 = Skill4.objects.filter(pk=3)
    skills1 = "Skill One"
    skills2 = "Skill Two"
    skills3 = "Skill Three"
<<<<<<< HEAD
    project = Project.objects.all
    return render(request, "home.html", {'paragraph': paragraph, 'skill1': skill1,
                                         'skills1': skills1, 'skill2': skill2, 'skills2': skills2,
                                         'skill3': skill3, 'skills3': skills3, 'project': project})
=======
    skills4 = "Skill Four"

    #Projects
    project1 = "Project One"
    tester1 = "This is the Project1 description"
    projects1 = Project1.objects.filter(pk=1)
    return render(request, "home.html", {'paragraph': paragraph, 'skill1': skill1,
                                         'skills1': skills1, 'skill2': skill2, 'skills2': skills2, 
                                                'skill3': skill3, 'skills3': skills3, 'skills4': skills4, 
                                                        'skill4': skill4, 'project1': project1, 'projects1': projects1, 'tester1': tester1})
>>>>>>> e77928d5266963a203a859326f0fecd73b032041
