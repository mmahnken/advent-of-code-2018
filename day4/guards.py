import datetime as dt
from collections import Counter


def get_guards():
	records = {}
	
	# sort records
	with open("input.txt") as f:
		for line in f:
			line = line.strip()
			month = int(line[6:8])
			day = int(line[9:11])
			minute = int(line[15:17])
			hour = int(line[12:14])

			workshift = dt.datetime(month=month, day=day, year=1518,
									minute=minute, hour=hour)

			if workshift in records:
				print("REPEAT FOUND, trying to add")
				print(line)
				print("ALREADY HAVE")
				print(records[workshift])
			records[workshift] = line

	sleep_log = {}

	for record in sorted(records):
		# print(records[record])
		tokens = records[record].split('] ')
		content = tokens[1]
		timestamp = tokens[0][1:]
		
		if content.startswith("Guard"):
			guard_id = content.split()[1]
			
			if guard_id in sleep_log:
				current_guard = sleep_log[guard_id]
			else:
				current_guard = Guard(guard_id)
				sleep_log[guard_id] = current_guard

		elif content.startswith("falls asleep"):
			sleep_start = record.minute

		elif content.startswith("wakes up"):
			sleep_end = record.minute
			new_sleep = Sleep(sleep_start, sleep_end, timestamp)
			current_guard.sleeps.append(new_sleep)
	return sleep_log
			

def find_guard(guards):
	sleepiest = {
	    'max_minutes': float('-inf')
	}

	for guard in guards:
		total = guards[guard].get_total_mins()
		
		if total > sleepiest['max_minutes']:
			sleepiest = {'max_minutes': total, 'guard': guards[guard]}

	print("SLEEPIEST GUARD", sleepiest['guard'].guard_id)

	return sleepiest['guard'].get_most_common_minute()



class Guard(object):
	guard_id = None

	def __init__(self, guard_id):
		self.guard_id = guard_id
		self.sleeps = []

	def get_total_mins(self):
		return sum([s.total_mins for s in self.sleeps])

	def get_most_common_minute(self):
		mins_slept = []
		
		for sleep in self.sleeps:
			mins_slept.extend(range(sleep.start, sleep.end))

		if self.sleeps:
			c = Counter(mins_slept)

			most_common_minute = sorted(c, key=lambda k: c[k])[-1]

			return {
					'winner': most_common_minute, 
				    'frequency': c[most_common_minute]
			}

	def __repr__(self):
		return "<Guard guard_id={}>".format(self.guard_id)


class Sleep(object):
	date = None
	start = None
	end = None
	total_mins = None

	def __init__(self, start, end, date):
		self.start = start
		self.end = end
		self.date = date
		self._total_mins = end - start

	@property
	def total_mins(self):
		return self._total_mins

	def __repr__(self):
		return "<Sleep start={} end={} date={} total_mins={}>".format(
			self.start, 
			self.end,
			self.date,
			self.total_mins
		)
	
def find_most_predictable_guard(guards):
	"""PART 2"""

	most_common_minutes = {}
	
	for g in guards:
		current_guard = guards[g]
		mcm = current_guard.get_most_common_minute()
		if mcm:
			most_common_minutes[mcm['frequency']] = (mcm['winner'], current_guard.guard_id)
	
	return most_common_minutes[max(most_common_minutes)]


log = get_guards()
# s = find_guard(log)
print(find_most_predictable_guard(log))
