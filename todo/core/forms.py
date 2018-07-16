from django import forms
from core.models import *

class ActivityForm(forms.ModelForm):
	class Meta:
		model = Activity
		fields = '__all__'

class Usr_activitiesForm(forms.ModelForm):
	class Meta:
		model = Usr_activities
		fields = '__all__'
