from datetime import datetime
from django.http import JsonResponse
from managerApp.models import Staff, Attendance
from .serializers import StaffSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def staffs(request):
    # GET::
    # get all Staffs in DB.
    if request.method == 'GET':
        staffs = Staff.objects.all()
        serializers = StaffSerializer(staffs, many=True)
        return JsonResponse(data=serializers.data, safe=False)
    
    # POST::
    # to check staff is have in exist in DB.
    # if yes, return an info of Staff and attendance to DB.
    # if no, return an empty info.
    elif request.method == 'POST':
        serializers = StaffSerializer(data=request.data)
        if serializers.is_valid():
            code = serializers.data['code']
            staff = Staff.objects.filter(code=code).first()
            if staff:
                now = datetime.now()
                attendance = Attendance.objects.staff_attendance(staff, datetime.date(now), datetime.time(now), True)
                
                serializer = StaffSerializer(staff)
                return JsonResponse(data=serializer.data, safe=False)
            else:
                serializer = StaffSerializer()
                return JsonResponse(data=serializer.data, safe=False)
                
        return Response(status=status.HTTP_400_BAD_REQUEST)