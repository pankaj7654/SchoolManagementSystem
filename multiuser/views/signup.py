from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password , check_password
from multiuser.models.user import Student,Teacher , AddStudent ,AddTeacher


class SignupView(View):
    def get(self , request):
        return render(request, 'signup.html')



class S_SignupView(View):
    def get(self , request):
        return render(request, 'S_Signup.html')

    def post(self , request):
        studentId = request.POST.get('studentId')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        father = request.POST.get('father')
        branch = request.POST.get('branch')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        password = request.POST.get('password')           #Hashing password
        hashedPassword = make_password(password = password)
        if studentId:
            try:
                studentobj = AddStudent.objects.get(studentId=studentId)
                if studentobj.studentId==studentId:
                    user = Student(studentId=studentId,name=name,email=email,password=hashedPassword,phone = phone,father=father,branch=branch,gender=gender,address=address)
                    result = user.save()
                    return render(request , 'studentLogin.html')
                else:
                    return render(request , 'S_Signup.html' ,{'error' : "this enrollment is not associated with this organigation"})   
        
            except:
                studentId = None
                return render(request , 'S_Signup.html' ,{'error' : "this enrollment is not associated with this organigation"})   
            
            



class T_SignupView(View):
    def get(self , request):
        return render(request, 'T_Signup.html')

    def post(self , request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        gender = request.POST.get('gender')
        password = request.POST.get('password')           #Hashing password
        hashedPassword = make_password(password = password)
        if email:
            try:
                teacherobj = AddTeacher.objects.get(email=email)
                if teacherobj.email==email:
                    user = Teacher(name=name,email=email,password=hashedPassword,phone = phone,department=department,gender=gender)
                    result = user.save()
                    return render(request , 'teacherLogin.html')
                else:
                    return render(request , 'T_Signup.html' ,{'error' : "this enrollment is not associated with this organigation"})   
            
            except:
                teacherId = None
                return render(request , 'T_Signup.html' ,{'error' : "this enrollment is not associated with this organigation"})  
