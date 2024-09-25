from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from .serializer import userSerializer,RegistrarEncargadoSerializer,RegistrarGalponSerializer,RegistrarGranjaSerializer,RegistrarUsuarioSerializer,AlertaSerializer,ConfigurarParametrosSerializer,MedicionesSerializer
from django.contrib.auth.models import User
from .models import registrar_usuario,registrar_encargado,registrar_galpon,registrar_granja,Alerta,configurar_parametros,mediciones
from rest_framework.authtoken.models import Token
from rest_framework import status,generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

@api_view(['POST'])
# @permission_classes([AllowAny])
def register (request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user  = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = userSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
def registrarMediciones(request):
    if request.method == 'POST':
        serializer = MedicionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile (request):
    serializer = userSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class RegistrarGranjaView(generics.ListCreateAPIView):
    queryset = registrar_granja.objects.all()
    serializer_class = RegistrarGranjaSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     if self.request.user.is_staff:
    #         serializer.save()
    #     else:
    #         raise permissions.PermissionDenied("Solo los administradores pueden crear productos")

class RegistrarGranjaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_granja.objects.all()
    serializer_class = RegistrarGranjaSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not self.request.user.is_staff:
                raise permissions.PermissionDenied("Solo los administradores pueden modificar galpones")
        return super().get_permissions()

class RegistrarGalponView(generics.ListCreateAPIView):
    queryset = registrar_galpon.objects.all()
    serializer_class = RegistrarGalponSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarGalponDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_galpon.objects.all()
    serializer_class = RegistrarGalponSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.request.method in ['PUT', 'PATCH', 'DELETE']:
    #         if not self.request.user.is_staff:
    #             raise permissions.PermissionDenied("Solo los administradores pueden modificar galpones")
    #     return super().get_permissions()

class ConfigurarParametrosView(generics.ListCreateAPIView):
    queryset = configurar_parametros.objects.all()
    serializer_class = ConfigurarParametrosSerializer
    permission_classes = [permissions.AllowAny]

class ConfigurarParametrosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = configurar_parametros.objects.all()
    serializer_class = ConfigurarParametrosSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.request.method in ['PUT', 'PATCH', 'DELETE']:
    #         if not self.request.user.is_staff:
    #             raise permissions.PermissionDenied("Solo los administradores pueden modificar galpones")
    #     return super().get_permissions()
    
class MedicionesView(generics.ListCreateAPIView):
    queryset = mediciones.objects.all()
    serializer_class = MedicionesSerializer
    permission_classes = [permissions.AllowAny]

class MedicionesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = mediciones.objects.all()
    serializer_class = MedicionesSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.request.method in ['PUT', 'PATCH', 'DELETE']:
    #         if not self.request.user.is_staff:
    #             raise permissions.PermissionDenied("Solo los administradores pueden modificar galpones")
    #     return super().get_permissions()    

class RegistrarEncargadoView(generics.ListCreateAPIView):
    queryset = registrar_encargado.objects.all()
    serializer_class = RegistrarEncargadoSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarEncargadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_encargado.objects.all()
    serializer_class = RegistrarEncargadoSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.request.method in ['PUT', 'PATCH', 'DELETE']:
    #         if not self.request.user.is_staff:
    #             raise permissions.PermissionDenied("Solo los administradores pueden modificar galpones")
    #     return super().get_permissions()    

class RegistrarUsuarioViewSet(generics.ListCreateAPIView):
    queryset = registrar_usuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_usuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

    # def get_permissions(self):
    #     if self.request.method in ['PUT', 'PATCH', 'DELETE']:
    #         if not self.request.user.is_staff:
    #             raise permissions.PermissionDenied("Solo los administradores pueden modificar galpones")
    #     return super().get_permissions()    
