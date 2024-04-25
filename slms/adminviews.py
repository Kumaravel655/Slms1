
from django.shortcuts import render,redirect,HttpResponse
from slmsapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from slmsapp.models import CustomUser,Staff,Staff_Leave
from django.db.models import Q

@login_required(login_url='/')
def HOME(request):
    current_user = request.user.username
    staff_count = Staff.objects.all().count()
    leave_count = Staff_Leave.objects.filter(leave_type=current_user).count()
    context ={
        'staff_count':staff_count,
        'leave_count':leave_count
    }
    return render(request,'admin/home.html',context)


def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        department = request.POST.get('department')
        parent_phone = request.POST.get('parent_phone')
        student_phone = request.POST.get('student_phone')
        FloorIncharge = request.POST.get('student_phone')
        timetable = request.FILES.get('timetable')


        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is already Exist')
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is already Exist')
            return redirect('add_staff')
        
        else:
            user = CustomUser(first_name = first_name,last_name = last_name,email = email, profile_pic = profile_pic, user_type = 2, username = username)
            user.set_password(password)
            user.save()
            staff = Staff(
                admin = user,
                address = address,
                Department = department,
                parent_phone =parent_phone,
                student_phone = student_phone,
                floor_incharge= FloorIncharge,
                TimeTable=timetable,
            )
            staff.save()
            messages.success(request,'Student details has beend added successfully')
            return redirect('add_staff')

    return render(request,'admin/add_staff.html')

def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context = {
        "staff":staff,
    }
    return render(request,'admin/view_staff.html',context)

def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)
    context = {
        "staff":staff,
    }
    return render(request,'admin/edit_staff.html',context)

def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        department = request.POST.get('department')
        parent_phone = request.POST.get('parent_phone')
        student_phone = request.POST.get('student_phone')
        floor_incharge = request.POST.get('FloorIncharge')
        
        user = CustomUser.objects.get(id = staff_id)
        user.username =username
        user.first_name =first_name
        user.last_name =last_name
        user.email =email

        if password != None and password !="":
            user.set_password(password)
        if profile_pic != None and profile_pic !="":
            user.profile_pic = profile_pic
        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.department = department
        staff.address = address
        staff.parent_phone= parent_phone
        staff.student_phone = student_phone
        staff.floor_incharge = floor_incharge
        staff.save()
        messages.success(request,'Student details has been succeesfully updated')
        return redirect('view_staff')
        
    return render(request,'admin/edit_staff.html')

def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,"Staff record has been deleted successfully.")
    return redirect('view_staff')


def STAFF_LEAVE_VIEW(request):
    current_user = request.user.username
    
    # Assuming there's a ForeignKey relationship between Staff_Leave and User for the floor in-charge
    staff_leave = Staff_Leave.objects.filter(leave_type=current_user)
    
    context = {
        "staff_leave": staff_leave,
    }
    
    return render(request,'admin/staff_leave.html',context)
def STAFF_PROOF_VIEW(request):
    # Assuming you have a User model for authentication and a Staff_Leave model for leave forms
    current_user = request.user.username
    
    # Assuming there's a ForeignKey relationship between Staff_Leave and User for the floor in-charge
    staff_leave = Staff_Leave.objects.filter(leave_type=current_user)
    
    context = {
        "staff_leave": staff_leave,
    }
    return render(request, 'admin/proofview.html', context)

    return render(request,'admin/proofview.html',context)
def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view_admin')

def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view_admin')



