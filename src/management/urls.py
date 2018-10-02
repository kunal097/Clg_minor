from django.urls import path
from .views import complete_profile,home,update_criminal


urlpatterns = [
    
    path('home/', home,name='home'),
    path('update_profile/<id>', update_criminal,name='update-profile'),
    path('', complete_profile,name='complete-profile'),
    
]
