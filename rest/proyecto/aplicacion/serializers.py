from rest_framework import serializers
from .models import (
    registrar_granja,
    registrar_galpon,
    registrar_encargado,
    registrar_usuario,
    configurar_parametros,
    mediciones,
    Alerta
)
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_staff']
        # extra_kwargs = {
        #     'email': {'required': True}  # Asegúrate de que el campo email sea requerido
        # }

    # def create(self, validated_data):
    #     # Asegúrate de incluir first_name y last_name si están en validated_data
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #         first_name=validated_data.get('first_name', ''),
    #         last_name=validated_data.get('last_name', '')
    #     )
        
    #     if 'is_staff' in validated_data:
    #         user.is_staff = validated_data['is_staff']
    #         user.save()
        
    #     return user
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

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = registrar_usuario
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
