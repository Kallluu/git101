from django.db import models

# Create your models here.
class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=50)
    status = models.IntegerField(default=0)

class camp(models.Model):
    camp_id = models.CharField(max_length=50)
    camp_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    panchayat = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)


class public(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)

class volunteer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=10)
    district = models.CharField(max_length=50)
    login_id = models.OneToOneField('login',on_delete=models.CASCADE,related_name='volunteer')
    

class station(models.Model):
    station_id = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)

class refugee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    login_id = models.ForeignKey('login',on_delete=models.CASCADE)

class needs(models.Model):
    need = models.CharField(max_length=100)
    camp_id = models.ForeignKey('camp',on_delete=models.CASCADE)
    current_date = models.DateField(auto_now_add=True)
    status = models.TextField(blank=True,null=True)
    
class VolunteerRequest(models.Model):
    volunteer_no = models.IntegerField()
    current_date =  models.DateField(auto_now_add=True)
    camp_id = models.ForeignKey('camp',on_delete=models.CASCADE)  
    
   
class volunteer_allot(models.Model):
    request_id = models.ForeignKey('VolunteerRequest',on_delete=models.CASCADE)
    current_date = models.DateField(auto_now_add=True)
    volunteer_id = models.ForeignKey('volunteer', on_delete=models.CASCADE, null=True, blank=True)
    
class duty_assignment(models.Model):
    volunteer_id = models.ForeignKey('Volunteer',on_delete=models.CASCADE)
    camp_id = models.ForeignKey('camp',on_delete=models.CASCADE)
    duty = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    current_date = models.DateField(auto_now_add=True)


class emergency_camp(models.Model):
    message = models.TextField()
    current_date = models.DateField(auto_now_add=True)
    
class missing_person(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='emergency_photos/', blank=True, null=True)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    panchayat = models.CharField(max_length=50)
    missing_date = models.DateField()
    missing_place = models.CharField(max_length=100)
    other_details = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    public_id = models.ForeignKey('public',on_delete=models.CASCADE)
    
class missing_vehicle(models.Model):
    vehicle_category = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    missing_date = models.DateField()
    current_date = models.DateField(auto_now_add=True)
    public_id = models.ForeignKey('public',on_delete=models.CASCADE)
    station_id = models.ForeignKey('station',on_delete=models.CASCADE)

class fund(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    panchayat = models.CharField(max_length=100)
    taluk =  models.CharField(max_length=50)
    ward_no = models.CharField(max_length=50)
    building_no = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='house_photos/', blank=True, null=True)
    state = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    in_camp = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')],default='no')
    status = models.IntegerField(default=0)
    public_id = models.ForeignKey('public',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # bank details 
    bank_name = models.CharField(max_length=100,blank=True,null=True)
    account_Holder_name = models.CharField(max_length=100,blank=True,null=True)
    account_number = models.CharField(max_length=20,blank=True,null=True)
    IFSC_code = models.CharField(max_length=11,blank=True,null=True)
    payment_status = models.IntegerField(default=0)

class assign_fund(models.Model):
    camp_id = models.ForeignKey('camp',on_delete=models.CASCADE)
    fund_id = models.ForeignKey('fund',on_delete=models.CASCADE)
    current_date = models.DateField(auto_now_add=True)
    approve_status = models.IntegerField(default=0)
    admin_status = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.fund_id.name} assigned to {self.camp_id}"
    
class payment(models.Model):
    name = models.CharField(max_length=100)
    card_no = models.CharField(max_length=20)
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    amount = models.IntegerField(default=0)
    current_date = models.DateTimeField(auto_now_add=True)

class emergency_station(models.Model):
    message = models.TextField()
    current_date = models.DateField(auto_now_add=True) 