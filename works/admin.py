from django.contrib import admin
from .models import Work


class WorkAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True


admin.site.register(Work, WorkAdmin)
