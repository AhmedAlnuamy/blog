from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User 

from . models import Customer, Order

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"


class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        exclude  = ['user']

class CreateNewUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password1']