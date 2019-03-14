from django import forms
from .models import Image , Profile , User
from pyuploadcare.dj.forms import ImageField

class ImageForm(forms.ModelForm):  
    class Meta:
        model = Image
        fields = ("image","name","caption")

class ProfileForm(forms.Form):
    bio = forms.CharField(label = "Bio")
    pic = ImageField(label = "Pic")