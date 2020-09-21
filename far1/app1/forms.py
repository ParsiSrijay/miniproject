from django import forms
from .models import *


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['Username','CropName','CropType','MinCost','Quantity','Quality']