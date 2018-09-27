from django.urls import path
from .views import complete_profile


urlpatterns = [
    path('', complete_profile,name='complete-profile'),
]
