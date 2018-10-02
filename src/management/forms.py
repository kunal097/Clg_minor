from django.contrib.auth import authenticate , get_user_model
from django import forms
from django.contrib.auth.models import User
from .models import User, Criminal


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name',
                   'designation',
                   'police_station']




class CriminalForm(forms.ModelForm):

	class Meta:
		model = Criminal
		fields = "__all__"

