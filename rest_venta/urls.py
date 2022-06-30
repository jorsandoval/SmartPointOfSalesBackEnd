from django.urls import path
from rest_venta.views import lista_ventas, lista_detalle_ventas, lista_medio_pagos

urlpatterns = [
    path('lista_ventas', lista_ventas, name="lista_ventas"),
    path('lista_detalle_ventas', lista_detalle_ventas, name="lista_detalle_ventas"),
    path('lista_medio_pagos', lista_medio_pagos, name="lista_medio_pagos"),
]
