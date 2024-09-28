from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from .serializer import userSerializer,RegistrarEncargadoSerializer,RegistrarGalponSerializer,RegistrarGranjaSerializer,RegistrarUsuarioSerializer,AlertaSerializer,ConfigurarParametrosSerializer,MedicionesSerializer
from .models import Custom,registrar_usuario,registrar_encargado,registrar_galpon,registrar_granja,Alerta,configurar_parametros,mediciones
from rest_framework.authtoken.models import Token
from rest_framework import status,generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

@api_view(['POST'])
def register (request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user  = Custom.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(Custom, username=request.data['username'])
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
@permission_classes([AllowAny])
def lista_user(request):
    custom = Custom.objects.all()
    serializer = userSerializer(custom, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def eliminar_usuarios(request,pk):
    try:
        user = Custom.objects.get(pk=pk)
    except Custom.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({'message': 'Usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def actualizar_Usuario(request, pk):
    try:
        user = Custom.objects.get(pk=pk)
    except Custom.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = userSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
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
    authentication_classes =[TokenAuthentication]

  
class RegistrarGranjaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_granja.objects.all()
    serializer_class = RegistrarGranjaSerializer
    authentication_classes =[TokenAuthentication]


class RegistrarGalponView(generics.ListCreateAPIView):
    queryset = registrar_galpon.objects.all()
    serializer_class = RegistrarGalponSerializer
    authentication_classes =[TokenAuthentication]

class RegistrarGalponDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_galpon.objects.all()
    serializer_class = RegistrarGalponSerializer
    authentication_classes =[TokenAuthentication]



class ConfigurarParametrosView(generics.ListCreateAPIView):
    queryset = configurar_parametros.objects.all()
    serializer_class = ConfigurarParametrosSerializer
    authentication_classes =[TokenAuthentication]

class ConfigurarParametrosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = configurar_parametros.objects.all()
    serializer_class = ConfigurarParametrosSerializer
    authentication_classes =[TokenAuthentication]
    
class MedicionesView(generics.ListCreateAPIView):
    queryset = mediciones.objects.all()
    serializer_class = MedicionesSerializer
    authentication_classes =[TokenAuthentication]

class MedicionesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = mediciones.objects.all()
    serializer_class = MedicionesSerializer
    authentication_classes =[TokenAuthentication]

class RegistrarEncargadoView(generics.ListCreateAPIView):
    queryset = registrar_encargado.objects.all()
    serializer_class = RegistrarEncargadoSerializer
    authentication_classes =[TokenAuthentication]

class RegistrarEncargadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_encargado.objects.all()
    serializer_class = RegistrarEncargadoSerializer
    authentication_classes =[TokenAuthentication]



class RegistrarUsuarioViewSet(generics.ListCreateAPIView):
    queryset = registrar_usuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    authentication_classes =[TokenAuthentication]

class RegistrarUsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrar_usuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [permissions.AllowAny]

