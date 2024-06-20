from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Favourite
from datetime import date

class FavouriteModelTest(TestCase):
    
    def setUp(self):
        # Configuramos un usuario para usar en las pruebas.
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Configuramos un favorito para usar en las pruebas.
        self.favourite = Favourite.objects.create(
            title='Test Title',
            description='Test Description',
            image_url='http://example.com/image.jpg',
            date=date.today(),
            user=self.user
        )
    
    def test_favourite_creation(self):
        # Comprobamos que el favorito se ha creado correctamente.
        self.assertEqual(self.favourite.title, 'Test Title')
        self.assertEqual(self.favourite.description, 'Test Description')
        self.assertEqual(self.favourite.image_url, 'http://example.com/image.jpg')
        self.assertEqual(self.favourite.date, date.today())
        self.assertEqual(self.favourite.user, self.user)
    
    def test_favourite_str_method(self):
        # Comprobamos que el método __str__ devuelve el string correcto.
        expected_string = f"{self.favourite.title} by {self.user.username}"
        self.assertEqual(str(self.favourite), expected_string)
    
    def test_favourites_deleted_when_user_deleted(self):
        # Comprobamos que los favoritos se eliminan cuando se elimina el usuario.
        self.user.delete()
        favourites = Favourite.objects.filter(user=self.user)
        self.assertEqual(favourites.count(), 0)
    
    def test_unique_together_constraint(self):
        # Comprobamos la restricción de unicidad.
        with self.assertRaises(Exception):
            Favourite.objects.create(
                title='Test Title',
                description='Test Description',
                image_url='http://example.com/image.jpg',
                date=date.today(),
                user=self.user
            )

# Ejecutamos los tests
if __name__ == '__main__':
    TestCase.main()