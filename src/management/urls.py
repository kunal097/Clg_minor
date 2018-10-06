from django.urls import path
from .views import complete_profile,home,update_criminal,profile_detail,past_record , add_record



urlpatterns = [
    
    path('home/', home,name='home'),
    path('update_profile/<id>', update_criminal.as_view(),name='update-profile'),
    path('detail/<id>',profile_detail,name='detail'),
    path('record/<id>',past_record,name='record'),
    path('addrec/<id>',add_record,name='add-record'),
    path('', complete_profile,name='complete-profile'),
    
]
