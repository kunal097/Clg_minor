from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import User, Criminal
from .forms import UserForm

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


def update_criminal(request,id):
	obj = Criminal.objects.get(id=id)
	# return HttpResponse(obj)