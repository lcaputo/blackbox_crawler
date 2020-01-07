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
    refCatastral = forms.IntegerField()
    codRecibo = forms.IntegerField()
    ctaRecaudadora = forms.IntegerField()



"""class ImpuestoPredial(froms.Form, files.FIle):
    cintaIGAC = files.File()"""