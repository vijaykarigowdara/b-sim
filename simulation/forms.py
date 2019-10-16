from django import forms
from .models import *

class SuccessFactorForm(forms.ModelForm):
    class Meta:
        model = SuccessFactor
        fields = ('name', 'unit','fy_0', 'fy_1', 'fy_2','fy_3','fy_combined')

class PerformanceIndicatorForm(forms.ModelForm):
    class Meta:
        model = PerformanceIndicator
        fields = ('name', 'unit', 'fy_0','fy_1', 'fy_2','fy_3','fy_combined')
        
