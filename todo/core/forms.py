from django import forms
from core.models import *

__all__ = ['FoodApiForm']

class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		fields = '__all__'

class Usr_activitiesForm(forms.ModelForm):
	class Meta:
		model = Usr_activities
		fields = '__all__'

class FoodApiForm(forms.Form):
	api_key = forms.CharField(label='Your Api Key', max_length=50)
	api_id = forms.CharField(label='Your User App ID', max_length=50)
	from_ = forms.IntegerField(label='From', required=False)
	to = forms.IntegerField(label='To', required=False)
	ingr = forms.IntegerField(label='Max. Ingredients', required=False)
	calories = forms.CharField(label='Calories Range (MIN-MAX)', max_length=30, required=False)

	query = forms.CharField(label='Search for', max_length=50)
