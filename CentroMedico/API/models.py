from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    appaterno = models.CharField(max_length=100)
    apmaterno = models.CharField(max_length=100)
    gmail = models.EmailField()
    telefono = models.PositiveIntegerField()
    prevision = models.CharField(max_length=100)

class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    appaterno = models.CharField(max_length=100)
    apmaterno = models.CharField(max_length=100)
    gmail = models.EmailField()
    telefono = models.PositiveIntegerField()
    especialidad = models.CharField(max_length=100)

class Secretaria(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    appaterno = models.CharField(max_length=100)
    apmaterno = models.CharField(max_length=100)
    gmail = models.EmailField()
    telefono = models.PositiveIntegerField(default=0)

class Cajero(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.PositiveIntegerField()
    dv = models.CharField(max_length=1)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    appaterno = models.CharField(max_length=100)
    apmaterno = models.CharField(max_length=100)
    gmail = models.EmailField()
    telefono = models.PositiveIntegerField(default=0)

class DisponibilidadDiaria(models.Model):
    id = models.AutoField(primary_key=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class CitaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)  
    hora = models.TimeField(null=True)  
    estado = models.CharField(max_length=100)

class ComprobantePago(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

class ComprobanteCobro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)