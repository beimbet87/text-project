from django import forms

class TextInputForm(forms.Form):
    text_file = forms.FileField(required=False, label="Upload a text file")
    text_area = forms.CharField(widget=forms.Textarea, required=False, label="Enter text manually")