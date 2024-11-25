from django import forms  
from homepage.models import homepage
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = homepage 
        fields = "__all__" 