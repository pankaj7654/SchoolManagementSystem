from django.urls import path
from multiuser.views import index
from multiuser.views import LoginView , SignupView , signup , login , newAddStudent
from multiuser.views.email_verification import verifyCode , sendOtp
from multiuser.views import reset_password
from multiuser.views.reset_password import ResetPassword , PasswordResetVerification , verifyResetPasswordCode , TeacherResetPassword,TeacherPasswordResetVerification,teacherVerifyResetPasswordCode


urlpatterns = [
    path('', index.index , name='index'),
    
    path('signup/', signup.SignupView.as_view() , name='signup'),
    path('studentSignup/', signup.S_SignupView.as_view() , name='S_SignupView'),
    path('teacherSignup/', signup.T_SignupView.as_view() , name='T_SignupView'),

    path('login/', login.LoginView.as_view() , name='login'),
    path('studentLogin/', login.StudentLoginView.as_view() , name='studentLogin'),
    path('teacherLogin/', login.TeacherLoginView.as_view() , name='teacherLogin'),

    path('logout/', index.logout , name='logout'),

    path('reset-password' , ResetPassword.as_view() , name = 'reset-password'),
    path('reset-password-verification' , PasswordResetVerification.as_view() , name = 'reset-password-verification'),
    path('verify-reset-password-code' , verifyResetPasswordCode , name='verify-reset-password-code'),

    path('teacher-reset-password' , reset_password.TeacherResetPassword.as_view() , name = 'teacher-reset-password'),
    path('teacher-reset-password-verification' , reset_password.TeacherPasswordResetVerification.as_view() , name = 'teacher-reset-password-verification'),
    path('teacher-verify-reset-password-code' , reset_password.teacherVerifyResetPasswordCode , name='teacher-verify-reset-password-code'),

    path('send-otp', sendOtp , name='sendotp'),
    path('verify', verifyCode , name='verify'),

    path('enrollNewStudent/', newAddStudent.NewAddStudent.as_view(), name='enrollNewStudent'),
    path('delEnrollStudent/', newAddStudent.DeleteEnrolledStudent.as_view(), name='delEnrollStudent'),

]
