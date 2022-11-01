from django import forms
from resumeapp.models import Resume
from resumeapp.models import AppUser
GENDER_CHOICE=[
    ('male','male'),
    ('female','female')
]

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=AppUser
        fields=('first_name','middle_name','last_name','email','contact','password')

class UserLoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=AppUser
        fields=('email', 'password')

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    class Meta:
        model=Resume
        fields=['name','dob','gender','city','pin','province','mobile','email','job_city','profile_image','my_file']    
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your full name'}),
            'dob':forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your living city'}),
            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your city pin'}),
            'province':forms.Select(attrs={'class':'form-control','placeholder':'Enter your province'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'job_city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your preferred job cities'}),
         }