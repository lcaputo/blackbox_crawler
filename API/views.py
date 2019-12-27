from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

# Import Selenium Crawler 
from blackbox_crawler import controller

# Model
from .models import Novedad,ImpuestoPredial

# Create your views here.
""" LOGIN """
controller.Page.login()

@csrf_exempt
def elaborarNovedad(request):
    if request.method == 'POST':
        controller.Actions.goToNovedades()
        form = Novedad(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data['resolucion'] = request.POST['resolucion']
            data['tipo_novedad'] = request.POST['tipo_novedad']
            controller.Novedad.seleccionar(data['resolucion'],data['tipo_novedad'])
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


@csrf_exempt
def liquidacionImpuestoPredial(request):
    if request.method == 'POST':
        controller.Actions.goToLiquidacionImpuestoPredial()
        form = ImpuestoPredial(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data[''] = request.POST['']
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
