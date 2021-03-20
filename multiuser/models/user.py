from django.db import models

class Student(models.Model):
    studentId = models.CharField(max_length=10 , unique = True)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100 )
    father = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)


# return user name in admin panel
    def __str__(self):
        return self.name


class Teacher(models.Model):
    #email = models.EmailField(max_length=100 , unique = True)  //basically we have to use "unique" email but i have one email so here comfilict occouring. i used for testing 
    email = models.EmailField(max_length=100 )
    name = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)


# return user name in admin panel
    def __str__(self):
        return self.name


class AddStudent(models.Model):
    studentId = models.CharField(max_length=10 , unique = True)
    name = models.CharField(max_length = 50)
    gender = models.CharField(max_length=100 )
    branch = models.CharField(max_length=100 )
    
    def __str__(self):
        return self.name
    

class AddTeacher(models.Model):
    #email = models.EmailField(max_length=100 , unique = True)  //basically we have to use "unique" email but i have one email so here comfilict occouring. i used for testing 
    email = models.EmailField(max_length=100 )
    name = models.CharField(max_length = 50)
    gender = models.CharField(max_length=100 )
    department = models.CharField(max_length=100 )

    def __str__(self):
        return self.name