from django import forms
from imageuploadapp.models import ImageUplaodModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUplaodModel
        fields = '__all__'
