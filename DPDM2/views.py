
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from datetime import date 
from django.http import JsonResponse
from django.utils import timezone 

# Create your views here.


def index(request):
    return render(request,'usercontent.html')


def admin_index(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')

    emergency_messages = emergency_camp.objects.all().order_by('-current_date')
    return render(request,'admin_home.html',{'emergency_messages': emergency_messages})


def camp_entry(request):
    log_id = request.session.get('campid')
    if  not log_id:
        return redirect('login')

    # persons = missing_person.objects.all()

    # missing_persons = missing_person.objects.filter().exclude(status=1)
    # print(missing_persons)  

    # return render(request, 'camp_home.html', {'missing_persons': missing_persons})
    missing_persons = missing_person.objects.exclude(status=1)

    # Get emergency station requests (you can add filters if needed, e.g., only active ones)
    emergency_requests = emergency_station.objects.all().order_by('-id')  # Or apply relevant filters

    return render(request, 'camp_home.html', {
        'missing_persons': missing_persons,
        'emergency_requests': emergency_requests
    })

def public_entry(request):
    log_id = request.session.get('publicid')
    if  not log_id:
        return redirect('login')
    return render(request,'public_home.html')

def volunteer_entry(request):
    log_id = request.session.get('volunteerid')
    if  not log_id:
        return redirect('login')
    return render(request,'volunteer_home.html')

def station_entry(request):
    log_id = request.session.get('stationid')
    if  not log_id:
        return redirect('login')
    return render(request,'station_home.html')

def login_index(request):
    if request.method == 'POST':
        form = Login2Form(request.POST)
        # print("dataaaaa",form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = login.objects.get(email = email)
                if user.password == password:
                    if user.usertype == "camp" and user.status == 1:
                        request.session['campid'] = user.id
                        return redirect('camppage')
                    elif user.usertype == "public":
                        request.session['publicid'] = user.id
                        return redirect('publicpage')
                    elif user.usertype == "volunteer" and user.status == 1:
                        request.session['volunteerid'] = user.id
                        return redirect('volunteerpage')
                    elif user.usertype == "station" and user.status == 1:
                        request.session['stationid'] = user.id
                        return redirect('stationpage')
                    elif user.usertype == "admin":
                        request.session['adminid'] = user.id
                        return redirect('admin_path')
                else:
                    messages.error(request,'invalid password')
            except login.DoesNotExist:
                messages.error(request,'User does not exist')
    else:
        form = Login2Form()
    return render(request,'userlogin/login_index.html',{'log':form})

def campreg(request):
    if request.method == 'POST':
        form = campform(request.POST)
        login = loginform(request.POST)
        if form.is_valid() and login.is_valid():
            a=login.save(commit=False)
            a.usertype='camp'
            a.save()
            b=form.save(commit=False)
            b.login_id=a
            b.save()
        messages.success(request, 'User data saved successfully.')
        return redirect('index')
    else:
        form = campform()
        login = loginform()
        return render(request,'campregister.html',{'form':form,'log':login})

def publicreg(request):
    if request.method == 'POST':
        pub = publicform(request.POST)
        login = loginform(request.POST)
        if pub.is_valid() and login.is_valid():
            c=login.save(commit=False)
            c.usertype='public'
            c.status=1
            c.save()
            d=pub.save(commit=False)
            d.login_id=c
            d.save()
        messages.success(request,'User data saved successfully.')
        return redirect('index')
    else:
        pub = publicform()
        login = loginform()
        return render(request,'publicregister.html',{'public_form':pub,'log':login})
    
def volunteerreg(request):
    if request.method == 'POST':
        vol = volunteerform(request.POST)
        login = loginform(request.POST)
        if vol.is_valid() and login.is_valid():
            c=login.save(commit=False)
            c.usertype='volunteer'
            c.save()
            d=vol.save(commit=False)
            d.login_id=c
            d.save()
        messages.success(request,'User data saved successfully.')
        return redirect('index')
    else:
        vol = volunteerform()
        login = loginform()
        return render(request,'volunteerregister.html',{'vol_form':vol,'log':login})
    

def stationreg(request):
    if request.method == 'POST':
        stat = stationform(request.POST)
        login = loginform(request.POST)
        if stat.is_valid() and login.is_valid():
            c=login.save(commit=False)
            c.usertype='station'
            c.save()
            d=stat.save(commit=False)
            d.login_id=c
            d.save()
        messages.success(request,'User data saved successfully.')
        return redirect('index')
    else:
        stat = stationform()
        login = loginform()
        return render(request,'stationregister.html',{'stationf':stat,'log':login})
    
def camp_pro(request):
    log_id = request.session.get('campid')
    if  not log_id:
        return redirect('login')
    log = get_object_or_404(login,id = log_id)
    pro =get_object_or_404(camp,login_id = log)
    if request.method == 'POST':
        form = campform(request.POST,instance=pro)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('camp_profile_path')
    else:
        form = campform(instance=pro)
        emailform = login_email_form(instance=log)
    return render(request,'camp_profile.html',{'camp_p':form,'emailf':emailform})

def public_pro(request):
    log_id = request.session.get('publicid')
    if  not log_id:
        return redirect('login')
    log = get_object_or_404(login,id = log_id)
    pro_p = get_object_or_404(public,login_id = log)
    if request.method == 'POST':
        form = publicform(request.POST,instance=pro_p)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('public_profile_path')
    else:
        form = publicform(instance=pro_p)
        emailform = login_email_form(instance=log)
    return render(request,'public_profile.html',{'public_p':form,'emailf':emailform})

def station_pro(request):
    log_id = request.session.get('stationid')
    if  not log_id:
        return redirect('login')
    log = get_object_or_404(login,id = log_id)
    pro_s = get_object_or_404(station,login_id = log)
    if request.method == 'POST':
        form = stationform(request.POST,instance=pro_s)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('station_profile_path')
    else:
        form = stationform(instance=pro_s)
        emailform = login_email_form(instance=log)
    return render(request,'station_profile.html',{'station_p':form,'emailf':emailform})

def volunteer_pro(request):
    log_id = request.session.get('volunteerid')
    if  not log_id:
        return redirect('login')
    log = get_object_or_404(login,id = log_id)
    pro_v = get_object_or_404(volunteer,login_id = log)
    if request.method == 'POST':
        form = volunteerform(request.POST,instance=pro_v)
        emailform = login_email_form(request.POST,instance=log)
        if form.is_valid() and emailform.is_valid():
            form.save()
            emailform.save()
            return redirect('volunteer_profile_path')
    else:
        form = volunteerform(instance=pro_v)
        emailform = login_email_form(instance=log)
    return render(request,'volunteer_profile.html',{'volunteer_p':form,'emailf':emailform})


def camp_tab(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    users = camp.objects.all()
    return render(request,'camp_table.html',{'users': users})

def public_tab(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    users = public.objects.all()
    return render(request,'public_table.html',{'users': users})

def volunteer_tab(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    users = volunteer.objects.all()
    return render(request,'volunteer_table.html',{'users':users})
    

def station_tab(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    users = station.objects.all()
    return render(request,'station_table.html',{'users':users})
    
def camp_approve(request,id):
    users = get_object_or_404(login,id=id)
    users.status=1
    users.save()
    return redirect('camp_table_path')

def camp_reject(request,id):
    users = get_object_or_404(login,id=id)
    users.status=2
    users.save()
    return redirect('camp_table_path')

def station_approve(request,id):
    users = get_object_or_404(login,id=id)
    users.status=1
    users.save()
    return redirect('station_table_path')

def station_reject(request,id):
    users = get_object_or_404(login,id=id)
    users.status=2
    users.save()
    return redirect('station_table_path')

def volunteer_approve(request,id):
    users = get_object_or_404(login,id=id)
    users.status=1
    users.save()
    return redirect('volunteer_table_path')

def volunteer_reject(request,id):
    users = get_object_or_404(login,id=id)
    users.status=2
    users.save()
    return redirect('volunteer_table_path')

def add_refugee(request):
    ref_id = request.session.get('campid')
    if not ref_id:
        return redirect('login')
    log = get_object_or_404(login,id = ref_id)
    if request.method == 'POST':
        form = refugeeform(request.POST)
        if form.is_valid():
            r = form.save(commit=False)
            r.login_id = log
            r.save()
        return redirect('view_refugee')
    else:
        form = refugeeform()
        return render(request,'add_refugee.html',{'ref':form})

def view_refugee(request):
    log_id = request.session.get('campid')
    if  not log_id:
        return redirect('login')
    users = refugee.objects.all()
    return render(request,'view_refugee.html',{'users':users})

def delete_refugee(request,id):
    user = get_object_or_404(refugee,id=id)
    user.delete()
    return redirect('view_refugee')

def edit_refugee(request,id):
    log_id = request.session.get('campid')
    if  not log_id:
        return redirect('login')
    user = get_object_or_404(refugee,id=id)
    if request.method == 'POST':
        form = refugeeform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_refugee')
    else:
        form = refugeeform(instance=user)
        return render(request,'edit_refugee.html',{'form':form})
    
def view_refugee_public(request):
    log_id = request.session.get('publicid')
    if  not log_id:
        return redirect('login')
    query = refugee.objects.all()  # Show all data initially

    if request.method == 'POST':
        ser = request.POST.get('search', '').strip()  # Get search term, remove spaces
        if ser:
            query = refugee.objects.filter(
                Q(name__icontains=ser) |
                Q(age__icontains=ser) |
                Q(gender__icontains=ser) |
                Q(address__icontains=ser) |
                Q(contact__icontains=ser)
            )

    return render(request, 'view_refugee_public.html', {'users': query})

def needs_camp(request):
    camp_id = request.session.get('campid')
    if  not camp_id:
        return redirect('login')
    log = get_object_or_404(camp,login_id = camp_id)
    if request.method == 'POST':
        form = needsform(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.camp_id = log
            a.save()
            return redirect('needs_camp')
    else:
        form = needsform()
    return render(request,'needs_camp.html',{'form':form})

def manage_needs(request):
    camps = request.session.get('campid')
    if not camps:
        return redirect('login')
    camp_id = get_object_or_404(camp,login_id = camps)
    users = needs.objects.filter(camp_id = camp_id)
    return render(request,'manage_needs.html',{'users':users,'camps':camp})

def edit_needs(request,id):
    log_id = request.session.get('campid')
    if  not log_id:
        return redirect('login')
    user = get_object_or_404(needs,id=id)
    if request.method == 'POST':
        form = needsform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_needs')
    else:
        form = needsform(instance=user)
        return render(request,'edit_needs.html',{'form':form})

def delete_needs(request,id):
    user = get_object_or_404(needs,id=id)
    user.delete()
    return redirect('manage_needs')

def admin_needs(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    camps = needs.objects.all()
    return render(request, 'admin_needs.html', {'camps': camps})

def update_needs_status(request, id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    need = get_object_or_404(needs, id=id)  # Fetch the need object
    if request.method == 'POST':
        status = request.POST.get('status')
        if status:
            need.status = status
            need.save()
            return redirect('admin_needs')
    return render(request,'update_needs_status.html',{'need':need}) 

def volunteer_request_camp(request):
    camp_id = request.session.get('campid')  # Get camp ID from session
    if not camp_id:
        return redirect('login')
    log = get_object_or_404(camp, login_id=camp_id)  # Get camp object

    if request.method == 'POST':
        form = volunteerrequestform(request.POST)  # Correct form name
        if form.is_valid():
            volunteer_request = form.save(commit=False)  # Don't save yet
            volunteer_request.camp_id = log  # Assign camp ID
            volunteer_request.save()  # Now save it
            return redirect('volunteer_request')  # Redirect after saving
    else:
        form = volunteerrequestform()
    return render(request, 'volunteer_request_camp.html', {'form': form})


def admin_volunteer_request(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    admins = VolunteerRequest.objects.all()  # Get all volunteer requests
    return render(request, 'admin_volunteer_request.html', {'admins': admins})



def allot_volunteers(request, id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    users = get_object_or_404(VolunteerRequest, id=id)

    vol = login.objects.filter(status=1, usertype='volunteer').select_related('volunteer')

    # Get the search query
    query = request.GET.get('search')

    if query:
        # Filter volunteers based on the `district` field in the `volunteer` model
        vol = vol.filter(Q(volunteer__district__icontains=query))

    # Fetch the specific volunteer request

    return render(request, 'allot_volunteers.html', {'volunteers': vol, 'request_id': users})

def allot_now(request,vid,rid):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    a = get_object_or_404(VolunteerRequest,id=rid)
    b = get_object_or_404(volunteer,login_id=vid)

    if volunteer_allot.objects.filter(volunteer_id=b,request_id=a).exists():
        messages.success(request,'Already Alloted.')
        return redirect('allot_volunteers',id=rid)


    else:
        volunteer_allot.objects.create(request_id=a,volunteer_id=b)
        messages.success(request,'Successfully assigned!')
        return redirect('allot_volunteers',id=rid)



def volunteer_camp(request):
    camp_id = request.session.get('campid')
    if  not camp_id:
        return redirect('login')
    camps = get_object_or_404(camp,login_id=camp_id)
    req = volunteer_allot.objects.filter(request_id__camp_id=camps)
    return render(request, 'volunteer_camp.html', {'requests': req })

def duty_camp(request, id):
    camps = request.session.get('campid')
    if not camps:
        return redirect('login')

    campid = get_object_or_404(camp, login_id=camps)
    vol_id = get_object_or_404(volunteer, id=id)

    try:
        # Check if a duty already exists for the volunteer with status 1
        assignment = duty_assignment.objects.filter(volunteer_id=vol_id).first()

        if request.method == "POST":
            form = dutyassignmentform(request.POST)
            if form.is_valid():
                new_duty = form.cleaned_data['duty']

                if assignment:
                    if assignment.status == 1:
                        # Update existing duty and set status to 0
                        assignment.duty = new_duty
                        assignment.status = 0
                        assignment.save()
                        messages.success(request, "Duty updated successfully!")
                    elif assignment.status == 0:
                        messages.error(request, "Previous duty not yet completed!")
                        return redirect('volunteer_camp')
                else:
                    # No existing assignment — create new
                    duty_assignment.objects.create(
                        volunteer_id=vol_id,
                        duty=new_duty,
                        status=0,
                        camp_id=campid
                    )
                    messages.success(request, "New duty assignment created successfully!")

                return redirect('volunteer_camp')
            else:
                messages.error(request, "Invalid form data.")

        return render(request, 'duty_camp.html', {
            'form': dutyassignmentform(),
            'assignment': assignment
        })

    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('volunteer_camp')


def duty_volunteer(request):
    volunteer_id = request.session.get('volunteerid')
    if  not volunteer_id:
        return redirect('login')
    log = get_object_or_404(volunteer,login_id=volunteer_id)
    duties = duty_assignment.objects.filter(volunteer_id=log)
    return render(request,'duty_volunteer.html',{'duties':duties})

def duty_complete(request,id):
    duty = get_object_or_404(duty_assignment,id=id)
    duty.status=1
    duty.save()
    messages.success(request, "Duty marked as completed successfully!")
    return redirect('duty_volunteer')  

def emergency_request_camp(request):
    log_id = request.session.get('campid')
    if  not log_id:
        return redirect('login')
    if request.method == 'POST':
        alert = request.POST.get('alert')
        emergency_camp.objects.create(
            message = alert
        )
    return render(request, 'emergency_request_camp.html')

def missing_person_details(request):
    public_id = request.session.get('publicid')
    if  not public_id:
        return redirect('login')
    log = get_object_or_404(public,login_id=public_id)
    if request.method == 'POST':
        form = missingpersonform(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.public_id = log
            p.save()
            return redirect('missing_person_details')  
    else:
        form = missingpersonform()
    
    return render(request, 'missing_person_details.html', {'form': form})

def found_person(request,id):
    person = get_object_or_404(missing_person,id=id)
    person.status=1
    person.save()
    return redirect('camppage')

def not_found_person(request,id):
    person = get_object_or_404(missing_person,id=id)
    person.status=2
    person.save()
    return redirect('camppage')

def registered_station(request):
    stations = station.objects.all() 
    if request.method == 'POST':
            ser = request.POST.get('search', '').strip()  
            if ser:
                stations = station.objects.filter(
                Q(district__icontains=ser) 
                
            )

    return render(request, 'registered_station.html', {'stations': stations})

def find_vehicle(request,id):
    public_id = request.session.get('publicid')
    log = get_object_or_404(public,login_id=public_id)
    s_log = get_object_or_404(station,id=id)
    if request.method == 'POST':
        stat = missingvehicleform(request.POST)
        if stat.is_valid():
            data = stat.save(commit=False)
            data.station_id = s_log
            data.public_id = log
            data.save()
            return redirect('find_vehicle',id=id)
    else:
        stat = missingvehicleform()
    return render(request,'find_vehicle.html',{'stat':stat})

def missing_vehicle_details(request):
    station_id = request.session.get('stationid')
    if  not station_id:
        return redirect('login')
    log = get_object_or_404(station,login_id=station_id)
    vehicles = missing_vehicle.objects.filter(station_id=log)
    return render(request,'missing_vehicle_details.html',{'vehicles':vehicles})

def missing_person_station(request):
    station_id = request.session.get('stationid')
    if  not station_id:
        return redirect('login')
    persons = missing_person.objects.filter(status=2)
    return render(request,'missing_person_station.html',{'persons':persons})

def missing_person_public(request):
    public_id = request.session.get('publicid')
    if  not public_id:
        return redirect('login')
    log = get_object_or_404(public,login_id = public_id)
    persons = missing_person.objects.filter(public_id=log)
    return render(request,'missing_person_public.html',{'persons':persons})
   
def edit_missing_person(request,id):
    person = get_object_or_404(missing_person,id=id)
    if request.method == 'POST':
        form = missingpersonform(request.POST,request.FILES,instance=person)
        if form.is_valid():
            form.save()
            return redirect('missing_person_public')
    else:
        form = missingpersonform(instance=person)
    return render(request,'edit_missing_person.html',{'form': form})

def delete_missing_person(request,id):
    person = get_object_or_404(missing_person,id=id)
    person.delete()
    return redirect('missing_person_public')

def mark_as_found(request,id):
    person = get_object_or_404(missing_person, id=id)
    
    # Update status to "Found"
    person.status = 1  # Assuming "1" means "Found"
    person.save()
    
    messages.success(request, f'{person.name} has been marked as Found.')
    return redirect('missing_person_station')  # Redirect to station's missing persons page

def fund_allocation(request):
    f=request.session.get('publicid')
    if  not f:
        return redirect('login')
    c=get_object_or_404(public,login_id=f)
    if request.method == 'POST':
        funds = fundform(request.POST,request.FILES)
        print(funds)
        if funds.is_valid():
            d=funds.save(commit=False)
            d.public_id=c
            d.save()
            messages.success(request,'User data saved successfully.')
            return redirect('fund_allocation')
    else:
        funds = fundform()
       
    return render(request,'fund_allocation.html',{'form':funds})
    
def fund_allocation_public(request):
    

    public_id = request.session.get('publicid')
    if  not public_id:
        return redirect('login')
    log = get_object_or_404(public, login_id=public_id)
    funds = fund.objects.filter(public_id=log)

    fund_data = []

    for f in funds:
        assign = assign_fund.objects.filter(fund_id=f).first()  # Get related assignment if it exists
        admin_status = assign.admin_status if assign else 0     # Default to 0 if not assigned
        fund_data.append({
            'fund': f,
            'admin_status': admin_status,
            'assign_id': assign.id if assign else None,             # Optional if needed in template
            'payment_status': f.payment_status,                     # Add payment status
            'amount': f.amount if f.payment_status == 1 else 0       # Show amount only if paid
        })

    return render(request, 'fund_allocation_public.html', {'fund_data': fund_data})

def edit_fund_public(request,id):
    log_id = request.session.get('publicid')
    if  not log_id:
        return redirect('login')
    users = get_object_or_404(fund,id=id)
    if request.method == 'POST':
        form = fundform(request.POST,request.FILES,instance=users)
        if form.is_valid():
            form.save()
            return redirect('fund_allocation_public')
    else:
        form = fundform(instance=users)
    return render(request,'edit_fund_public.html',{'form':form})

def delete_fund_public(request,id):
    users = get_object_or_404(fund,id=id)
    users.delete()
    return redirect('fund_allocation_public')



def fund_allocation_admin(request):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    funds = fund.objects.all()
    fund_data = []

    for f in funds:
        assign = assign_fund.objects.filter(fund_id=f).first()  # get related assignment if it exists
        admin_status = assign.admin_status if assign else 0  # default to 0 if not assigned
        fund_data.append({
            'fund': f,
            'admin_status': admin_status,
            'assign_id': assign.id if assign else None  # needed for approving/rejecting
        })

    return render(request, 'fund_allocation_admin.html', {'fund_data': fund_data})


def assign_camp(request,id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
   
    funds = get_object_or_404(fund, id=id)

    if request.method == 'POST':
        camp_id = request.POST.get('camp_id')
        selected_camp = get_object_or_404(camp, id=camp_id)

        # Assign the selected camp to the fund and update status
        funds.camp_id = selected_camp
        funds.status = 1  # 1 = Assigned to camp
        funds.save()

        # Redirect to a camp approval page
        return redirect('camp_list_admin', fund_id=funds.id, camp_id=selected_camp.id)

    all_camps = camp.objects.all()
    return render(request, 'camp_list_admin.html', {'camps': all_camps,'funds':funds, 'fund_id': funds})

def assign_the_camp(request,camp_id,fund_id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    camps = get_object_or_404(camp,id=camp_id)
    funds = get_object_or_404(fund,id=fund_id)
    assign_fund.objects.create(
        camp_id=camps,
        fund_id=funds,
        current_date=timezone.now().date()
    )

    # Optionally update the fund status (e.g., assigned = 1)
    funds.status = 1
    funds.save()

    return redirect('fund_allocation_admin') 


def fund_allocation_camp(request):
    camps = request.session.get('campid')
    if  not camps:
        return redirect('login')
    log = get_object_or_404(camp,login_id=camps)
    items = assign_fund.objects.filter(camp_id=log)
    return render(request,'fund_allocation_camp.html',{'items':items})


def approve_fund_by_camp(request,assign_id):
    assigned = get_object_or_404(assign_fund, id=assign_id)
    assigned.approve_status = 1
    assigned.save()
    return redirect('fund_allocation_camp')

def reject_fund_by_camp(request,assign_id):
    assigned = get_object_or_404(assign_fund,id=assign_id)
    assigned.approve_status=2
    assigned.save()
    return redirect('fund_allocation_camp')

def view_assigned_camp(request,fund_id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    assigned = get_object_or_404(assign_fund, fund_id=fund_id)
    camps = assigned.camp_id
    return render(request, 'view_assigned_camp.html', {'camps': camps,'assigned': assigned })

def approve_fund_by_admin(request,id):
    assign = get_object_or_404(assign_fund, id=id)
    assign.admin_status = 1  
    assign.save()
    return redirect('fund_allocation_admin')

def reject_fund_by_admin(request,id):
    assign = get_object_or_404(assign_fund,id=id)
    assign.admin_status = 2  
    assign.save()
    return redirect('fund_allocation_admin') 

def amount_transfer(request,id,fund_id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    funds = get_object_or_404(fund,id=id)

    if request.method == 'POST':
        new_value = request.POST.get("amount")

        if new_value is not None and new_value != funds.amount:
            funds.amount = new_value
            funds.save()
            amt = funds.amount

            return redirect('paymentindex',amt,funds.id)
    return render(request,'amount_transfer.html',{'funds':funds})

def paymentindex(request,amt,fund_id):
    log_id = request.session.get('adminid')
    if  not log_id:
        return redirect('login')
    if request.method == "POST":
        name = request.POST.get('name')
        card_number = request.POST.get('card_no')
        month = request.POST.get('month')
        year = request.POST.get('year')
        cvv = request.POST.get('cvv')

        payment.objects.create(
            name=name,
            card_no=card_number,
            month=month,
            year=year,
            cvv=cvv,
            amount=amt,
        
        )

        fund_obj = fund.objects.get(id=fund_id)
        fund_obj.payment_status = 1
        fund_obj.save()

        messages.success(request,'Payment successful.')
        return redirect('fund_allocation_admin')
        
    return render(request, 'paymentindex.html', {'amt': amt,'fund_id':fund_id})

def emergency_request_station(request):
    log_id = request.session.get('stationid')
    if  not log_id:
        return redirect('login')
    if request.method == 'POST':
        alert = request.POST.get('alert')
        emergency_station.objects.create(
            message=alert
        )

    # Fetch all alerts (e.g., latest first)
    
    return render(request, 'emergency_request_station.html')

def volunteer_camp_list(request):
    log_id = request.session.get('volunteerid')
    if  not log_id:
        return redirect('login')
    camps = camp.objects.all()
    return render(request, 'volunteer_camp_list.html', {'camps': camps})

def logout_view(request):
    # Clear all possible session keys
    keys_to_clear = ['adminid', 'campid', 'publicid', 'volunteerid', 'stationid']
    for key in keys_to_clear:
        request.session.pop(key, None)

    messages.success(request, "You have been logged out successfully.")
    return redirect('index')  # Replace with your login page's name

import requests

API_KEY = "7c8f76a84fb1b06e3990c51bedf0a2fa"


def get_weather(request):
    
    latitude = request.GET.get("lat", None)
    longitude = request.GET.get("lon", None)

    if not latitude or not longitude:
        return render(request, "weather.html", {"error": "Location not provided!"})

    URL = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        prediction = predict_disaster(data)
        context = {
            "latitude": latitude,
            "longitude": longitude,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather_condition": data["weather"][0]["description"],
            "prediction": prediction
        }
    else:
        context = {"error": "Could not fetch weather data"}

    return render(request, "weather.html", context)

def predict_disaster(data):
    """Predict disaster risk based on weather data"""
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_condition = data["weather"][0]["main"]

    if weather_condition in ["Thunderstorm", "Tornado"]:
        return "⚠️ High Risk of Storm"
    elif weather_condition == "Rain" and humidity > 80:
        return "⚠️ Flood Risk Due to Heavy Rain"
    elif temp > 40 and humidity < 30:
        return "🔥 Extreme Heat Warning"
    else:
        return "✅ No Disaster Risk Detected"



