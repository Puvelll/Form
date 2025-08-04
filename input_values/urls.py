from os import name
from django.urls import path
from input_values.views import index, sobre, submit_form

urlpatterns = [
    path('', index, name='home'),
    path('sobre', sobre, name='sobre'),
    path('submit-form', submit_form)

]
