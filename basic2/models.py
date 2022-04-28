from operator import mod
from xml.parsers.expat import model
from django.db import models

# Create your models here.

# PARAGRAPH


class Paragraph(models.Model):
    paragraph = models.TextField(max_length=500)


def __str__(self):
    return self.paragraph
