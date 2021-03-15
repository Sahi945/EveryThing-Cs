from django.contrib import admin
#importing model which we created in home/models
#which is Contact
from home.models import Contact

# Register your models here.

admin.site.register(Contact)
