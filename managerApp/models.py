from django.db import models
from datetime import datetime
# Create your models here.

class Department(models.Model) :
    name = models.TextField(max_length=255, default="No Name")
    
    def __str__(self):
        return f"{self.name}({self.id})"


class Staff(models.Model) :
    code = models.TextField(max_length=10, default="0000000000")
    name = models.TextField(max_length=255, default="No Name")
    gender = models.BooleanField(default=True)
    age = models.IntegerField(default=20)
    email = models.EmailField(default="noname@no1.vn")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    def __str__(self):
        return f" {self.code} - {self.name}"

class AttendanceManager(models.Manager):
    def create_attendance(self, staff, isPresent):
        attendance_check = Attendance.objects.filter(staff=staff, dateLog=datetime.date(datetime.now())).first()
        if attendance_check:
            return attendance_check;
        else:
            attendance = self.create(staff=staff, isPresent=isPresent)
            return attendance

    def staff_attendance(self, staff, dateLog, timeLog, isPresent):
        attendance_check = Attendance.objects.filter(staff=staff, dateLog=datetime.date(datetime.now())).first()
        if attendance_check:
            attendance = self.update(isPresent=isPresent)
            return attendance
        else:
            attendance = self.create(staff=staff, dateLog=dateLog, timeLog=timeLog, isPresent=isPresent)
            return attendance


class Attendance(models.Model) :
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    dateLog = models.DateField(default=datetime.now, blank=True)
    timeLog = models.TimeField(default=datetime.now, blank=True)
    isPresent = models.BooleanField(default=False)

    objects = AttendanceManager()
    