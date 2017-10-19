from django import forms

from django_countries.widgets import CountrySelectWidget

from django_countries import countries
from . import models

class CountryLinkForm(forms.Form):
    country_code = forms.CharField(label='country code', max_length=2)



class CountryInfoForm(forms.ModelForm):

    class Meta:
        model = models.CountryInfo
        #fields = ('notes', 'country')
        fields = ('notes',)


class ChooseCountryForm(forms.Form):
    country = forms.ChoiceField(choices=countries,
                                label="country_select",
                                initial='US',
                                #widget=forms.Select(),
                                required=True,)


class UpdateCountryInfoForm(forms.ModelForm):
    class Meta:
        model = models.CountryInfo
        fields = ('notes',)

