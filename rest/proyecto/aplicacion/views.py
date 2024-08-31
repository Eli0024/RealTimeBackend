import csv
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import (
    registrar_granja,
    registrar_galpon,
    registrar_encargado,
    configurar_parametros,
    mediciones,
    Alerta
)
from .serializers import (
    RegistrarGranjaSerializer,
    RegistrarGalponSerializer,
    RegistrarEncargadoSerializer,
    ConfigurarParametrosSerializer,
    MedicionesSerializer,
    AlertaSerializer,
    UserSerializer
)

# Vistas de Autenticación y Registro

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Crear el usuario
        user = serializer.save()
        # Generar el token para el usuario recién creado
        token = Token.objects.create(user=user)
        # Almacenar el token en la instancia para utilizarlo en la respuesta
        self.token = token

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Agregar el token a la respuesta
        response.data['token'] = self.token.key
        return response

# Vista para autenticar usuarios y obtener un token
class ObtainAuthTokenView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'detail': 'El nombre de usuario y la contraseña son necesarios.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'is_staff': user.is_staff})
        
        return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


# views.py


class UserRoleView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.groups.filter(name='Admin').exists():
            role = 'admin'
        else:
            role = 'user'
        
        return Response({'role': role})

# Vistas del Administrador

class RegistrarGranjaViewSet(viewsets.ModelViewSet):
    queryset = registrar_granja.objects.all()
    serializer_class = RegistrarGranjaSerializer
    permission_classes = [permissions.IsAdminUser]

class RegistrarGalponViewSet(viewsets.ModelViewSet):
    queryset = registrar_galpon.objects.all()
    serializer_class = RegistrarGalponSerializer
    permission_classes = [permissions.IsAdminUser]

class ConfigurarParametrosViewSet(viewsets.ModelViewSet):
    queryset = configurar_parametros.objects.all()
    serializer_class = ConfigurarParametrosSerializer
    permission_classes = [permissions.IsAdminUser]

class MedicionesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = mediciones.objects.all()
    serializer_class = MedicionesSerializer
    permission_classes = [permissions.IsAdminUser]

class RegistrarEncargadoViewSet(viewsets.ModelViewSet):
    queryset = registrar_encargado.objects.all()
    serializer_class = RegistrarEncargadoSerializer
    permission_classes = [permissions.IsAdminUser]

class GenerateReportView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mediciones_report.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Temperatura', 'Humedad', 'Fecha', 'Hora', 'Promedio Temperatura'])

        queryset = mediciones.objects.all()
        for medicion in queryset:
            writer.writerow([
                medicion.id_medicion,
                medicion.temperatura,
                medicion.humedad,
                medicion.fecha,
                medicion.hora,
                medicion.promedio_temperatura
            ])

        return response

# Vistas del Usuario

class VerGranjaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RegistrarGranjaSerializer

    def get_queryset(self):
        user = self.request.user
        return registrar_granja.objects.filter(id_usuario=user)

class VerGalponViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RegistrarGalponSerializer

    def get_queryset(self):
        user = self.request.user
        return registrar_galpon.objects.filter(id_usuario=user)

class VerMedicionesActualesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MedicionesSerializer

    def get_queryset(self):
        user = self.request.user
        galpones = registrar_galpon.objects.filter(id_usuario=user)
        return mediciones.objects.filter(id_config_parametro__in=galpones)

class AlertaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlertaSerializer

    def get_queryset(self):
        user = self.request.user
        return Alerta.objects.filter(id_encargado__id=user.id)
