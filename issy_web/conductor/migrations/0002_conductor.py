# Generated by Django 2.0b1 on 2017-10-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=264)),
                ('apellido', models.CharField(max_length=264)),
                ('estrellas', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('estado_civil', models.IntegerField()),
                ('ciudad', models.CharField(max_length=50)),
                ('inicio_app', models.DateField()),
                ('total_viajes', models.IntegerField()),
                ('tipo_licencia', models.CharField(max_length=8)),
                ('vencimiento_licencia', models.DateField()),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
