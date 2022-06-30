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

#EndPoint de los detalles
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def detalle_venta(request,id_venta):
    """ 
    Get, update o delete de una venta en especifico.
    Recibe el parametro <id_venta>
    """
    try:
        venta = Venta.objects.get(id_venta=id_venta)
    except Venta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VentaSerializer(venta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(venta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def detalle_medio_pago(request,id_medio_pago):
    """ 
    Get, update o delete de una venta en especifico.
    Recibe el parametro <id_medio_pago>
    """
    try:
        medio_pago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    except medio_pago.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MedioPagoSerializer(medio_pago)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(medio_pago, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        medio_pago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)