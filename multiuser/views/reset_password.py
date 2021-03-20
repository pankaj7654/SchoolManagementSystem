from django.views import View
from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from multiuser.models import Student,Teacher
from multiuser.utils.email_sender import sendEmail
import math
import random


# Reset Password For Student 
# set new password

class ResetPassword(View):
    def get(self , request):
        return render(request , 'reset-password.html' , {'step1' : True})


    def post(self , request):
        pass
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None
        if len(password) < 6:
            error = 'Password must be more than 6 char long'

        elif len(repassword) < 6:
            error = 'Password must be more than 6 char long'

        elif password != repassword:
            error = 'Password miss matched'

        if error:
            return render(request, 'reset-password.html' , {'step3' : True , 'error' : error})
        else:
            email = request.session.get('reset-password-email')
            user = Student.objects.get(email = email)
            user.password = make_password(password)
            user.save()
            request.session.clear()
            sendEmailAfterChangePassword(user)
            return render(request , 'studentLogin.html' , {'message' : 'Password Changed...'})


# Chnge sucessfully reset password mail
def sendEmailAfterChangePassword(user):
    html = "<h1>Password Changed Successfully....</h1>"
    sendEmail(user.name , user.email , message='Password Changed' , htmlContent=html , subject='Password Changed Successfully')


# code verify reset password code

def verifyResetPasswordCode(request):
    code =  request.POST.get('code')
    sessioncode = request.session['reset-password-verification-code']
    if code == str(sessioncode):
        return render(request, 'reset-password.html' , {'step3' : True})
    else:
        return render(request, 'reset-password.html' , {'step2' : True})

# change password

class PasswordResetVerification(View):
    def post(self , request):
        print(request.POST.get('email'))
        email = request.POST.get('email')
        try:
            user = Student.objects.get(email = email)
            print(user)
            otp = math.floor(random.random() * 10000000)

            html = f'''

            <h4>Your Password Reset Verification Code is {otp}

            '''

            sendEmail(name = "Student" , email=email  , subject = 'Reset Password Verification Code' , message= "Password Reset Verification Code" , htmlContent=html)
            request.session['reset-password-verification-code'] = otp
            request.session['reset-password-email'] = email
            return render(request, 'reset-password.html' , {'step2' : True})

        except:
            return redirect('/reset-password') # we can redirect from url as wel as name of url









# Reset password For Teacher

class TeacherResetPassword(View):
    def get(self , request):
        return render(request , 'teacher-reset-password.html' , {'step1' : True})


    def post(self , request):
        pass
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None
        if len(password) < 6:
            error = 'Password must be more than 6 char long'

        elif len(repassword) < 6:
            error = 'Password must be more than 6 char long'

        elif password != repassword:
            error = 'Password miss matched'

        if error:
            return render(request, 'reset-password.html' , {'step3' : True , 'error' : error})
        else:
            email = request.session.get('reset-password-email')
            user = Teacher.objects.get(email = email)
            user.password = make_password(password)
            user.save()
            request.session.clear()
            sendEmailAfterChangePassword(user)
            return render(request , 'teacherLogin.html' , {'message' : 'Password Changed...'})



def sendEmailAfterChangePassword(user):
    html = "<h1>Password Changed Successfully....</h1>"
    sendEmail(user.name , user.email , message='Password Changed' , htmlContent=html , subject='Password Changed Successfully')



# code verify reset password code

def teacherVerifyResetPasswordCode(request):
    code =  request.POST.get('code')
    sessioncode = request.session['reset-password-verification-code']
    print(code,sessioncode)
    if code == str(sessioncode):
        return render(request, 'teacher-reset-password.html' , {'step3' : True})
    else:
        return render(request, 'teacher-reset-password.html' , {'step2' : True})


# change password

class TeacherPasswordResetVerification(View):
    def post(self , request):
        print(request.POST.get('email'))
        email = request.POST.get('email')
        try:
            user = Teacher.objects.get(email = email)
            print(user)
            otp = math.floor(random.random() * 10000000)

            html = f'''

            <h4>Your Password Reset Verification Code is {otp}

            '''

            sendEmail(name = "Teacher" , email=email  , subject = 'Reset Password Verification Code' , message= "Password Reset Verification Code" , htmlContent=html)
            request.session['reset-password-verification-code'] = otp
            request.session['reset-password-email'] = email
            return render(request, 'teacher-reset-password.html' , {'step2' : True})

        except:
            return redirect('/teacher-reset-password') # we can redirect from url as wel as name of url
