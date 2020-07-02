from django.contrib import admin
from .models import HelloCustomer
from import_export.admin import ImportExportModelAdmin

# ImportExportModelAdmin, should be used first to avoid MRO.
class HelloCustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # display as list
    list_display = ["full_name", "email", "phone", "dob", "gender"]
    # makes the dob and full_name field clickable.
    # default is always the first member in the list.
    list_display_links = ["dob"]
    # Full_Name is editable.
    list_editable = ["full_name"]
    # The number of element in one page to be displayed.
    list_per_page = 10
    # Adds DOB and PINCODE as a filter option.
    list_filter = ["dob", "pincode"]
    # Sort based on full_name and then email.
    # - indicates reverse order.
    ordering = ["-full_name", "email"]
    # search fields to search for.
    search_fields = ["full_name", "phone", "email"]
    # fieldsets, how the form has to be organized.
    # collapse, meaning collapsing.
    fieldsets = (
        (None, {"fields": ("full_name", "email", "phone", "gender")}),
        ("More", {"classes": ("collapse",), "fields": ("dob", "address", "pincode")}),
    )


# Register your models here.
admin.site.register(HelloCustomer, HelloCustomerAdmin)
