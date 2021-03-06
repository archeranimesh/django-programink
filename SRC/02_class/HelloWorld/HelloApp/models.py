from django.db import models

# Create your models here.
class HelloCustomer(models.Model):
    full_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    address = models.TextField(blank=True)
    pincode = models.IntegerField(default=0)
    dob = models.DateField(verbose_name="Date of Birth")
    # The below drop down menu option was added,
    # once added we have to run migrate and makemigration.
    gender = models.CharField(
        max_length=30, choices=(("Male", "Male"), ("Female", "Female")), default="Male"
    )

    def __str__(self):  # string representation of object
        return self.full_name
