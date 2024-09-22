from django.urls import path
<<<<<<< HEAD
from . import views
from .views import (ConfigurarParametrosDetailView, MedicionesDetailView, RegistrarEncargadoDetailView, RegistrarGalponDetailView, RegistrarGranjaDetailView, UserRegisterView,ObtainAuthTokenView,RegistrarGranjaView,RegistrarGalponView,ConfigurarParametrosView,
    MedicionesView,RegistrarEncargadoView)

=======
from .views import (
    ConfigurarParametrosDetailView,
    MedicionesDetailView,
    RegistrarEncargadoDetailView,
    RegistrarGalponDetailView,
    RegistrarGranjaDetailView,
    UserRegisterView,
    ObtainAuthTokenView,
    RegistrarGranjaView,
    RegistrarGalponView,
    ConfigurarParametrosView,
    MedicionesView,
    RegistrarEncargadoView
)
>>>>>>> 6be11885a2c94acc62a0f909081d61ee60b47288

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', ObtainAuthTokenView.as_view(), name='login'),
    path('galpones/', RegistrarGalponView.as_view(), name='galpon_list'),
    path('galpones/<int:pk>/', RegistrarGalponDetailView.as_view(), name='galpon_detail'),
    path('granjas/', RegistrarGranjaView.as_view(), name='granja_list'),
    path('granjas/<int:pk>/', RegistrarGranjaDetailView.as_view(), name='granja_detail'),
    path('parametros/', ConfigurarParametrosView.as_view(), name='parametro_list'),
    path('parametros/<int:pk>/', ConfigurarParametrosDetailView.as_view(), name='parametro_detail'),
    path('mediciones/', MedicionesView.as_view(), name='medicion_list'),
    path('mediciones/<int:pk>/', MedicionesDetailView.as_view(), name='medicion_detail'),
    path('encargados/', RegistrarEncargadoView.as_view(), name='encargado_list'),
<<<<<<< HEAD
    path('encargados/<int:pk>/', RegistrarEncargadoDetailView.as_view(), name='granja_list'),
    path('mediciones/',views.registrarMediciones, name='mediciones')
=======
    path('encargados/<int:pk>/', RegistrarEncargadoDetailView.as_view(), name='encargado_detail'),
>>>>>>> 6be11885a2c94acc62a0f909081d61ee60b47288
]
