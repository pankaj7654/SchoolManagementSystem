from django.views import View
from django.shortcuts import HttpResponse ,render , redirect
from django.contrib.auth.hashers import check_password , make_password
from multiuser.models import Student,Teacher
from multiuser.utils.email_sender import sendEmail
import math
import random


def sendOtp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    otp = math.floor(random.random() * 10000000)

    html = f'''
        <h3>OTP Varification</h3>
        <hr>
        <h4>Hello {name}</h4>
        <br>
        <p>Your Varification Code is <b>{otp}</b></p>
        <br>
        <p>If did not required varification code, you can ignore this email</p>
    '''

    
    if name and email:
        response = sendEmail(name=name , message='' , email=email , htmlContent=html , subject ="User Verification Request")
        try:
            if(response.json()['messageId']):
                request.session['verification-code'] = otp
                return HttpResponse("{'message' : 'success'}" , status = 200)
                
            else:
                return HttpResponse(status = 400)
        except:
            return HttpResponse(status = 400)



def verifyCode(request):
    code = request.POST.get('code')
    otp = request.session.get('verification-code')
    print(code , otp)
    if(str(otp) == code):
        return HttpResponse("{'message' : 'success'}" , status = 200)

    else:
        return HttpResponse(status = 400)

