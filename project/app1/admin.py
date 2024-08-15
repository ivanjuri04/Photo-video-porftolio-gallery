from django.contrib import admin
from .models import FirstProductPicture,ProductGallery,ProductVideo

# Register your models here.

class ProductGalleryInline(admin.TabularInline):
      model=ProductGallery
      extra=1
      can_delete = True
class ProductVideoInLine(admin.TabularInline):
      model=ProductVideo
      extra=1
      can_delete = True      

class FirstProductPictureAdmin(admin.ModelAdmin):
    list_display=('title','description','images','is_availbile','created_date','modyfied_date')
    inlines=[ProductGalleryInline,ProductVideoInLine]
    

admin.site.register(FirstProductPicture,FirstProductPictureAdmin)
admin.site.register(ProductGallery)
admin.site.register(ProductVideo)


