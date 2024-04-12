from django.db import models
from user.models import User

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    product_img = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    data_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ №{self.id} "