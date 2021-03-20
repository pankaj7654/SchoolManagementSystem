from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password , make_password
from multiuser.models import Student,Teacher



class LoginView(View):
    def get(self , request):
        return_url = None
        print("From Class Based View")
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html')




class StudentLoginView(View):
    def get(self , request):
        return_url = None
        print("From Class Based View")
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'studentLogin.html')


    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            user = Student.objects.get(email = email)
            print(user)
            flag = check_password(password = password , encoded = user.password)
            if flag:
                #print(flag,"MMMMMMMMMMMMMMM")
                #print(user.__dict__)
                temp = {}
                temp['email'] = user.email
                temp['studentId'] = user.studentId
                request.session['user'] = temp
                return render(request,'studentIndex.html')
            else:
                return render(request,'studentLogin.html' , {'error' : 'Email or Password Invalid'})
        except:
            return render(request,'studentLogin.html' , {'error' : 'Email or Password Invalid'}) #redirect index from url name

        


class TeacherLoginView(View):
    def get(self , request):
        return_url = None
        print("From Class Based View")
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'teacherLogin.html')


    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            user = Teacher.objects.get(email = email)
            print(user)
            flag = check_password(password = password , encoded = user.password)
            if flag:
                #print(flag,"MMMMMMMMMMMMMMM")
                #print(user.__dict__)
                temp = {}
                temp['email'] = user.email
                temp['id'] = user.id
                request.session['user'] = temp
                return render(request,'teacherIndex.html')
            else:
                return render(request,'teacherLogin.html' , {'error' : 'Email or Password Invalid'})
                
        except:
            return render(request,'teacherLogin.html' , {'error' : 'Email or Password Invalid'}) #redirect index from url name
