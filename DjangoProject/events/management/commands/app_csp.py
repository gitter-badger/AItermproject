# formulate the anti party pooper CSP

from csp import *
from events.models import *
from itertools import combinations, chain
from django.contrib.auth.models import User


def formulate_app_csp(event):
	# loading all activities
	activities = list(Activity.objects.all().filter(event=event))

	# loading all days
	days = {}
	positiveVotes = {}
	negativeVotes = {}
	for activity in activities:
	    temp_list_days = Day.objects.all().filter(activity=activity)
	    days[activity] = list(temp_list_days)
	    for day in temp_list_days:
	        positiveVotes[day] = list(Vote.objects.all().filter(day=day,will_go=True))
	        negativeVotes[day] = list(Vote.objects.all().filter(day=day,will_go=False))

	users = list(User.objects.all())
	#now we have all activities with its days and votes loaded
	variables = ['X_activity','X_day','X_attendees']

	# create the domains
	domains = {}

	# domain for X_activity is just the list of acitivities
	domains['X_activity'] = list(activities)

	# domain for X_day
	X_day_domain = set([])
	for act in activities:
		X_day_domain = X_day_domain.union(days[act])
	domains['X_day'] = list(X_day_domain)

	# domain for X_attendees
	powerset = lambda S: list(chain(*[combinations(S, ni) for ni in reversed(range(len(S)+1))]))
	domains['X_attendees'] = powerset(users)

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

		if day not in days[activity]:
			return False
		nof_pos_votes = len(positiveVotes[day])
		if nof_pos_votes < activity.min_attendees:
			return False
		if nof_pos_votes > activity.max_attendees:
			return False
		return True

	def activity_attendees_constraint(A,a,B,b):
		if A == 'X_activity' and B == 'X_attendees':
			activity = a
			number_of_attendees = len(b)
		elif A == 'X_attendees' and B == 'X_activity':
			activity = b
			number_of_attendees = len(a)
		else:
			return False

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

	app_csp = CSP(variables,domains,neighbors,constraints)

	#print len(app_csp.domains['X_attendees'])

	app_csp.curr_domains = domains
	AC3(app_csp)
	print("AC3 done")
	#app_csp.curr_domain = None

	#print len(app_csp.domains['X_attendees'])

	#Define the goal
	goal = 0
	for attendee in app_csp.domains['X_attendees']:
		if len(attendee) > goal:
			goal = len(attendee)
	#Evaluation funcion
	def eval(solution):
		if not solution:
			return -1
		return len(solution[2])#attendees lenght
	#Solution check function
	def valid(solution):
		if activity_day_constraint('X_activity',solution[0],'X_day',solution[1]):
			return True
		elif activity_attendees_constraint('X_attendees',solution[2],'X_activity',solution[0]):
			return True
		elif day_attendees_constraint('X_attendees',solution[2],'X_day',solution[1]):
			return True
		else:
			return False
	#Search the solution BFS
	current_solution = None
	flag = False
	for act in app_csp.domains['X_activity']:
		for day in app_csp.domains['X_day']:
			for att in  app_csp.domains['X_attendees']:
				solution = (act,day,att)
				#check if the solution is beter than the current one
				if eval(solution) < eval(current_solution):
					continue
				#check if is an actual solution
				if valid(solution):
					current_solution=solution
					#if we reached the goal no more search
					if eval(solution) >= goal:
						flag = True
						break
			if flag:
				break
		if flag:
			break
	print("Search done")
	print (solution)
	return solution
