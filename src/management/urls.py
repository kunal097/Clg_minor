from django.urls import path
from django.shortcuts import reverse
from .views import complete_profile,home,update_criminal,profile_detail,past_record , add_record,profile,test,reg_criminal,image_search#,Reg_criminal



urlpatterns = [
    
    path('home/', home,name='home'),
    path('profile/', profile,name='profile'),
    path('update_profile/<id>', update_criminal.as_view(),name='update-profile'),
    path('detail/<id>',profile_detail,name='detail'),
    path('record/<id>',past_record,name='record'),
    path('addrec/<id>',add_record,name='add-record'),
    path('add-criminal',reg_criminal,name="add-criminal"),
    path('test/', test,name='test'),
    path('search/',image_search,name='filequery'),
    path('', complete_profile,name='complete-profile'),
    
]
