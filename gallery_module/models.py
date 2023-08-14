from django.db import models

# Create your models here.

class AnimalGallery(models.Model):
    title = models.CharField(max_length=300, verbose_name='ایدی عکس', blank=True, null=True)
    image = models.ImageField(upload_to='gallery/', verbose_name='عکس')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return f'image {self.id}'
    
    def save(self, **kwargs):
        self.title = f'picture-{self.id}'
        super().save(**kwargs)
    
    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'