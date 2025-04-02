from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
         

class Products(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    price = models.IntegerField(default=0)  
    stock = models.IntegerField(default=0)  
    image = models.ImageField(upload_to='products/')
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name





