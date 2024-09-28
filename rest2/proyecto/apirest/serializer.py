from . models import Custom,Alerta,registrar_encargado,registrar_granja,registrar_usuario,registrar_galpon,mediciones, configurar_parametros
from rest_framework import serializers
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = ['id','imagen','password','username','first_name','last_name','email','is_staff']
        
        extra_kwargs = {
            'is_staff': {'read_only': False}, 
        }
        

        def create(self, validated_data):
            user = Custom.objects.create_user(
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