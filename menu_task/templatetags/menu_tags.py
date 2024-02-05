from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.get_queryset_descendants(
        MenuItem.objects.filter(menu_name=menu_name, parent=None),
        include_self=True
    )
    return {'menu_items': menu_items}
