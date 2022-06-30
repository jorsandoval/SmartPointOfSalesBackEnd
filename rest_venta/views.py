from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Venta, DetalleVenta, MedioPago
from .serializers import DetalleVentaSerializer, MedioPagoSerializer, VentaSerializer
# Create your views here.

#EndPoint de Ventas
@csrf_exempt
@api_view(['GET','POST'])
def lista_ventas(request):
    """
    Lista todas las ventas realizadas
    """
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view

        
#EndPoint de Detalle de las ventas
@csrf_exempt
@api_view(['GET','POST'])
def lista_detalle_ventas(request):
    """ 
    Lista todos los detalle de las ventas realizadas
    """
    if request.method == 'GET':
        detalle_venta = DetalleVenta.objects.all()
        serializer = DetalleVentaSerializer(detalle_venta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DetalleVentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#EndPoint de medio de pago
@csrf_exempt
@api_view(['GET','POST'])
def lista_medio_pagos(request):
    """ 
    Lista todos los medios de pagos existetes
    """
    if request.method == 'GET':
        mediopago = MedioPago.objects.all()
        serializer = MedioPagoSerializer(mediopago, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MedioPagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
