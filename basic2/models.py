from operator import mod
from xml.parsers.expat import model
from django.db import models

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


# SKILL 4 

class Skill4(models.Model):
    skill4 = models.CharField(max_length=100)

def __str__(self):
    return self.skill4
