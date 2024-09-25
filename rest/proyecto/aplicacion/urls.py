from django.urls import path

from . import views



from .views import (
    ConfigurarParametrosDetailView,
    MedicionesDetailView,
    RegistrarEncargadoDetailView,
    RegistrarGalponDetailView,
    RegistrarGranjaDetailView,
    RegistrarGranjaView,
    RegistrarGalponView,
    ConfigurarParametrosView,
    MedicionesView,
    RegistrarEncargadoView
)


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('galpones/', RegistrarGalponView.as_view(), name='galpon_list'),
    path('galpones/<int:pk>/', RegistrarGalponDetailView.as_view(), name='galpon_detail'),
    path('granjas/', RegistrarGranjaView.as_view(), name='granja_list'),
    path('granjas/<int:pk>/', RegistrarGranjaDetailView.as_view(), name='granja_detail'),
    path('parametros/', ConfigurarParametrosView.as_view(), name='parametro_list'),
    path('parametros/<int:pk>/', ConfigurarParametrosDetailView.as_view(), name='parametro_detail'),
    path('mediciones/', MedicionesView.as_view(), name='medicion_list'),
    path('mediciones/<int:pk>/', MedicionesDetailView.as_view(), name='medicion_detail'),
    path('encargados/', RegistrarEncargadoView.as_view(), name='encargado_list'),
    path('encargados/<int:pk>/', RegistrarEncargadoDetailView.as_view(), name='granja_list'),
    path('mediciones/',views.registrarMediciones, name='mediciones'),
    path('encargados/<int:pk>/', RegistrarEncargadoDetailView.as_view(), name='encargado_detail')
]


