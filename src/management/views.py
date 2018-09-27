from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import User

@login_required
def complete_profile(request):

	pass





"""

	username = models.CharField(max_length=20)
	password = models.CharField(max_length=15)
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=25)
	is_authorised = models.BooleanField()
	is_activated = models.BooleanField()
	designation = models.CharField(max_length=20)
	police_station = models.CharField(max_length=25)


"""