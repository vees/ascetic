from veesnet.ascetic.models import *
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
   filter_horizontal = ['related','tags','owners']

admin.site.register(Picture)
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
admin.site.register(ConsumerItem, ItemAdmin)
admin.site.register(MediaItem)
admin.site.register(Group)

