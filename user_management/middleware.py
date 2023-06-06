from datetime import datetime
from django.shortcuts import redirect
from django.utils import timezone
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication


class ExpiredTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        user = self.jwt_auth.authenticate(request)
        if user is not None:
            try:
                # Vérifier si le token a expiré
                token = self.jwt_auth.get_validated_token(request)
                expiration_timestamp = token['exp']
                current_timestamp = timezone.now().timestamp()
                if current_timestamp >= expiration_timestamp:
                    # Le token a expiré, déconnecter l'utilisateur et le rediriger vers la page de connexion
                    request.user = None
                    return redirect('user_management:login')
            except TokenError:
                # Gérer les exceptions liées aux tokens (par exemple, token invalide, signature invalide, etc.)
                # Déconnecter l'utilisateur et prendre d'autres mesures si nécessaire
                request.user = None
                return redirect('user_management:login')
        return self.get_response(request)
