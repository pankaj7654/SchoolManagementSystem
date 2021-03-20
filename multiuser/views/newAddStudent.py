from django.views import View
from django.shortcuts import render , redirect
from multiuser.models.user import Student,Teacher , AddStudent ,AddTeacher



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
                return render(request , 'enrollNewStudent.html', {'error' : "Successfully Enrollment From Orginization"})
            else:
                return render(request , 'teacherIndex.html', {'error' : "Failed Enrollment From Orginization"})
       
        except:
            return render(request , 'teacherIndex.html', {'error' : "Failed Enrollment From Orginization"})
            

class DeleteEnrolledStudent(View):
    def get(self , request):
        return render(request, 'delEnrollStudent.html')


    def post(self , request):
        studentId = request.POST.get('studentId')
        try:
            if studentId:
                user = AddStudent(studentId=studentId)
                print(user,"KKKKKKKKKKKKKKKKKKKKKKKK")
                result = user.all().delete()
                print("EEEEEEEEEEEEEEEEEEEEEEEEE")
                return render(request , 'delEnrollStudent.html', {'error' : "Successfully Enrollment Deleted"})
            else:
                return render(request , 'teacherIndex.html', {'error' : "Failed Enrollment Deletion"})
        
        except:
            return render(request , 'teacherIndex.html', {'error' : "Failed Enrollment Deletion"})

