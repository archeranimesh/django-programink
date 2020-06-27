from django.db import models

# Create your models here.
class HelloCustomer(models.Model):
    full_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(blank=True)
    pincode = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.full_name, self.phone, self.email
