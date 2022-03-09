from django.db.models import Model
from django.forms import ModelForm
from issuerAccounts.models import *

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['address',]