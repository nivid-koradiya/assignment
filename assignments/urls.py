
from hashlib import new
from django.urls import path
from assignments.views import view_task,new_task
urlpatterns =[
    path('task/all/', view_task),
    path('task/new/', new_task),

]