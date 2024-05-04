from django.shortcuts import render,redirect,HttpResponse
from slmsapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from slmsapp.models import CustomUser,Staff,Staff_Leave
from django.db.models import Q
from datetime import date

import tablib
from django.shortcuts import render, get_object_or_404


@login_required(login_url='/')
def HOME(request):
    current_date = date.today()

    # Filter staff by the current user ID
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id
        
        # Filter staff leave history where to_date is in the future
        staff_leave_history = Staff_Leave.objects.filter(
            staff_id=staff_id,
            to_date__gte=current_date
        )

        context = {
            'staff_leave_history': staff_leave_history,
        }

     
    return render(request,'staff/home.html',context)



@login_required(login_url='/')   
def STAFF_APPLY_LEAVE(request):
    return render(request,'staff/apply_leave.html')

@login_required(login_url='/')   
def PROFILE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    
    return render(request,'staff/VIEW.html')


@login_required(login_url='/')   
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_type = request.POST.get('leave_type')
        proof = request.FILES.get('proof')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        message = request.POST.get('message') 
        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_Leave(
            staff_id = staff,
            leave_type = leave_type,
            proof= proof,
            from_date = from_date,
            to_date = to_date,
            message = message,
            
          )
        leave.save()
        messages.success(request,'Leave apply successfully')
        return redirect('staff_apply_leave')

@login_required(login_url='/')    


def STAFF_LEAVE_VIEW(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_Leave.objects.filter(staff_id = staff_id)
    
    context = {
            'staff_leave_history':staff_leave_history,
        }
    


    return render(request, 'staff/leave_history.html', context)
def PASS(request, id):
    # Retrieve the Staff_Leave object using the provided id
    staff_leave = get_object_or_404(Staff_Leave, id=id)
    
    context = {
        "staff_leave": staff_leave,
    }
    
    return render(request, 'admin/proofview.html', context)

