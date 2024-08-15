from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FirstProductPicture,ProductGallery,ProductVideo
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method == 'POST':

        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            subject = f"{cd['name']}  || Subject : {cd['subject']}" \
                      
            message = f"Send from email : {cd['email']} \n\n" \
                      f"{cd['name']}\'s message: {cd['message']}"
            send_mail(subject, message, 'ivan1804ju@gmail.com',
                      ['ivan1804ju@gmail.com'])
            sent = True
            

            

    else:
        form = EmailPostForm()

    context={'form': form,} 

    return render (request , 'index.html',context)

def ticket(request):
    return render (request , 'ticket.html')
def portfolio(request):
    pictures=FirstProductPicture.objects.all()
    context={
        'pictures':pictures,
    }
    return render (request , 'portfolio.html',context)

def gallery(request,slug):
    try:
        first_product_picture=FirstProductPicture.objects.get(slug=slug)
        

    except Exception as e:
        raise e
    
   
    ##get the product gallery
    product_gallery=ProductGallery.objects.filter(product_id=first_product_picture.id)

    context={ 
        
        'product_gallery':product_gallery,
        'first_product_picture':first_product_picture,
        'slug':slug,
    }
    
    return render (request , 'gallery.html',context)
def video(request,slug):
    try:
        first_product_picture=FirstProductPicture.objects.get(slug=slug)
        

    except Exception as e:
        raise e
    
   
    ##get the product gallery
    product_video=ProductVideo.objects.filter(product_id=first_product_picture.id)

    context={ 
        
        'product_video':product_video,
        'first_product_picture':first_product_picture,
        'slug':slug,
    }
    
    return render (request , 'video.html',context)
