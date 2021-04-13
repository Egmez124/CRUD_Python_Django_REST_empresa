# Generated by Django 2.2 on 2021-04-13 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('puestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('puesto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='puestos', to='puestos.Puesto')),
            ],
        ),
    ]
