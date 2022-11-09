from django import template
import datetime 

register = template.Library() 

@register.filter
def is_younger_than_ten_days(value):
	if value != None:
		if isinstance(value, datetime.datetime):
			value = value.date()
		delta = value - datetime.date.today()
		return delta.days < 10
	else:  
		return False
		