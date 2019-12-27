from django.db import models
from django import forms

# Create your models here.
class Novedad(forms.Form):
    #.IntegerField()
    resolucion = forms.CharField()
    tipo_novedad = forms.CharField()

class ImpuestoPredial(froms.Form, files.FIle):
    cintaIGAC = files.File()