from django.contrib import admin
from .models import Company, Medicine, MedicineForm, MedicineType

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicineType)
admin.site.register(MedicineForm)




