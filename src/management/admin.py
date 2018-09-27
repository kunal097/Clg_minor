from django.contrib import admin
from .models import User , Criminal , Record

# Register your models here.

admin.site.register(User)
admin.site.register(Criminal)
admin.site.register(Record)