from django.forms import ModelForm
from .models import Check, Result


class CheckForm(ModelForm):
    class Meta:
        model = Check
        fields = '__all__'


class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

