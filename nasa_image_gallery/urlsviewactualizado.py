from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Páginas principales
    path('', views.index_page, name='index-page'),  # Página principal
    path('login/', views.index_page, name='login'),  # Página de inicio de sesión
    
    # Páginas de la aplicación
    path('home/', views.home, name='home'),  # Página de inicio (dashboard)
    path('buscar/', views.search, name='buscar'),  # Página de búsqueda
    
    # Favoritos
    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),  # Lista de favoritos del usuario
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),  # Agregar un favorito
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),  # Borrar un favorito
    
    # Salida (cerrar sesión)
    path('exit/', views.exit, name='exit'),  # Página de salida (cerrar sesión)
]