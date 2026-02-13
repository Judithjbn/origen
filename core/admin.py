from django.contrib import admin
from .models import SiteConfig, HomeContent, Service, CateringPack, GalleryImage

# Configuración visual del Admin
admin.site.site_header = "Administración D'Origen"
admin.site.site_title = "Panel D'Origen"
admin.site.index_title = "Gestión Web"

class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SiteConfig)
class SiteConfigAdmin(SingletonAdmin):
    pass

@admin.register(HomeContent)
class HomeContentAdmin(SingletonAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

@admin.register(CateringPack)
class CateringPackAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_from', 'order')
    list_editable = ('order',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'order')
    list_editable = ('order',)
