# Generated by Django 4.2.1 on 2023-09-28 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_rename_noticiadirection_noticias_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.PositiveIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('appaterno', models.CharField(max_length=100)),
                ('apmaterno', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateTimeField()),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ComprobanteCobro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ComprobantePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DisponibilidadDiaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=100)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.PositiveIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('appaterno', models.CharField(max_length=100)),
                ('apmaterno', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
                ('telefono', models.PositiveIntegerField()),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.PositiveIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('appaterno', models.CharField(max_length=100)),
                ('apmaterno', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
                ('telefono', models.PositiveIntegerField()),
                ('prevision', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.PositiveIntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('appaterno', models.CharField(max_length=100)),
                ('apmaterno', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
        migrations.DeleteModel(
            name='TypeNotice',
        ),
        migrations.DeleteModel(
            name='TypeUser',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='disponibilidaddiaria',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.medico'),
        ),
        migrations.AddField(
            model_name='comprobantepago',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.paciente'),
        ),
        migrations.AddField(
            model_name='comprobantecobro',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.medico'),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.medico'),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.paciente'),
        ),
    ]
