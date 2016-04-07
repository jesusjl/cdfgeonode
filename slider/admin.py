from django.contrib import admin
from slider.models import Slide

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'sort_order')
    list_editable = ('is_active','sort_order',)

admin.site.register(Slide, SlideAdmin)
