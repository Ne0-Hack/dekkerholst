from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Work(models.Model):
    image = models.ImageField(upload_to='works', verbose_name="загрузить изображение", blank=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="80" height="80" style="object-fit: contain" />'.format(self.image.url))
        return ""

    class Meta:
        verbose_name = "работу"
        verbose_name_plural = "работы"

    def __str__(self):
        return f"Работа {self.id}"
