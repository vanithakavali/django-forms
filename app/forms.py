
from django import forms

def validate_for_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('The first letter not to be correct')
def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('name is less than 5')



class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage=forms.IntegerField()
    semail=forms.EmailField(validators=[validate_for_a])