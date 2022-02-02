from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Counselor,User_normal

class CounselarSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super( UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username","password1", "password2"]:
            self.fields[fieldname].help_text = None
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        counselor = Counselor.objects.create(user=user)
        counselor.phone_number=self.cleaned_data.get('phone_number')
        counselor.save()
        return user

class NormalUserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        normal = User_normal.objects.create(user=user)
        normal.phone_number=self.cleaned_data.get('phone_number')
        normal.save()
        return user