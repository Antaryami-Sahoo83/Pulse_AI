from django.contrib import admin
from patient.models import HeartVital

# Register your models here.

# (To display Admin only read purpose, so that value can't be modified )
# class HeartVitalAdmin(admin.ModelAdmin):
#       readonly_fields = ('user',)
# admin.site.register(HeartVital,HeartVitalAdmin)

admin.site.register(HeartVital)
