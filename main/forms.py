from django.forms import ModelForm
from .models import Check, Result


class CheckForm(ModelForm):
    class Meta:
        model = Check
        fields = '__all__'


class ResultForm(ModelForm):
    class Meta:
        model = Result
        check_id = Result.check_id
        fields = [
            'check_id',
            'status',
        ]
