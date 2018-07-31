from django.shortcuts import render
from core.models import *
from core.forms import *
from django.contrib.auth.models import User
from .foodapi import food_search

# Aux Functions

def treat_name(usr):
	name = usr.get_full_name()
	if name == '':
		name = usr.username.upper()
		return name[:2]
	vowels = ['a', 'e', 'i', 'o', 'u']
	strips = name.split(' ')
	print(strips)
	if len(strips) > 1:
		name_fxd = strips[0][0] + strips[-1][0]
		return name_fxd
	else:
		if strips[0] == '':
			return name
		name_fxd = strips[0][0]
		for i in name[:-2:-1]:
			if i not in vowels:
				name_fxd += i
				return name_fxd
		name_fxd += strips[-1][0]
		return name_fxd
# Create your views here.

__all__ = ['index', 'foodapi'] 

def get_activities(user):
	acts = []
	for a in Activity.objects.all():
		if user == a.users:
			acts.append(a)
	if len(acts) == 0:
		return False
	return acts


def index(request):
	user = request.user
	usr_acts = Activity.objects.filter(users=user)
	for act in usr_acts:
		tmp = []
		for usr in act.users.all():
			nm = treat_name(usr)
			tmp.append(nm)
		act.names = tmp
	context = {
		'user':user,
		'usr_acts':usr_acts,
	}
	return render(request, 'index.html', context)

def foodapi(request):
	if request.POST:
		form = FoodApiForm(request.POST)
		if form.is_valid():
			fs = food_search(
				form.cleaned_data['api_id'],
				form.cleaned_data['api_key'],
				q=form.cleaned_data['query'],
				from_=form.cleaned_data['from_'],
				to=form.cleaned_data['to'],
				ingr=form.cleaned_data['ingr'],
				calories=form.cleaned_data['calories']
				)
			result = fs._get_result().get('hits')
	else:
		form = FoodApiForm()
		result = None
	context = {
		'form':form,
		'result':result,
	}
	return render(request, 'foodapi.html', context)