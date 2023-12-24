from django import template
from WWW.models import SiteSettings

register = template.Library()


@register.simple_tag()
def load_site_info():
    return SiteSettings.objects.first()
