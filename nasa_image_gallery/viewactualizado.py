from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.services import services_nasa_image_gallery

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.get_all_images()
    favourite_list = services_nasa_image_gallery.get_favourites_by_user(request.user) if request.user.is_authenticated else []
    return images, favourite_list

# función principal de la galería.
def home(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})

# función utilizada en el buscador.
def search(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_query = request.POST.get('query', '').strip()
    
    if not search_query:
        return redirect('home')
    
    filtered_images = [img for img in images if search_query.lower() in img['title'].lower()]
    return render(request, 'home.html', {'images': filtered_images, 'favourite_list': favourite_list, 'search_msg': search_query})

# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = services_nasa_image_gallery.get_favourites_by_user(request.user)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})

@login_required
def saveFavourite(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        services_nasa_image_gallery.save_favourite(request.user, image_id)
    return redirect('home')

@login_required
def deleteFavourite(request):
    if request.method == 'POST':
        favourite_id = request.POST.get('id')
        services_nasa_image_gallery.delete_favourite(request.user, favourite_id)
    return redirect('getAllFavouritesByUser')

@login_required
def exit(request):
    logout(request)
    return redirect('index')