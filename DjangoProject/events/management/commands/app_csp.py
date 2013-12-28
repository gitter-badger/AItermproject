# formulate the anti party pooper CSP

from csp import *
from itertools import combinations, chain


def formulate_app_csp(activities,days,positiveVotes,negativeVotes,users):

	vars = ['X_activity','X_day','X_attendees']

	# create the domains
	domains = {}

	# domain for X_activity is just the list of acitivities
	domains['X_activity'] = list(activities)

	# domain for X_day
	X_day_domain = set([])
	for act in activities:
<<<<<<< HEAD
		set_of_days = days[act] # is of type django.db.models.query.QuerySet
		for day in set_of_days:
			# day is of type models.Day, which has an attribute called 'day' which is a datetime
			if day.dateAndTime not in X_datetime_domain:
				X_datetime_domain.add(day.dateAndTime)

	domains['X_datetime'] = list(X_datetime_domain)

	# domain for X_attendees
	domains['X_attendees'] = range(100)
=======
		X_day_domain = X_day_domain.union(days[act])
	domains['X_day'] = list(X_day_domain)

	# domain for X_attendees
	powerset = lambda S: list(chain(*[combinations(S, ni) for ni in range(len(S)+1)]))
	domains['X_attendees'] = powerset(users)
>>>>>>> CSP


	neighbors = {}
	neighbors['X_activity'] = ['X_day','X_attendees']
	neighbors['X_day'] = ['X_activity','X_attendees']
	neighbors['X_attendees'] = ['X_activity','X_day']

	# the constraints

	def constraints(A,a,B,b):
		if activity_day_constraint(A,a,B,b):
			return True
		elif activity_attendees_constraint(A,a,B,b):
			return True
		elif day_attendees_constraint(A,a,B,b):
			return True
		else:
			return False

	'''
	checks whether the chosen chosen DAY is one of the proposed days for the
	chosen ACTIVITY and if the number of VOTES associated with this DAY exceeds
	the limits on the number of attendees given by the ACTIVITY
	'''
	def activity_day_constraint(A,a,B,b):
		if A == 'X_activity' and B == 'X_day':
			activity = a
			day = b
		elif A == 'X_day' and B == 'X_activity':
			activity = b
			day = a
		else:
			return False
<<<<<<< HEAD
		# get the QuerySet object associated with activity
		set_of_days = days[activity]
		for day in set_of_days:
			if datetime == day.dateAndTime:
				return True
		return False
=======
		if day not in days[activity]:
			return False
		nof_pos_votes = len(positiveVotes[day])
		if nof_pos_votes < activity.min_attendees:
			return False
		if nof_pos_votes > activity.max_attendees:
			return False
		return True
>>>>>>> CSP

	def activity_attendees_constraint(A,a,B,b):
		if A == 'X_activity' and B == 'X_attendees':
			activity = a
			number_of_attendees = len(b)
		elif A == 'X_attendees' and B == 'X_activity':
			activity = b
			number_of_attendees = len(a)
		else:
			return False
<<<<<<< HEAD
=======

>>>>>>> CSP
		if number_of_attendees<activity.min_attendees:
			return False
		if number_of_attendees>activity.max_attendees:
			return False
		return True

	def day_attendees_constraint(A,a,B,b):
		if A == 'X_day' and B == 'X_attendees':
			day = a
			attendees = b
		elif A == 'X_attendees' and B == 'X_day':
			day = b
			attendees = a
		else:
			return False

		for attendee in attendees:
			if not any(v.user == attendee for v in positiveVotes[day]):
				return False
		return True

	app_csp = CSP(vars,domains,neighbors,constraints)

	print len(app_csp.domains['X_attendees'])

	app_csp.curr_domains = domains
	AC3(app_csp)
	app_csp.curr_domain = None
<<<<<<< HEAD

	print len(app_csp.domains['X_attendees'])

	print min_conflicts(CSP(vars,domains,neighbors,constraints),1000)
=======

	print len(app_csp.domains['X_attendees'])


	print min_conflicts(CSP(vars,domains,neighbors,constraints),1000)
>>>>>>> CSP
