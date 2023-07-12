
from django import forms
from django.core import validators
def validate_for_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('The first letter not to be correct')
def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('name is less than 5')



class StudentForm(forms.Form):
    email=forms.EmailField()
    remail=forms.EmailField()
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validators.RegexValidator])
    sage=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    moblie=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!= re :
            raise forms.ValidationError('emails are not matched')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('Not Valid!!!!')

