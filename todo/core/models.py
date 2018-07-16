import datetime

from django.db import models
from django.contrib.auth.models import User

__all__ = ['Activity', 'Usr_activities']

# Create your models here.

class Activity(models.Model):
	users = models.ManyToManyField(User, 
							  verbose_name='Related Users')
	title = models.CharField("Activity Name", max_length=30)
	description = models.TextField("Description", null=True)
	date = models.DateField("Date")
	time = models.TimeField("Time", null=True)
	is_done = models.BooleanField("Done", default=False)
	dt_created = models.DateTimeField("Created on",default=datetime.datetime.now())

	class Meta:
		verbose_name = "Activity"
		verbose_name_plural = "Activities"

	def __str__(self):
		return self.title


class Usr_activities(models.Model):
	fk_activity = models.ForeignKey('Activity', 
									on_delete='DO_NOTHING',
									verbose_name="Related Activity")
	fk_user = models.ForeignKey(User, 
								on_delete='DO_NOTHING',
								verbose_name="Related User")

	class Meta:
		verbose_name = "User Activity"
		verbose_name_plural = "User Activities"

	def __str__(self):
		return f'{self.fk_activity.title}{self.fk_user.name}'