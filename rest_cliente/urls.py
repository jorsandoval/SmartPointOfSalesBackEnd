from django.urls import path
from rest_cliente.views import lista_clientes, detalle_cliente
from rest_cliente.viewsLogin import login

urlpatterns = [
    path('lista_clientes', lista_clientes, name="lista_clientes"),
    path('detalle_cliente/<id_cliente>',detalle_cliente, name="detalle_cliente"),
    path('login',login, name="login"),
]