from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



from .models import (
    registrar_granja,
    registrar_galpon,
    registrar_encargado,
    registrar_usuario,
    configurar_parametros,
    mediciones,
    
)
from .serializers import (
    RegistrarGranjaSerializer,
    RegistrarGalponSerializer,
    RegistrarEncargadoSerializer,
    RegistrarUsuarioSerializer,
    ConfigurarParametrosSerializer,
    MedicionesSerializer,
    userSerializer
)

# Vistas de Autenticación y Registro

# class UserRegisterView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     def perform_create(self, serializer):
#         # Crear el usuario
#         user = serializer.save()
#         # Generar el token para el usuario recién creado
#         token = Token.objects.create(user=user)
#         # Almacenar el token en la instancia para utilizarlo en la respuesta
#         self.token = token

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         # Agregar el token a la respuesta
#         response.data['token'] = self.token.key
#         return response

# class MyTokenObtainPairView(TokenObtainPairView):
#     pass

# class MyTokenRefreshView(TokenRefreshView):
#     pass

# @api_view(['POST'])
# # @permission_classes([AllowAny])
# def login(request):
#     user = get_object_or_404(User, username=request.data['username'])

#     if not user.check_password(request.data['password']):
#         return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = UserSerializer(instance=user)
    
#     return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = userSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([AllowAny])

def register (request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para autenticar usuarios y obtener un token
# class ObtainAuthTokenView(generics.GenericAPIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         if not username or not password:
#             return Response({'detail': 'El nombre de usuario y la contraseña son necesarios.'}, status=status.HTTP_400_BAD_REQUEST)
        
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, 'is_staff': user.is_staff})
        
#         return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


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

@api_view(['POST'])
def registrarMediciones(request):
    if request.method == 'POST':
        serializer = MedicionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
