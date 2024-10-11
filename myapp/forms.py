from django import forms

class TextInputForm(forms.Form):
    text_file = forms.FileField(required=False, label="Файлды жүктеңіз (.txt, .docx, .pdf)")
    text_area = forms.CharField(widget=forms.Textarea, required=False, label="Тексті енгізіңіз")