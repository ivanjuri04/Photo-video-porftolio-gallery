from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class FirstProductPicture(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.CharField(max_length=500,blank=True)
    images=models.ImageField(upload_to='photos/pictures')
    is_availbile=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modyfied_date=models.DateTimeField(auto_now=True)

 

    def get_url(self):
        return reverse ('gallery',args=[self.slug])
    def get_urll(self):
        return reverse ('video',args=[self.slug])
    
    def __str__(self):
        return self.title
    
 
class ProductGallery(models.Model):
    product=models.ForeignKey(FirstProductPicture,default=None,on_delete=models.CASCADE)    
    image=models.ImageField(upload_to='photos/pictures',max_length=255)

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name='productgallery'
        verbose_name_plural='product gallery'   

class ProductVideo(models.Model):
    product=models.ForeignKey(FirstProductPicture,default=None,on_delete=models.CASCADE)    
    video=models.FileField(upload_to='videos/clips')

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name='productvideo'
        verbose_name_plural='product video'


    