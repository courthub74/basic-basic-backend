from operator import mod
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models
from django.forms import CharField, Textarea

# Create your models here.

# PARAGRAPH


class Paragraph(models.Model):
    paragraph = models.TextField(max_length=500)


def __str__(self):
    return self.paragraph


# SKILLS

# SKILL 1
class Skill1(models.Model):
    skill1 = models.CharField(max_length=100)


def __str__(self):
    return self.skill1

# SKILL 2


class Skill2(models.Model):
    skill2 = models.CharField(max_length=100)


def __str__(self):
    return self.skill2


# SKILL 3


class Skill3(models.Model):
    skill3 = models.CharField(max_length=100)


def __str__(self):
    return self.skill3


<<<<<<< HEAD
# PROJECT 1

class Project(models.Model):
    project = models.CharField(max_length=500)


def __str__(self):
    return self.project
=======
# SKILL 4 

class Skill4(models.Model):
    skill4 = models.CharField(max_length=100)

def __str__(self):
    return self.skill4


#PROJECTS

# PROJECT 1

class Project(models.Model):
    project = models.TextField(max_length=500)

def __str__(self):
<<<<<<< HEAD
    return self.project
=======
    return self.project1
>>>>>>> e77928d5266963a203a859326f0fecd73b032041
>>>>>>> f7c0d89cd928d0a5ca8172d0cb3b76a2cecc7c06
