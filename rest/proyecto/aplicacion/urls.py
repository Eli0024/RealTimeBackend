from django.urls import path
from .views import (UserRegisterView,ObtainAuthTokenView,RegistrarGranjaViewSet,RegistrarGalponViewSet,ConfigurarParametrosViewSet,
    MedicionesViewSet,RegistrarEncargadoViewSet)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', ObtainAuthTokenView.as_view(), name='login'),
    path('granjas/', RegistrarGranjaViewSet.as_view({'get': 'list', 'post': 'create'}), name='granjas-list-create'),
    path('granjas/<int:pk>/', RegistrarGranjaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='granjas-detail'),
    path('galpones/', RegistrarGalponViewSet.as_view({'get': 'list', 'post': 'create'}), name='galpones-list-create'),
    path('galpones/<int:pk>/', RegistrarGalponViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='galpones-detail'),
    path('parametros/', ConfigurarParametrosViewSet.as_view({'get': 'list', 'post': 'create'}), name='parametros-list-create'),
    path('parametros/<int:pk>/', ConfigurarParametrosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='parametros-detail'),
    path('mediciones/', MedicionesViewSet.as_view({'get': 'list'}), name='mediciones-list'),
    path('encargados/', RegistrarEncargadoViewSet.as_view({'get': 'list', 'post': 'create'}), name='encargados-list-create'),
    path('encargados/<int:pk>/', RegistrarEncargadoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='encargados-detail'),
]

