from django.urls import path
from .views import (UserRegisterView,ObtainAuthTokenView,RegistrarGranjaView,RegistrarGalponView,ConfigurarParametrosView,
    MedicionesView,RegistrarEncargadoView)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', ObtainAuthTokenView.as_view(), name='login'),
    path('galpones/', RegistrarGalponView.as_view(), name='galpon_list'),
    path('galpones/create/', RegistrarGalponView.as_view(), name='galpon_list'),
    path('granjas/', RegistrarGranjaView.as_view(), name='granja_list'),
    path('parametros/', ConfigurarParametrosView.as_view(), name='parametro_list'),
    path('mediciones/', MedicionesView.as_view(), name='medicion_list'),
    path('encargados/', RegistrarEncargadoView.as_view(), name='encargado_list'),
]

