from django.db import models


class SiteSettings(models.Model):
    org_ogrnip = models.CharField("ОГРНИП", max_length=255)
    org_inn = models.CharField("ИНН", max_length=255)
    org_ip = models.CharField("ИП", max_length=255)
    org_address = models.CharField("Адрес", max_length=255)

    con_vk = models.CharField("ВКонтакте", max_length=255, null=True, blank=True)
    con_instagram = models.CharField("Instagram", max_length=255, null=True, blank=True)
    con_whatsapp = models.CharField("WhatsApp", max_length=255, null=True, blank=True)
    con_telegram = models.CharField("Telegram", max_length=255, null=True, blank=True)
    con_phone = models.CharField("Телефон", max_length=255, null=True, blank=True, help_text="+70000000000")
    con_email = models.CharField("E-Mail", max_length=255, help_text="STUDIAARTHOLST@gmail.com")

    site_price = models.BooleanField("Калькулятор на сайте", default=False,
                                     help_text="Калькулятор рассчёта цены при заказе")
    site_telegram = models.TextField("Токен Telegram бота", help_text="Для отправки уведомлений сотрудникам")

    class Meta:
        verbose_name = "настройка"
        verbose_name_plural = "настройки"

    def __str__(self):
        return f"Настройка сайта"
