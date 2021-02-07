from django.forms import ModelForm
from .models import Wacky



class WackyForm(ModelForm):
   class Meta:
         model = Wacky
         fields = '__all__'