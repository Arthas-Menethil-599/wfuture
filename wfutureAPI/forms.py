from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models.skill import Skill

from .models.review import Review

from .models.city import City
from .models.country import Country

from .models.volunteership import Volunteership

from .models.location import Location
from .models.volunteer import Volunteer
from .models.company import Company

class VolunteerSignupForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    sex = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('prefer_not_to_say', 'Prefer not to say')], required=False)
    birthday = forms.DateField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    phone_number = forms.CharField(max_length=15)
    avatar = forms.ImageField(required=False)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CompanySignupForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    description = forms.CharField(widget=forms.Textarea, required=False)
    mission = forms.CharField(widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.all())
    address = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_content']


class ApplicationStatusForm(forms.Form):
    application_id = forms.IntegerField(widget=forms.HiddenInput())
    status = forms.ChoiceField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

class VolunteerStatusForm(forms.Form):
    volunteer_volunteership_id = forms.IntegerField(widget=forms.HiddenInput())
    status = forms.ChoiceField(choices=[('active', 'Active'), ('expelled', 'Expelled'), ('finished', 'Finished')])

class VolunteershipForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    address = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Volunteership
        fields = [
            'title', 'picture', 'description', 'mission_statement', 
            'skills', 'causes', 'company', 'start_date', 'end_date', 'points'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'mission_statement': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'company': forms.HiddenInput(),
        }
