from django.shortcuts import render
from core.models import *
from django.contrib.auth.models import User

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

__all__ = ['index'] 

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