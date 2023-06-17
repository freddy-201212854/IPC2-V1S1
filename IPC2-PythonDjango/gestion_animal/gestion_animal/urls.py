"""
URL configuration for gestion_animal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from animales.views import lista_animales, crear_animal, actualizar_animal, eliminar_animal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animales/', lista_animales, name='lista_animales'),
    path('animales/crear/', crear_animal, name='crear_animal'),
    path('animales/actualizar/<int:codigo>/', actualizar_animal, name='actualizar_animal'),
    path('animales/eliminar/<int:codigo>/', eliminar_animal, name='eliminar_animal')
]
