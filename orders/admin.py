from django.contrib import admin
from .models import Order, CategoryOrder, ProductionOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status',)
    readonly_fields = ('get_products',)
    fieldsets = [
        ("", {
            'fields': [
                "status"
            ]
        }),
        ("Заказчик", {
            'fields': [
                ("client_name", "client_phone"),
                "description"
            ]
        }),
        ("Ответы на вопросы", {
            'fields': [
                "get_products"
            ],
            'classes': ('collapse', 'closed'),
        })
    ]

    def order_status(self, obj):
        return obj.status

    order_status.admin_order_field = 'status'

    def get_products(self, obj):
        return obj.get_products

    get_products.short_description = ''


class ProductionInline(admin.TabularInline):
    model = ProductionOrder
    extra = 0
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductionInline,
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(CategoryOrder, CategoryAdmin)
