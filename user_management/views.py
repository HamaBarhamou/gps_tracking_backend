from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.utils import timezone
from django.conf import settings
""" from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
 """


""" @authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated]) """

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Vérifier si un token de rafraîchissement existe déjà pour l'utilisateur
            try:
                refresh_token = RefreshToken.objects.get(user=user)
                token = refresh_token.access_token
                
                # Vérifier si le token est expiré
                current_time = timezone.now()
                expires_at = refresh_token.expires_at
                if expires_at > current_time:
                    # Le token n'est pas expiré, le réutiliser
                    token = refresh_token.access_token
                else:
                    # Le token est expiré, générer un nouveau token de rafraîchissement
                    refresh_token.delete()
                    refresh_token = RefreshToken.for_user(user)
                    token = refresh_token.access_token
            
            except:
                # Générer un nouveau token de rafraîchissement
                refresh_token = RefreshToken.for_user(user)
                token = refresh_token.access_token
            
            # Enregistrer le token d'accès dans les cookies
            response = HttpResponseRedirect(reverse('dashboard'))
            response.set_cookie('access_token', token, httponly=True)
            return response
        else:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('user_management:login')  # Rediriger vers la page de connexion après la déconnexion
