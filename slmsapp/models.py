from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER ={
        (1,'admin'),
        (2,'staff')
    }
    user_type = models.CharField(choices=USER,max_length=50,default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    Department = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=20)  # Assuming parent phone number can contain characters
    student_phone = models.CharField(max_length=20) 
    floor_incharge = models.CharField(max_length=50)
    floor_incharge_phone = models.CharField(max_length=20)  
    TimeTable = models.ImageField(upload_to='media/timetable')
    room_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.username

class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default=0)
    proof = models.ImageField(upload_to='media/proof') # Assuming student phone number can contain characters 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Changed to auto_now=True for updated_at field
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name 

