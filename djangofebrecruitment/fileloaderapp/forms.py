from django import forms
from .models import UploadedFile

#Form for uploading a new file from the computer
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

#Form for selecting an existing file from the server
class SelectFileForm(forms.Form):
    existing_file = forms.ModelChoiceField(
        queryset=UploadedFile.objects.all(),
        required=True,
        empty_label="Choose an existing file", 
        label="Select a file"
    )

