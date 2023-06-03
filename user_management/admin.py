from django.contrib import admin
from .models import Client, User

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Liste des champs à afficher dans la liste des clients

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'client')  # Liste des champs à afficher dans la liste des utilisateurs
    list_filter = ('role', 'client')  # Options de filtrage
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Champs de recherche
    list_per_page = 20  # Nombre d'utilisateurs à afficher par page
