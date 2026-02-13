from django.shortcuts import render
from .models import HomeContent, Service, CateringPack, GalleryImage

def home(request):
    try:
        content = HomeContent.load()
    except:
        content = None
        
    services = Service.objects.all()
    catering_packs = CateringPack.objects.all()
    gallery_images = GalleryImage.objects.all()

    context = {
        'content': content,
        'services': services,
        'catering_packs': catering_packs,
        'gallery_images': gallery_images,
    }
    return render(request, 'core/home.html', context)
