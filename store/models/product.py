from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    descpriction = models.TextField()
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default = 1)

    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)