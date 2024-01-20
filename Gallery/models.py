from django.db import models

# Create your models here.
class Image (models.Model):
 
    image = models.ImageField(verbose_name="Изображение", upload_to="Gallery_images/",
        null=True)

    
        
    class Meta:
       
        verbose_name="Изображение"
            
        verbose_name_plural="Изображения"

    def __str__(self):
            return self.images 