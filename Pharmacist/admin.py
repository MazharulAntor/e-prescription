from django.contrib import admin
from .models import Pharmacist, Order, MedicineStock, SoldMedicine

# Register your models here.

admin.site.register(Pharmacist)
admin.site.register(Order)
admin.site.register(MedicineStock)
admin.site.register(SoldMedicine)