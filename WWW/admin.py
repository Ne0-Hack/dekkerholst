from django.contrib import admin
from .models import SiteSettings


class SettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Настройки сайта", {
            "fields": [
                "site_price",
                "site_telegram",
            ]
        }),
        ("Настройки организации", {
            "fields": [
                "org_ogrnip",
                "org_inn",
                "org_ip",
                "org_address",

            ]
        }),
        ("Настройки контактов", {
            "fields": [
                "con_vk",
                "con_instagram",
                "con_whatsapp",
                "con_telegram",
                "con_phone",
                "con_email",
            ]
        }),
    ]


admin.site.register(SiteSettings, SettingsAdmin)
