from django.contrib import admin
from patient.models import HeartVital, Appointment

# Register your models here.

# (To display Admin only read purpose, so that value can't be modified )
# class HeartVitalAdmin(admin.ModelAdmin):
#       readonly_fields = ('user',)
# admin.site.register(HeartVital,HeartVitalAdmin)


class AppontmentAdmin(admin.ModelAdmin):
      list_display = ('user', 'mobile', 'date', 'note', 'status')
      search_fields = ('user', 'mobile')
      list_filter = ('status', 'date' )
      list_editable = ('status',)
      ordering = ('-date',)
      list_per_page = 25

admin.site.register(Appointment, AppontmentAdmin)
admin.site.register(HeartVital)
