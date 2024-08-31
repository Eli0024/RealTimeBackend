from rest_framework import serializers
from .models import (
    registrar_granja,
    registrar_galpon,
    registrar_encargado,
    configurar_parametros,
    mediciones,
    Alerta
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(required=False)  

    class Meta:
        model = User
        fields = ['id', 'username','password', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': False},  
        }

    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        
        if 'is_staff' in validated_data:
            user.is_staff = validated_data['is_staff']
            user.save()
        return user

class RegistrarGranjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrar_granja
        fields = '__all__'

class RegistrarGalponSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrar_galpon
        fields = '__all__'

class RegistrarEncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrar_encargado
        fields = '__all__'

class ConfigurarParametrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = configurar_parametros
        fields = '__all__'

class MedicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = mediciones
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
