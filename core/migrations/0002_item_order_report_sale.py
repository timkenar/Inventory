# Generated by Django 5.1 on 2025-02-19 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('low_stock_threshold', models.PositiveIntegerField(default=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
            ],
        ),
    ]
