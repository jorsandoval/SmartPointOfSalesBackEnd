# Generated by Django 4.0.5 on 2022-06-30 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de cliente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del cliente')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellido del cliente')),
                ('correo', models.CharField(max_length=200, verbose_name='Correo del cliente')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección del cliente')),
            ],
        ),
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id_medio_pago', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del medio de pago')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre del medio de pago')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del producto')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion del producto')),
                ('precio', models.IntegerField(verbose_name='Precio del producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de la venta')),
                ('monto', models.IntegerField(verbose_name='Monto Total')),
                ('fecha', models.CharField(max_length=10, verbose_name='Fecha de la venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Identificador del cliente')),
                ('medioPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mediopago', verbose_name='Medio de pago')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalle_venta', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del detalle de venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto', verbose_name='Identificador del producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta', verbose_name='Identificador de la venta')),
            ],
        ),
    ]
