from django.urls import path
from apps.authentication.views import get_registred_whatsapp_numbers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Gera um novo token de acesso e refresh
    TokenRefreshView,      # Atualiza o token de acesso usando o refresh token
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('whatsapp_numbers/', get_registred_whatsapp_numbers, name='whatsapp_numbers')
]
