from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, request


# Create your views here.
def register(request):
        if request.method == "POST":
            a = request.POST['name']
            b = request.POST['phone']
            c = request.POST['email']
            d = request.POST['password']
            e = request.POST['tiffin']
            f = request.POST['start_date']
            g = request.POST['end_date']
            new_customer = Register(name=a, phone_no=b, email_id=c, password=d, tiffin=e, start_date=f, end_date=g)
            new_customer.save()
            # customer_id = new_customer.custmer_id
            # print(customer_id)
            user = User.objects.create_user(username=a, password=d, first_name=a)
            main_customer = Main_Register(user=user, name=a, phone_no=b, email_id=c, password=d, tiffin=e, start_date=f,
                                         end_date=g)
            main_customer.save()
            return HttpResponse("Data saved successfully")
        return render(request,'register.html')




def elogin(request):
    error = ""
    # fullname = ""
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u, p)
        user = authenticate(username=u, password=p)
        print(user)

        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
                print("not usre login")
        except:
            error = "yes"
            print("nothing")
    return render(request, 'employeelogin.html', locals())


def dashbord(request):
    return render(request,'dashbord.html',)


#
# from django.db import IntegrityError
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
#
# from datetime import datetime, timedelta, timezone
# from django.utils import timezone
#
#
# # from .models import MainCustomer, yesnodata
#
# def Coupens(request):
#     if not request.user.is_authenticated:
#         return redirect('user_login')
#     a=request.user.id
#     # print(a)
#     user = User.objects.get(id=request.user.id)
#     # print(user)
#     empl = Main_Register.objects.get(user=user)
#     print(empl)
#     # //////////to get value//////////
#     r = yesno.objects.filter(empl=empl,Data='yes')
#     s = Main_Register.objects.filter(user=user)
#     print(s)
#
#     yes_count=r.count()
#     print(yes_count)
#     totaldays=36
#     remainingdays=totaldays-yes_count
#     print(remainingdays)
#
#     total_coupens=30
#     remaining_coupens=total_coupens-yes_count
#     print(remaining_coupens)
#
#
#     error = ""
#
#     info = None
#     last_entry = yesno.objects.last()
#     current_time = timezone.now()
#     print(current_time)
#     disable_until = last_entry.timestamp + timedelta(seconds=200)
#     if request.method == "POST":
#         i = request.POST['yesno']
#         enable_submit = timezone.now() >= disable_until
#         print(enable_submit)
#         try:
#             yesno.objects.create(empl=empl, Data=i)
#
#             error = "no"
#         except IntegrityError:
#             error = "yes"
#         return HttpResponse('data save')
#     return render(request,'coupens.html',{'remainingdays':remainingdays,'error': error,'remaining_coupens':remaining_coupens,'s':s})



from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.utils import timezone

# from .models import Main_Register, yesno

def Coupens(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    user = User.objects.get(id=request.user.id)
    empl = Main_Register.objects.get(user=user)

    r = yesno.objects.filter(empl=empl, Data='yes')
    s = Main_Register.objects.filter(user=user)

    yes_count = r.count()
    totaldays = 36
    remainingdays = totaldays - yes_count

    total_coupens = 30
    remaining_coupens = total_coupens - yes_count

    error = ""

    last_entry = yesno.objects.last()
    current_time = timezone.now()

    if last_entry is not None:
        disable_until = last_entry.timestamp + timedelta(seconds=10)
    else:
        disable_until = timezone.now()

    if request.method == "POST":
        i = request.POST['yesno']
        enable_submit = timezone.now() >= disable_until
        if enable_submit:
            try:
                yesno.objects.create(empl=empl, Data=i)
                error = "no"
            except IntegrityError:
                error = "yes"
        else:
            error = "no"
        return HttpResponse('data save')

    return render(request, 'coupens.html', {
        'remainingdays': remainingdays,
        'error': error,
        'remaining_coupens': remaining_coupens,
        's': s,
        'last_entry':last_entry,
        'disable_until':disable_until,
        'current_time':current_time,
    })




from django.db.models import OuterRef, Subquery

def filtered_data(request):
    latest_timestamp_subquery = yesno.objects.filter(empl=OuterRef('empl')).order_by('-timestamp').values('timestamp')[:1]
    latest_entries = yesno.objects.filter(timestamp__in=Subquery(latest_timestamp_subquery))
    return render(request, 'filtered_data.html', {'data': latest_entries})
