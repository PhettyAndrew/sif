from django import forms
from . models import Management, Team, News, Donations, Support, GeneralInfo, ShowImages

class SupporterForm(forms.ModelForm):
    class Meta:
        model=Support
        fields=['name','email','messsage']