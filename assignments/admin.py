from django.contrib import admin


from assignments.models import *
# Register your models here.

#this is our model/table that we need to see on the admin panel.
admin.site.register(assignments)