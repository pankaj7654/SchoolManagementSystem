from django.views import View
from django.shortcuts import render , redirect
from multiuser.models.user import Student,Teacher , AddStudent ,AddTeacher


# Add new student enrollment

class NewAddStudent(View):
    def get(self , request):
        return render(request, 'enrollNewStudent.html')

    def post(self , request):
        studentId = request.POST.get('studentId')
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        gender = request.POST.get('gender')
        #studentobj = AddStudent.objects.get(studentId=studentId)
        try:
            if studentId:
                user = AddStudent(studentId=studentId,name=name,branch=branch,gender=gender)
                result = user.save()
                return render(request , 'teacherIndex.html', {'error' : "Successfully Enrollment From Orginization"})
            else:
                return render(request , 'enrollNewStudent.html', {'error' : "Failed Enrollment From Orginization"})
       
        except:
            return render(request , 'enrollNewStudent.html', {'error' : "Failed Enrollment From Orginization"})
            


# delete Enrolled student

class DeleteEnrolledStudent(View):
    def get(self , request):
        return render(request, 'delEnrollStudent.html')
        

    def post(self , request):
        studentId = request.POST.get('studentId')
        try:
            if studentId:
                studentobj = AddStudent.objects.get(studentId=studentId)
                result = studentobj.delete()
                return render(request , 'teacherIndex.html', {'error' : "Successfully Enrollment Deleted"})
            else:
                return render(request , 'delEnrollStudent.html', {'error' : "Please enter Valid Enrollment"})
        
        except:
            return render(request , 'delEnrollStudent.html', {'error' :  "Please enter Valid Enrollment"})

