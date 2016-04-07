from django import template

from slider.models import Slide

register = template.Library()

@register.inclusion_tag('_flexslider.html')
def flexslider():
    return {'slides': Slide.objects.filter(is_active=True),}
