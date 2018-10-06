from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import User, Criminal , Record
from .forms import UserForm,CriminalForm,RecordForm

@login_required
def complete_profile(request):

	# print(request.user)
	try:
		User.objects.get(user=request.user)
		return redirect(home)
	except:
		pass

	# try:
	form = UserForm(request.POST or None)

	if form.is_valid():

		name = form.cleaned_data['name']
		designation = form.cleaned_data['designation']
		police_station = form.cleaned_data['police_station']

		obj=form.save(commit=False)
		obj.user = request.user
		obj.save()

		# form=UserForm()
		return render(request , 'management/thankyou.html',{'name':request.user})

	return render(request , 'management/complete_profile.html',{'form':form})
            
            



@login_required
def home(request):
	query = request.GET.get('q',None)
	obj = []
	print(query)
	if query:
		obj = Criminal.objects.filter(first_name__icontains=query)
		print('********')
		print(obj)
	user = User.objects.get(user=request.user)
	print(user)
	print(user.is_authorised)
	return render(request,'management/home.html',{'obj':obj,'user':user})


# def update_criminal(request,id):
# 	# obj = Criminal.objects.get(id=id)
	
# 	form = CriminalForm(request.POST or None)
# 	if form.is_valid():

# 		print('************%%$%$%$%$%$%$%')

# 		first_name = form.cleaned_data['first_name']
# 		last_name = form.cleaned_data['last_name']
# 		aadhar_number = form.cleaned_data['aadhar_number']
# 		dob = form.cleaned_data['dob']
# 		email = form.cleaned_data['email']
# 		fathers_name = form.cleaned_data['fathers_name']
# 		mothers_name = form.cleaned_data['mothers_name']
# 		mobile_number = form.cleaned_data['mobile_number']
# 		nationality = form.cleaned_data['nationality']
# 		address = form.cleaned_data['address']
# 		no_of_family_member = form.cleaned_data['no_of_family_member']

# 		obj = Criminal.objects.filter(id=id).update('first_name'=first_name,'last_name'=last_name,'aadhar_number'=aadhar_number,'dob'=dob,'email'=email,'fathers_name'=fathers_name,'mothers_name'=mothers_name,'mobile_number'=mobile_number,'nationality'=nationality,'address'=address,'no_of_family_member'=no_of_family_member)
		

# 		# obj.save()
# 		# form = CriminalForm(obj)



# 		# pass
# 	# return HttpResponse(obj)
# 	return render(request , 'management/update-profile.html',{'form':form})


from django.views.generic import UpdateView


class update_criminal(UpdateView):
    model = Criminal
    template_name = 'management/update-profile.html'
    fields = ['first_name','last_name','aadhar_number','dob','email','fathers_name','mothers_name','mobile_number','nationality','address','no_of_family_member'
]
 
    def get_object(self, queryset=None):
        id = self.kwargs['id']
        return self.model.objects.get(id=id)
 
    def form_valid(self, form):
        form.save()
        # return HttpResponseRedirect(reverse('demos-models-dbcrud-list'))
        return redirect('/')
 




def profile_detail(request,id):
	criminal = Criminal.objects.get(id=id)
	# print(criminal)
	# print(criminal.first_name)
	ruser=request.user
	print('6472647236478')
	user=User.objects.get(user=ruser)
	# print("TTTTTTTTTTTTT")
	# print(user.is_authorised)



	return render(request,'management/detail-profile.html',{'criminal':criminal,'user':user})



def past_record(request,id):

	criminal = Criminal.objects.get(id=id)
	record = Record.objects.filter(criminal=criminal)
	print('*******')
	print(record)
	return render(request,'management/records.html',{'record':record})


def add_record(request,id):
	criminal=Criminal.objects.get(id=id)
	form = RecordForm(request.POST or None)
	# form.criminal=criminal.
	if form.is_valid():
		alloted_jail= form.cleaned_data['alloted_jail']
		crime= form.cleaned_data['crime']
		crime_date= form.cleaned_data['crime_date']
		police_act= form.cleaned_data['police_act']
		punishment= form.cleaned_data['punishment']
		obj=form.save(commit=False)

		obj.criminal=criminal
		obj.save()
		# pass
	
	# print()
	return render(request,'management/add-record.html',{'form':form})


