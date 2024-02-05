from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None).prefetch_related('children')
    return {'menu_items': menu_items}
