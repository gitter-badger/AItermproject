import re;
import uuid;

#these globals represent the database
#global varuabke of all events being hosted, dict mapping unique eventID to associated instance of the Event class
eventIDs = {}
#global variable of all users in the networks, dict mapping userID to associated instance of the User Class
usernames = {}
userIDs= {}
#global variable dictionary keeping track of all suggested activites and how frequently they are suggested
allSuggestedActivities = {}


userID_minLength = 8
userID_maxLength = 16

#Regular Expressions
yes_no_re = re.compile(r'yes|no|y|n\Z')
yes_no_maybe_re = re.compile(r'yes|no|maybe|y|n|m\Z')
validUserID_re = re.compile(r'\w{8,16}\Z')
validUserIDSearch_re = re.compile(r'\w{0,16}\Z')

"""class Users:
	def _init__(self):
		self.users = {}

	def addUser(self, userID):
		if userID in self.users:
			print 'user already exists!'
			return
		#self.users[userID] = """

class User:
	#need to 
	"""
	User Class

	attributes
		-userID is unique ID for each instance a User
		-eventIDs is a dict mapping each eventID for which the user has been invited to they corresponding is the duration of each time interval for which to check availability
		-schedule is 
		-pastSuggestions is a dict mapping all suggestions a user has suggested in the past to the number of times they have suggested each activity

	methods
	 	suggestActivity - takes activityName, eventID, and (duration) as inputs and suggests the activity to the host of the event
	"""

	def __init__(self, username):
		self.userID = uuid4()
		self.username = username
		self.eventNames = {}
		#self.hostedEventIDs = {}
		#self.authorizedEventIDs = {}
		self.hostedEventNames = {}?
		self.authorizedEventNames = {}
		#self.schedule = AvailabilitySchedule()
		self.pastSuggestions = {}

	#gets
	def getUserID(self):
		return self.userID

	def getUsername(self):
		return self.username

	def getEventNames(self):
		return self.eventNames

	def getHostedEventNames(self):
		return self.hostedEventNames

	def getAuthorizedEventNames(self):
		return self.authorizedEventNames

	def getPastSuggestions(self):
		return self.pastSuggestions

	#methods as host
	def authorizeUser(self, eventName, username):
		return

	def unauthorizeUser(self, eventName, username):
		return

	def cancelEvent(self, eventName):
		return

	def finalizeEvent(self, eventName):
		return

	def removeOfferedActivity(self, event, offeredActivity):
		return

	#methods as authorized user
	def addOfferedActivity(self, event, offeredActivity):
		return

	def addOfferedSchedule(self, event, offeredSchedule):
		return

	def addGuest(self, event, user):
		return

	#methods as user
	def hostEvent(self, event):
		
		eventID = uuid.uuid4()
		while eventID in eventIDs:
			eventID = uuid.uuid4()
		eventNum = 0;
		eventNameKey = eventName + '#' = str(eventNum)
		while eventNameKey in self.eventNames.keys():
			eventNum += 1
			eventNameKey = eventName + '#' = str(eventNum)
		self.eventNames[eventNameKey] = eventID
		eventIDs[eventID] = Event()

		return

	def isHostForEvent(self, event):
		return event.getEventName() in self.hostedEventNames

	def isAuthorizedForEvent(self, event):
		return event.getEventName() in self.authorizedEventNames

	def printEventNames(self):
		for eventID in self.eventIDs.keys():
			print self.eventIDs[eventID].getEventName()

	def suggestActivity(activityName, eventID, duration = 180):
		activityName = activityName.lower()
		if activityName not in self.pastSuggestions:
			self.pastSuggestions[activityName] = 1
		else:
			self.pastSuggestions[activityName] += 1
		if activityName not in allSuggestedActivities:
			allSuggestedActivities[activityName] = 1
		else:
			allSuggestedActivities[activityName] += 1

		return

class Activity:

	def __init__(self, activityName, duration=180):
		self.activityName = activityName
		self.duration = duration

	#def getActivityID(self):
	#	return self.activityID

	def getActivityName(self):
		return self.activityName

	def getDuration(self):
		return self.duration

	def setDuration(self, newDuration):
		self.duration = newDuration
		return

class Event:
	"""
	Event Class

	attributes
		-eventID
		-eventName
		-hostIDs dict mapping id to host value. If value is 1, they are original host, o/w it is 2.
		-guestList 
		-activitiesOffered 
		-suggestedActivites 
		-schedule 

	methods
	"""
	def __init__(self, host, schedule_slots, frequency=60, clock=12):
		self.eventName = eventName
		self.hostIDs = {host.getID:1}
		self.guestList = {}
		self.activitiesOffered = []
		self.suggestedActivites = {}
		self.schedule = Schedule(schedule_slots, frequency, clock)
		#self.suggestedScheduleAdditions = 
#gets

	def getEventName(self):
		return self.eventName

	def getGuestList(self):
		return self.guestList
	
	def getHostID(self):
		return self.hostID
	
	def getActivitiesOffered(self):
		return self.activitiesOffered
	
	def getSuggestedActivities(self):
		return self.suggestedActivites

	def getSchedule(self):
		return self.schedule

	def addSuggestedActivity(self, activity):
		if activity.getActivityID in self.suggestedActivites:
			
		
	def authorizeHost(self, user):
		if user.getUserID in self.hostID
		return

	def authorizeNewOriginalHost(self, user=None):
		return

	def addToGuestList(self, user):
		if user.getUserID not in self.guestList:
			self.guestList{user.getUserID:None}
		else:
			print '{0} already on guestList'.format(user.getUserID)
		return

class Host(User):
	def __init__(self):
		User.__init__(self)
		self.fullName= fullName
		self.user_suggestions = {}
		self.deadline = getDeadline()
		# self.preference_type = 
		self.allowsMaybe = false

	def authorizeHost(self, ID):
		return

	def deauthorizeHost(self):
		return

	def addHost(self, ID):
		return

class Schedule:
	"""
	dates and times proposed

	attributes
		-schedule is a dictionary corresponding to each day's proposed start and stop times {date:[(timeStart, timeEnd)]}
		-frequency is the duration of each time interval for which to check availability
		-schedule is 

	"""
	def __init__(self, schedule_slots, frequency=60, clock=12):
		self.frequency = frequency
		self.clock = clock
		self.schedule = schedule_slots

	def getFrequency(self):
		return self.frequency

	def getDates(self):
		return self.dates.keys()

class AvailabilitySchedule(Schedule):
	"""
	dates and times available, inherits from Schedule

	attributes
		-availability is a dictionary corresponding to each day/time combination and a bool representing availability{'date+time':bool}

	"""

	def __init__(self):
		Schedule.__init__(self)
		self.availability = {}
		for date in self.dates.keys():
			start_stop_times = dates[date]
			for start_stop_time in start_stop_times:
				startTime = start_stop_time[0]
				endTime = start_stop_time[1]
				for timeSlot in range(startTime, endTime, self.frequency):
					availability_key = date + ' ' + str(timeSlot)
					isAvailable = askIfAvailable(date, getDisplayTime(timeSlot, self.clock))
					self.availability[availability_key] = isAvailable
			#availability[]

	def getAvailableTimes(self):

		return

	def getAvailability(self):
		return self.availability

def getNumMinutes(displayTime, clock=12):
	#calculates number of minutes into the day the given displayedTime represents
	if clock!=12 and clock != 24:
		print 'specified time format invalid (getNumMinutes), using 12-hour clock'
		clock = 12
	#error check
	if not type(displayTime is str):
		print 'Invalid displayTime, not string', __name__
		return -1
	if clock == 12:
		matchObj = re.match(r'(10|11|12|\d):(\d\d)(am|pm)\Z', displayTime) #if fits 12hr format
		if matchObj:
			hours = int(matchObj.group(1))
			minutes = int(matchObj.group(2))
			am_pm = matchObj.group(3)
			time_of_day_adjustment = 0
			if am_pm == 'am':
				if hours == 12:
					print 'negative adjustment', getNumMinutes.__name__
					time_of_day_adjustment = -720
				else:
					time_of_day_adjustment = 720

			return hours * 60 + minutes + time_of_day_adjustment
	if clock == 24:
		matchObj = re.match(r'(0\d|1\d|20|21|22|23):(\d\d)\Z', displayTime) #if fits 24hr format
		if matchObj:
			hours = int(matchObj.group(1))
			minutes = int(matchObj.group(2))
			return hours * 60 + minutes

	print 'Invalid displayTime', getNumMinutes.__name__
	return -1

def getDisplayTime(numMinutes, clock=12):
	# minutesPerDay = 1440
	# minutesPerHalfDay = 720
	if numMinutes >= 1440:
		numMinutes = numMinutes%1440
		print 'specified number of minutes exceeds minutes per day, using', numMinutes
	if clock!=12 and clock != 24:
		print 'specified time format invalid (getDisplayTime), using 12-hour clock'
		clock = 12

	if clock == 12:
		#time calculations
		half_day_minutes = numMinutes%720
		hour_hand = half_day_minutes/60
		if hour_hand == 0: hour_hand = 12
		minute_hand = numMinutes%60
		#string formatting
		minute_hand_string = str(minute_hand).zfill(2)
		am_pm = 'am' if numMinutes<720 else 'pm'
		display_time = '{0}:{1}{2}'.format(hour_hand, minute_hand_string, am_pm)

	elif clock == 24:
		#time calculations
		hour_hundred = (numMinutes/60)*100
		minutes = numMinutes%60
		time_total = hour_hundred + minutes
		display_time = str(time_total).zfill(4)
		display_time = display_time[0:2]+':'+display_time[2:4]

	return display_time

def askIfAvailable(date, time):
	usableInput = None
	while not usableInput:
		answer = raw_input('Are you available on {0} at {1}? Enter yes/no/NOT YET IMPLEMENTED maybe'.format(date,time))
		usableInput = re.match(yes_no_maybe_re, answer.lower())
	print answer
	return answer

"""def getOriginalHostInfo():
	#messages to Host
	youAreTheHost = 'You are hosting an event, please specify some details for us.'
	enterPossibleDatesForTheEvent = 'Please give possible dates you would like to host the event. They should be in the format MM-DD-YYYY'
	#general messages
	invalidInputMsg = 'Invalid input.'

	#date messages
	enterFirstDateMsg = 'Please enter a date in the format MM-DD-YYYY.\n'
	enterNextDateMsg = 'Please enter the next date in the format MM-DD-YYYY.'
	doneEnteringDatesMsg = 'If you are done entering dates, please type \"Next\"'
	#invalidDateMsg = 'Invalid date format, please enter your date in the format MM-DD-YYYY.',
	#time messages
	windowOrSpecifyTimeMsg = 'If you would like to use a time window for all days, please type \"Window\" otherwise, if you would like to specify a time window for each day, please type \"NOT YET IMPLEMENTED Specify NOT YET IMPLEMENTED\"\n'
	enterTimeDisplayFormatMsg = 'If you woud like to display the time in 24-hour format, type \"NOT YET IMPLEMENTED 24\" otherwise if you would like to use 12-hour format, please type type \"12\"\n'
	enterFrequencyMsg = 'Please specify the time interval duration for which you would like to check availability. E.g. type \"30\" if you would like to check 08:30-09:00, 09:00-09:30, etc.\n'
	enterDayStartTimeMsg = 'NOT YET IMPLEMENTED Please enter start hour for {0}.\n'
	enterDayEndTimeMsg = 'NOT YET IMPLEMENTED Please enter end hour for {0}.\n'
	enterDailyStartTimeMsg = 'Please enter start hour for each day.\n'
	enterDailyEndTimeMsg = 'Please enter end hour for each day.\n'
	doneEnteringTimesMsg = 'NOT YET IMPLEMENTED If you are done entering times, please type \"Next\"\n'
	#activity messages
	askHostIfFullyAvailable = 'If you are available during all the time and dates you specified, please type \"Available\" otherwise, if you are unavailable during some of the time and dates specified, please type \"Unavailable\"\n'
	askIfAvailableDuringSlot = 'Are you available on {0} at {1}?'


	return host_info"""

"""def getUserInfo(userID):
	return userID_info"""

def displayMainMenu():
	#returns a main menu choice option as an int
	choiceMatch = None
	while not choiceMatch:
		print "\n\n\nDISPLAYING MAIN MENU\nWhat would you like to do"
		print "\t (1) Create a user?"
		print "\t (2) Search/See a list of user IDs?"
		print "\t (3) Login as a user?"
		print "\t (4) Import a dataset?"
		print "\t (5) Exit"
		choice = raw_input('Selection: ')
		choiceMatch = re.match(r'([12345]|(exit))\Z', choice.lower())
	return int(choice)

def displayMenu(menuSelection):
	backToMainMenuMsg = 'If you wish to return to the main menu, enter \"return!\"'
	invalidInputMsg = 'Invalid input -'
	alreadyExistsMsg = 'already exists, please enter a different user ID to create'
	doesNotExistMsg = 'does not exist, please enter a different user ID'
	#Create User ID Menu
	if menuSelection == 1:
		print '\n\n\nDISPLAYING CREATE USER ID MENU\n'+backToMainMenuMsg
		doneCreatingIDs = False
		while not doneCreatingIDs:
			enteredID = raw_input('\nEnter a user ID with 8-16 alphanumeric characters: ')
			if enteredID.lower() == 'return!':
				return

			validIDMatchObj = re.match(validUserID_re, enteredID)
			if validIDMatchObj and enteredID not in userIDs:
				userIDs[enteredID] = User(enteredID)
				print 'ID : {0} created!\n'.format(enteredID)
				validAnsObj = None
				while not validAnsObj:
					createAnotherIDAnswer = raw_input('Create another ID (Y/N)? ')
					validAnsObj = re.match(yes_no_re, createAnotherIDAnswer)
				#hacky
				doneCreatingIDs = ('y') not in createAnotherIDAnswer.lower()
			elif enteredID in userIDs:
				print enteredID, alreadyExistsMsg
			else:
				print invalidInputMsg, enteredID 
		return

	#Search/See User ID Menu
	if menuSelection == 2:
		print '\nDISPLAYING SEARCH/SEE USERID MENU\n'+backToMainMenuMsg
		doneSearchingIDs = False
		while not doneSearchingIDs:
			print 'Enter a part or all of the user ID you are searching for,'
			print 'or press enter to display all user IDs:'
			validSearchKey = None
			while not validSearchKey:
				print 'Keep in mind user IDs are alphanumeric and no longer than 16 characters\n'
				searchVal = raw_input('Search for strings containing: ')
				if searchVal.lower() == 'return!':
					return
				validSearchKey = re.match(validUserIDSearch_re, searchVal)
			if len(searchVal) == 0:
				print '\nDisplaying all user IDs:\n'
			else:
				print '\nDisplaying IDs containing \'{0}\' :\n'.format(searchVal)
			for userID in userIDs:
				if searchVal in userID:
					print userID
			validAnsObj = None
			while not validAnsObj:
				searchAnotherIDAnswer = raw_input('\nSearch for another ID (Y/N)? ')
				validAnsObj = re.match(yes_no_re, searchAnotherIDAnswer)
			#hacky
			doneSearchingIDs = ('y') not in searchAnotherIDAnswer.lower()

	#Login Menu
	if menuSelection == 3:
		print '\nDISPLAYING LOGIN MENU\n'+backToMainMenuMsg
		isLoggedIn = False
		while not is isLoggedIn:
			enteredID = raw_input('\nEnter a user ID: ')
			if enteredID.lower() == 'return!':
				return
			validIDMatchObj = re.match(validUserID_re, enteredID)
			if validIDMatchObj and enteredID in userIDs:
				isLoggedIn = True
				displayLoggedInMenu(enteredID)
			elif validIDMatchObj:
				print enteredID, doesNotExistsMsg
			else:
				print invalidInputMsg, enteredID 
		return

def displayLoggedInMenu(enteredID):
	return


def main():
	while True:
		nextMenuNum = displayMainMenu()
		if nextMenuNum == 5 or nextMenuNum == 'exit':
			return
		displayMenu(nextMenuNum)
	host_info = getHostInfo()
	return

if __name__ == '__main__':
	main()