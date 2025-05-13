from django import forms
from .models import *

class campform(forms.ModelForm):

    class Meta:
        model = camp
        fields = ['camp_id','camp_name','address','district','city','panchayat','contact']

class loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded-left'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control rounded-left'}))
    class Meta:
        model = login
        fields = ['email','password']
        
class Login2Form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control rounded-left'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded-left'}))



class publicform(forms.ModelForm):

    class Meta:
        model = public
        fields = ['name','address','district','city','state','contact']

class volunteerform(forms.ModelForm):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect()
    )
    class Meta:
        model = volunteer
        fields = ['name','gender','age','contact','district']
        widget={
            'gender':forms.RadioSelect(attrs={'id':'radiov'})
        }

class stationform(forms.ModelForm):

    class Meta:
        model = station
        fields = ['station_id','address_line1','address_line2','district','city','contact']

class camp_prof(forms.Form):

    class Meta:
        model = camp
        fields = ['camp_id','camp_name','address','district','city','panchayat','contact']

class login_email_form(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control rounded-left'}))
    class Meta:
        model = login
        fields = ['email']

class public_prof(forms.Form):
    class Meta:
        model = public
        fields = ['name','address','district','city','state','contact']

class station_prof(forms.Form):
    class Meta:
        model = station
        fields = ['station_id','address_line1','address_line2','district','city','contact','authentication']


class volunteer_prof(forms.Form):
    class Meta:
        model = volunteer
        fields = ['name','gender','age','contact']

class refugeeform(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    class Meta:
        model = refugee
        fields = ['name','age','gender','address','contact']

class needsform(forms.ModelForm):
    class Meta:
        model = needs
        fields = ['need','status']

class volunteerrequestform(forms.ModelForm):
        class Meta:
            model = VolunteerRequest
            fields = ['volunteer_no']

class dutyassignmentform(forms.ModelForm):
    class Meta:
        model = duty_assignment
        fields = ['duty']

class emergencycampform(forms.ModelForm):
    class Meta:
        model = emergency_camp
        fields = ['message']

class missingpersonform(forms.ModelForm):
    class Meta:
        model = missing_person
        fields = ['name','photo','contact','address','district','city','panchayat','missing_date','missing_place','other_details']

class missingvehicleform(forms.ModelForm):
    class Meta:
        model = missing_vehicle
        fields = ['vehicle_category','vehicle_type','company_name','vehicle_number','color','missing_date']

class fundform(forms.ModelForm):
    class Meta:
      model = fund  
      fields = ['name','address','district','city','panchayat','taluk','ward_no','building_no','photo','state','contact','in_camp','bank_name','account_Holder_name','account_number','IFSC_code']
      widgets = {
            'in_camp': forms.Select(choices=[('yes', 'Yes'), ('no', 'No')]),
        }

class paymentform(forms.ModelForm):
    class Meta:
        model = payment
        fields = ['name','card_no','month','year','cvv','amount']
        