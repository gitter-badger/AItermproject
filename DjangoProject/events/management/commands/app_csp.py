# formulate the anti party pooper CSP

from csp import *


def formulate_app_csp(activities,days,votes):

	vars = ['X_activity','X_datetime','X_attendees']

	# create the domains 
	domains = {}

	# domain for X_activity is just the list of acitivities
	domains['X_activity'] = activities

	# domain for X_datetime
	X_datetime_domain = set([])
	for act in activities:
		set_of_days = days[act] # is of type django.db.models.query.QuerySet
		for day in set_of_days:
			# day is of type models.Day, which has an attribute called 'day' which is a datetime
			if day.day not in X_datetime_domain:
				X_datetime_domain.add(day.day)

	domains['X_datetime'] = list(X_datetime_domain)

	# domain for X_attendees
	domains['X_attendees'] = range(1000)


	neighbors = {}
	neighbors['X_activity'] = ['X_datetime','X_attendees']
	neighbors['X_datetime'] = ['X_activity']
	neighbors['X_attendees'] = ['X_activity']
	    
	# the constraints

	def constraints(A,a,B,b):
		if activity_datetime_constraint(A,a,B,b):
			return True
		elif activity_attendees_constraint(A,a,B,b):
			return True
		else:
			return False

	def activity_datetime_constraint(A,a,B,b):
		if A == 'X_activity' and B == 'X_datetime':
			activity = a
			datetime = b
		elif A == 'X_datetime' and B == 'X_activity':
			activity = b
			datetime = a
		else:
			return False
		# get the QuerySet object associated with activity
		set_of_days = days[activity]
		for day in set_of_days:
			if datetime == day.day:
				return True
		return False

	def activity_attendees_constraint(A,a,B,b):
		if A == 'X_activity' and B == 'X_attendees':
			activity = a
			number_of_attendees = b
		elif A == 'X_attendees' and B == 'X_activity':
			activity = b
			number_of_attendees = a
		else:
			return False
		if number_of_attendees<activity.min_atendees:
			return False
		if number_of_attendees>activity.max_atendees:
			return False
		return True

	app_csp = CSP(vars,domains,neighbors,constraints)

	app_csp.curr_domain = 
	AC3(app_csp)

	print app_csp.domains

	#print min_conflicts(CSP(vars,domains,neighbors,constraints),1000)