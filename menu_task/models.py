from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')
    url = models.CharField(max_length=200,
                           blank=True,
                           null=True)
    named_url = models.CharField(max_length=200,
                                 blank=True,
                                 null=True)
    menu_name = models.CharField(max_length=50,
                                 help_text='Идентификатор меню, например "main_menu"'
                                 )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name