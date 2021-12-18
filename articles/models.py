from django.db import models

# Create your models here.
class Articles(models.Model):
    titre=models.CharField(max_length=150)
    contenu=models.TextField()
    slug=models.SlugField(max_length=100)
    date_publication=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(default='default.jpg')
    
    def __str__(self):
        return self.titre