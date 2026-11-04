from .models import SiteSettings, Brand

def site_settings(request):
    return {
        'site_settings': SiteSettings.objects.filter(pk=1).first(),
        'site_brands': Brand.objects.filter(
            is_active=True,
            image__isnull=False
        ).exclude(image='').order_by('display_order', 'id')
    }