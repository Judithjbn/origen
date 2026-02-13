from django.db import models
from django.core.exceptions import ValidationError

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():

            pass
        return super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteConfig(SingletonModel):
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp")
    whatsapp_message = models.TextField(verbose_name="Mensaje predefinido WhatsApp", default="Hola 😊 Me gustaría información sobre catering.")
    address = models.TextField(verbose_name="Dirección")
    hours = models.TextField(verbose_name="Horarios")
    google = models.URLField(blank=True, verbose_name="Google")
    instagram = models.URLField(blank=True, verbose_name="Instagram")

    def __str__(self):
        return "Configuración del Sitio"

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuración del Sitio"

class HomeContent(SingletonModel):
    hero_title = models.CharField(max_length=200, verbose_name="Titular Hero")
    hero_subtitle = models.TextField(verbose_name="Subtítulo Hero")
    cta_text = models.CharField(max_length=50, default="Contactar por WhatsApp", verbose_name="Texto Botón CTA")
    
    services_title = models.CharField(max_length=100, default="Nuestros Servicios", verbose_name="Título Servicios")
    catering_title = models.CharField(max_length=100, default="Catering para Eventos", verbose_name="Título Catering")
    gallery_title = models.CharField(max_length=100, default="Galería", verbose_name="Título Galería")

    def __str__(self):
        return "Contenido Home"

    class Meta:
        verbose_name = "Contenido Home"
        verbose_name_plural = "Contenido Home"

class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='services/', verbose_name="Imagen")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ['order']
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name

class CateringPack(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    price_from = models.CharField(max_length=50, verbose_name="Precio desde")
    image = models.ImageField(upload_to='catering/', verbose_name="Imagen")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ['order']
        verbose_name = "Pack Catering"
        verbose_name_plural = "Packs Catering"

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Imagen")
    alt_text = models.CharField(max_length=200, verbose_name="Texto Alternativo")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        ordering = ['order']
        verbose_name = "Imagen Galería"
        verbose_name_plural = "Imágenes Galería"

    def __str__(self):
        return self.alt_text or f"Imagen {self.id}"
