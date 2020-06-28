from django.contrib import admin
from .models import HelloCustomer


class HelloCustomerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "dob"]


# Register your models here.
admin.site.register(HelloCustomer, HelloCustomerAdmin)
