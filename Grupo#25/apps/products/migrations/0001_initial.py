# Generated by Django 2.1.7 on 2019-03-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('producto', models.TextField(blank=True, verbose_name='Producto')),
                ('lote', models.CharField(max_length=100, verbose_name='Lote')),
                ('datecompra', models.CharField(max_length=100, verbose_name='Datecompra')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('evidencia', models.TextField(blank=True, verbose_name='Evidencia')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Changed')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]