from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json
# Threads
from multiprocessing import Pool
import threading, queue

# Import Selenium Crawler 
from blackbox_crawler import controller

# Model
from .models import Novedad, AtencionAlCliente, RegistrarPago, OrdenDePagoPorVigencia

# Create your views here.
""" LOGIN """
#controller.Page.login()


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
            res = controller.AtencionAlCliente.reciboDePago(data['municipio'], data['refCatastral'].zfill(15))

            if res == 'error':
                return HttpResponse(json.dumps(
                    'No se encontro Saldo pendiente en los periodos Seleccionados.',
                    indent=4
                ), content_type="application/json", status=406)

            data['codOrdenPago'] = int(res['codOrdenPago'])
            data['vigencia'] = res['vigencia']
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


@csrf_exempt
def ordenDePagoPorVigencia(request):
    if request.method == 'POST':
        form = OrdenDePagoPorVigencia(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data['municipio'] = request.POST['municipio']
            data['refCatastral'] = request.POST['refCatastral']
            data['vigencia_inicial'] = request.POST['vigencia_inicial']
            data['vigencia_final'] = request.POST['vigencia_final']
            res = controller.AtencionAlCliente.reciboDePagoPorVigencia(data['municipio'], data['refCatastral'].zfill(15), data['vigencia_inicial'])
            if res == 'error':
                return HttpResponse(json.dumps(
                    'No se encontro Saldo pendiente en los periodos Seleccionados.',
                    indent=4
                ), content_type="application/json", status=406)

            data['codOrdenPago'] = int(res['codOrdenPago'])
            data['vigencia'] = res['vigencia']
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
            res = controller.AtencionAlCliente.registrarPago(data['municipio'], data['refCatastral'], data['codRecibo'], data['ctaRecaudadora'])

            if res == 'error':
                return HttpResponse(json.dumps(
                    'Error al registrar el pago.',
                    indent=4
                ), content_type="application/json", status=406)

            data['ultPago'] = res
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


@csrf_exempt
def pazYSalvo(request):
    if request.method == 'POST':
        form = AtencionAlCliente(request.POST)
        data = {}
        if not form.is_valid():
            data['error'] = 'error faltan datos'
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
        else:
            data['municipio'] = request.POST['municipio']
            data['refCatastral'] = request.POST['refCatastral']
            res = controller.AtencionAlCliente.pazYSalvo(data['municipio'], data['refCatastral'])

            if res == 'error':
                return HttpResponse(json.dumps(
                    'Error al generar el paz y salvo.',
                    indent=4
                ), content_type="application/json", status=406)

            data['codPyZ'] = int(res['codPyZ'])
            return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


# @csrf_exempt
# def pagoManual(request):
#     if request.method == 'POST':
#         controller.Actions.goToAtencionAlCliente()
#         form = AtencionAlCliente(request.POST)
#         data = {}
#         if not form.is_valid():
#             data['error'] = 'error faltan datos'
#             return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
#         else:
#             data['municipio'] = request.POST['municipio']
#             data['refCatastral'] = request.POST['refCatastral']
#             controller.AtencionAlCliente.pagoManual(data['municipio'], data['refCatastral'])
#             return HttpResponse(json.dumps(data, indent=4), content_type="application/json")
