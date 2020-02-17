"""xVoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from kamailio import views as views2
from django.urls import path, include
from rest_framework import routers
from kamailio.api import *
from rest_framework_jwt.views import obtain_jwt_token

router = routers.SimpleRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'recarga', RecargaViewSet, basename='recarga')
router.register(r'consumeApi', ApiUsageViewSet, basename='consumeApi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    #path('getSub/', get_subscriber),
    path('updateBalance/', update_balance),
    #path('recarga/', recarga),
    path('api/',include(router.urls)),
    path('consumeApiOG/', ApiUsageOG),
    path('recargaOG/', RecargaOG),
]
