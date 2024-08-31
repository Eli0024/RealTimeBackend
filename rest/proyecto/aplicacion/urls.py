from django.urls import path
from .views import (UserRegisterView,ObtainAuthTokenView,RegistrarGranjaViewSet,RegistrarGalponViewSet,ConfigurarParametrosViewSet,
    MedicionesViewSet,RegistrarEncargadoViewSet,GenerateReportView, UserRoleView,VerGranjaViewSet,VerGalponViewSet,VerMedicionesActualesViewSet,
    AlertaViewSet)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', ObtainAuthTokenView.as_view(), name='login'),
    path('user-role/', UserRoleView.as_view(), name='user-role'),
    path('granjas/', RegistrarGranjaViewSet.as_view({'get': 'list', 'post': 'create'}), name='granjas-list-create'),
    path('granjas/<int:pk>/', RegistrarGranjaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='granjas-detail'),
    path('galpones/', RegistrarGalponViewSet.as_view({'get': 'list', 'post': 'create'}), name='galpones-list-create'),
    path('galpones/<int:pk>/', RegistrarGalponViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='galpones-detail'),
    path('parametros/', ConfigurarParametrosViewSet.as_view({'get': 'list', 'post': 'create'}), name='parametros-list-create'),
    path('parametros/<int:pk>/', ConfigurarParametrosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='parametros-detail'),
    path('mediciones/', MedicionesViewSet.as_view({'get': 'list'}), name='mediciones-list'),
    path('encargados/', RegistrarEncargadoViewSet.as_view({'get': 'list', 'post': 'create'}), name='encargados-list-create'),
    path('encargados/<int:pk>/', RegistrarEncargadoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='encargados-detail'),
    path('report/', GenerateReportView.as_view(), name='generate_report'),
    path('ver_granjas/', VerGranjaViewSet.as_view({'get': 'list'}), name='ver_granjas'),
    path('ver_galpones/', VerGalponViewSet.as_view({'get': 'list'}), name='ver_galpones'),
    path('ver_mediciones/', VerMedicionesActualesViewSet.as_view({'get': 'list'}), name='ver_mediciones'),
    path('alertas/', AlertaViewSet.as_view({'get': 'list'}), name='alertas-list'),
]

