from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    phone= models.IntegerField()
    email = models.EmailField(unique=True)
    message= models.TextField()

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title= models.CharField(max_length=200)
    image= models.ImageField(upload_to='category_images',null=True)

    def __str__(self):
        return self.title
    

class Momo(models.Model):
    name= models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="items")
    desc= models.TextField()
    image= models.ImageField(upload_to='Momo')
    price= models.DecimalField(max_digits=8,decimal_places=2)
    is_available= models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class EmailVerfication(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token= models.CharField(max_length=6)
    is_created=models.DateTimeField(auto_now_add=True)


class Testemonials(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('regular', 'Regular Customer'),
        ('new', 'New Customer'),
        ('vip', 'VIP Customer'),
    ]

    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE_CHOICES)
    visit_count = models.PositiveIntegerField(default=1)
    review = models.TextField()
    is_most_helpful = models.BooleanField(default=False)
    visited_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

