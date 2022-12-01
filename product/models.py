from django.db import models

# Size cart
class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'

#  Color cart article
class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'

# products
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="image/")
    size = models.ManyToManyField(Size,blank=True,null=True, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")

    def __str__(self):
        return f'{self.title}'


class Information(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="information")
    text = models.TextField()

    def __str__(self):
        return self.text[:20]