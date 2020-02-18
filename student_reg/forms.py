from django.forms import ModelForm
from .models import Table


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = '__all__'



        

