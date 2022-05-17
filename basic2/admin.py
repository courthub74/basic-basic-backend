from django.contrib import admin

# Paragraph
from .models import Paragraph

# Skill
from .models import Skill1
from .models import Skill2
from .models import Skill3
from .models import Skill4

#PORTFOLIO
from .models import Project

# Register your models here.

# PARAGRAPH
admin.site.register(Paragraph)

# SKILLS
admin.site.register(Skill1)
admin.site.register(Skill2)
admin.site.register(Skill3)
admin.site.register(Skill4)

#PORTFOLIO
admin.site.register(Project)
