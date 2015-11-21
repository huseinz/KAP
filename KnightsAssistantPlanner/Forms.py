__author__ = 'blazeaga'
from django.contrib.auth.models import User
from django import forms
from KnightsAssistantPlanner.models import UserProfile
class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=128)
    slug=forms.CharField(widget=forms.HiddenInput(),required=False)

class PageForm(forms.ModelForm):
    title= forms.CharField(max_length=128,help_text="Enter Title")
    url=forms.URLField(max_length=200, help_text="Enter URL")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=('username','email','password')

#class UserProfileForm(forms.ModelForm):
 #   class Meta:
  #      model=UserProfile
   #     fields=('')
