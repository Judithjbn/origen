from .models import SiteConfig

def site_config(request):
    try:
        return {'site_config': SiteConfig.load()}
    except Exception:
        return {'site_config': None}
