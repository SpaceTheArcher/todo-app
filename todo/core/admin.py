from django.contrib import admin
from core.models import *

# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
	pass

class Usr_activitiesAdmin(admin.ModelAdmin):
	pass

admin.site.register(Activity)
admin.site.register(Usr_activities)