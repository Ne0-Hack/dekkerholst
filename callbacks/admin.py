from django.contrib import admin
from .models import TelegramUsers, Callback
from .views import send_to_telegram


# Register your models here.
class TelegramAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'telegram'),
            'description': "Чтобы сотруднику начали приходить уведомления на указанный ID аккаунта, необходимо нажать "
                           "кнопку \"Старт\" в чате с ботом <br> "
                           ""
        }),
    )


class CallbackAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'status')

    def callback_status(self, obj):
        return obj.status

    callback_status.admin_order_field = 'status'


admin.site.register(TelegramUsers, TelegramAdmin)
admin.site.register(Callback, CallbackAdmin)
