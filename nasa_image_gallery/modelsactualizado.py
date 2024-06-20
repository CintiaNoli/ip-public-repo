from django.db import models
from django.conf import settings

class Favourite(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.TextField()
    date = models.DateField()
    
    # Asociamos el favorito con el usuario en cuestión.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'title', 'description', 'image_url', 'date')
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return f"{self.title} by {self.user.username}"