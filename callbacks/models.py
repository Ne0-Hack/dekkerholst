from django.db import models


class TelegramUsers(models.Model):
    name = models.CharField("Имя сотрудника", max_length=255)
    telegram = models.CharField("Telegram ID сотрудника", max_length=255,
                                help_text="Получить Telegram ID можно в чате с этим ботом: <a target=\"_blank\" href=\"https://t.me/getmyid_bot\">https://t.me/getmyid_bot</a>")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграм"


class Callback(models.Model):
    status_list = (
        ("0", "Заявка ожидает обработки"),
        ("1", "Заявка в процессе"),
        ("2", "Заявка обработана")
    )
    name = models.CharField("Имя пользователя", max_length=255)
    phone = models.CharField("Телефон", max_length=30)
    status = models.CharField("Статус", choices=status_list, max_length=255, default=0)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Заявка на обратную связь"
        verbose_name_plural = "Заявки на обратную связь"
