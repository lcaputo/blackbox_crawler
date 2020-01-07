from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json
# Threads
from concurrent.futures import ThreadPoolExecutor

# Import Selenium Crawler 
from blackbox_crawler import controller

# Model
from .models import Novedad, AtencionAlCliente, RegistrarPago

# Create your views here.
""" LOGIN """
#controller.Page.login()
executor = ThreadPoolExecutor(max_workers=3)

@csrf_exempt
def elaborarNovedad(request):
    if request.method == 'POST':
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
def ordenPago(request):
    if request.method == 'POST':
        form = AtencionAlCliente(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data['municipio'] = request.POST['municipio']
            data['refCatastral'] = request.POST['refCatastral']
            executor.submit(controller.AtencionAlCliente.reciboDePago(data['municipio'], data['refCatastral']))
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

@csrf_exempt
def registrarPago(request):
    if request.method == 'POST':
        form = RegistrarPago(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data['municipio'] = request.POST['municipio']
            data['refCatastral'] = request.POST['refCatastral']
            data['codRecibo'] = request.POST['codRecibo']
            data['ctaRecaudadora'] = request.POST['ctaRecaudadora']
            controller.AtencionAlCliente.registrarPago(data['municipio'], data['refCatastral'], data['codRecibo'], data['ctaRecaudadora'])
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


@csrf_exempt
def pazYSalvo(request):
    if request.method == 'POST':
        controller.Actions.goToAtencionAlCliente()
        form = AtencionAlCliente(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data['municipio'] = request.POST['municipio']
            data['refCatastral'] = request.POST['refCatastral']
            controller.AtencionAlCliente.pazYSalvo(data['municipio'], data['refCatastral'])
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


