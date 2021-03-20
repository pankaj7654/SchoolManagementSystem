from django.contrib import admin
from django.utils.html import format_html
from multiuser.models import Student , Teacher ,AddStudent,AddTeacher
# Register your models here.


class StudentUserModel(admin.ModelAdmin):
    list_display = ['studentId','name','email','phone','father','branch','address','gender']
    sortable_by = ['studentId' , 'name']
   
def get_user(self , obj):
        return format_html(f'<a target="_blank" href="/admin/multiuser/user/{obj.user.id}">{obj.user}</a>')



class TeacherUserModel(admin.ModelAdmin):
    list_display = ['name','email','phone','department','gender']
    sortable_by = ['id' , 'name']
    

def get_user(self , obj):
        return format_html(f'<a target="_blank" href="/admin/multiuser/user/{obj.user.id}">{obj.user}</a>')



class AddStudentModel(admin.ModelAdmin):
    list_display = ['studentId','name','gender','branch']
    

class AddTeacherModel(admin.ModelAdmin):
    list_display = ['email','name','gender','department']




admin.site.register(Student , StudentUserModel)
admin.site.register(Teacher , TeacherUserModel)
admin.site.register(AddStudent , AddStudentModel)
admin.site.register(AddTeacher , AddTeacherModel)