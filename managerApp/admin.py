from django.contrib import admin
from .models import Department, Staff, Attendance

class StaffAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'email', 'department')
    list_filter = ('department',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'dateLog', 'timeLog', 'isPresent')
    list_filter = ('dateLog', 'staff',)

# Register your models here.
admin.site.register(Staff, StaffAdmin)
admin.site.register(Department)
admin.site.register(Attendance, AttendanceAdmin)