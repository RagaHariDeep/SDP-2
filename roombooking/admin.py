from django.contrib import admin

# Register your models here.
from .models import registrationmodel,bookroommodel

admin.site.register(registrationmodel)
admin.site.register(bookroommodel)