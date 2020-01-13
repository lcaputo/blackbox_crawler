from django.db import models
from django import forms

# Create your models here.
class Novedad(forms.Form):
    #.IntegerField()
    resolucion = forms.CharField()
    tipo_novedad = forms.CharField()

class AtencionAlCliente(forms.Form):
    municipio = forms.CharField()
    refCatastral = forms.IntegerField()

class RegistrarPago(forms.Form):
    municipio = forms.CharField()
    refCatastral = forms.CharField()
    codRecibo = forms.CharField()
    ctaRecaudadora = forms.CharField()



"""class ImpuestoPredial(froms.Form, files.FIle):
    cintaIGAC = files.File()"""