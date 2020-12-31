from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=True,
                            blank=False, verbose_name="Name")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    Description = models.TextField(
        null=True, blank=True, verbose_name="Description")

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Image(models.Model):
    Image = models.ImageField(
        upload_to='images', null=False, blank=False, verbose_name='Images')
    name = models.CharField(max_length=200, null=False, blank=False)
    product = models.ForeignKey(Product, models.CASCADE, verbose_name='Prduct')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.name
