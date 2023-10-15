from rest_framework import serializers
from API.models import Paciente, Medico, Secretaria, Cajero, DisponibilidadDiaria, CitaMedica, ComprobantePago, ComprobanteCobro

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class SecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = '__all__'

class CajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cajero
        fields = '__all__'

class DisponibilidadDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponibilidadDiaria
        fields = '__all__'

class CitaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaMedica
        fields = '__all__'

class ComprobantePagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobantePago
        fields = '__all__'

class ComprobanteCobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobanteCobro
        fields = '__all__'