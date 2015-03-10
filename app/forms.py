'''
Created on Mar 10, 2015

@author: nishant.nawarkhede
'''
from django import forms

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')