from django import forms

class idform(forms.Form):
    image_file = forms.ImageField()
    xml_file = forms.FileField()
    
class SearchForm(forms.Form):
    From = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    To = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))