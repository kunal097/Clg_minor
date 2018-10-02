from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.


class User(models.Model):
	user = models.ForeignKey(AuthUser,on_delete=models.CASCADE)
	# username = models.CharField(max_length=20)
	# password = models.CharField(max_length=15)
	name = models.CharField(max_length=20)
	# email = models.CharField(max_length=25)
	is_authorised = models.BooleanField(default=False)
	is_activated = models.BooleanField(default=False)
	designation = models.CharField(max_length=20)
	police_station = models.CharField(max_length=25)


	def __str__(self):
		return self.name


	




class Criminal(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	aadhar_number = models.CharField(max_length=12)
	dob = models.DateTimeField()
	email=models.CharField(max_length=25)
	fathers_name = models.CharField(max_length=30)
	mothers_name = models.CharField(max_length=30)
	mobile_number = models.CharField(max_length=12)
	nationality = models.CharField(max_length=15)
	address = models.CharField(max_length=50)
	no_of_family_member = models.IntegerField()


	def __str__(self):
		return self.first_name+' '+self.last_name




class Record(models.Model):
	criminal = models.ForeignKey(Criminal,on_delete=models.CASCADE)
	alloted_jail = models.CharField(max_length=20)
	crime = models.CharField(max_length=20)
	crime_date = models.DateTimeField()
	police_act = models.CharField(max_length=25)
	punishment = models.CharField(max_length=30)

	def __str__(self):
		return str(self.criminal)+'('+self.crime + ')'
