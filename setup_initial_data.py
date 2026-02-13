import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import SiteConfig, HomeContent, Service, CateringPack

# Create Superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser 'admin' created.")

# Create SiteConfig
if not SiteConfig.objects.exists():
    SiteConfig.objects.create(
        phone="+34 600 000 000",
        whatsapp="34600000000",
        address="Calle Principal 123, Madrid",
        hours="Lunes a Viernes: 8:00 - 20:00\nSábados: 9:00 - 14:00",
    )
    print("SiteConfig created.")

# Create HomeContent
if not HomeContent.objects.exists():
    HomeContent.objects.create(
        hero_title="Dorigen",
        hero_subtitle="Panadería y Cafetería artesanal con el mejor catering de la ciudad.",
    )
    print("HomeContent created.")

# Create Sample Services if none
if not Service.objects.exists():
    Service.objects.create(name="Panadería Artesanal", description="Pan de masa madre horneado a diario.", order=1)
    Service.objects.create(name="Cafetería", description="Café de especialidad y bollería casera.", order=2)
    Service.objects.create(name="Catering", description="Servicio integral para empresas y eventos.", order=3)
    print("Sample Services created.")

# Create Sample Catering Packs
if not CateringPack.objects.exists():
    CateringPack.objects.create(title="Pack Desayuno", description="Café, zumo y surtido de mini bollería.", price_from="8€/persona", order=1)
    CateringPack.objects.create(title="Coffee Break", description="Ideal para reuniones de empresa.", price_from="12€/persona", order=2)
    print("Sample Catering Packs created.")
