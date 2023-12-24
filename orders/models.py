from django.db import models
from django.utils.html import mark_safe


class Order(models.Model):
    status_list = (
        ("0", "Ожидает обработки"),
        ("1", "В обработке"),
        ("2", "В работе"),
        ("3", "Готов")
    )
    status = models.CharField("Статус заказа", choices=status_list, max_length=255, default=0)
    product = models.ManyToManyField("ProductionOrder")
    client_name = models.CharField("Имя клиента", max_length=255)
    client_phone = models.CharField("Телефон клиента", max_length=255, blank=True, help_text="Необязательное поле")
    description = models.TextField("Примечания для сотрудников", blank=True, help_text="Необязательное поле")

    def __str__(self):
        return f"заказ №{self.id}"

    @property
    def get_products(self):
        products = self.product.all()
        html = ""
        for item in products:
            url = ""
            if item.upload:
                url = item.upload.url
            html += (f'<div class="products-item">'
                     f'<span><img src="{url}" /></span>'
                     f'<span>Вопрос: <b>{item.category}</b></span>'
                     f'<span>Ответ: <b>{item.title}</b></span>'
                     f'<span>Цена: <b>{item.price}</b></span>'
                     f'</div>')

        html = (f'<div class="products">{html}</div>'
                f'<style>'
                '.products {display: flex; gap: 50px; flex-direction: column} '
                '.products-item {display: flex; gap: 10px; flex-direction: column}'
                f'</style>')
        return mark_safe(html)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"


class CategoryOrder(models.Model):
    title = models.CharField("Название", max_length=120, help_text="Например: размер")
    coefficient = models.IntegerField("Коэфициент", max_length=10, help_text="Например: один m2 равен 10")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class ProductionOrder(models.Model):
    category = models.ForeignKey("CategoryOrder", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=120, help_text="Например: 60x60")
    price = models.IntegerField('Цена', help_text="Например: 1000", null=True)
    upload = models.ImageField(upload_to='orders/', verbose_name="загрузить изображение", blank=True)

    @property
    def thumbnail_preview(self):
        if self.upload:
            return mark_safe(
                '<img src="{}" width="80" height="80" style="object-fit: contain" />'.format(self.upload.url))
        return ""

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "продукцию"
        verbose_name_plural = "продукция"
