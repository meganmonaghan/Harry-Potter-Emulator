import hp_classes as hpc 
import hp_items as hpi 
import time
import random

express_dict = {}
# test_train_dict = {}
# test_student_list = ['Hannah Abbott', 'Terry Boot', 'Vincent Crabbe',
# 					'Gregory Goyle', 'Draco Malfoy', 'Ron Weasley',
# 					'Hermione Granger', 'Ernie MacMillan', 'Anthony Goldstein',
# 					'Susan Bones', 'Lavender Brown', 'Padma Patil',
# 					'Parvati Patil', 'Pansy Parkinson', 'Seamus Finnegan',
# 					'Dean Thomas', 'Neville Longbottom', 'Justin Finch-Fletchley']

# create the train
def generate_hogwarts_express(train_dict, student_list):
	for x in range(1,7):
		students_in_car = []
		for i in range(3):
			student_added = random.choice(student_list)
			students_in_car.append(student_added)
			student_list.remove(student_added)
		train_dict[x] = students_in_car
	return train_dict

# actually go on the train
def navigate_hogwarts_express(person, train_dict):
	cars_unvisited = [1, 2, 3, 4, 5, 6]
	visit_tally = 0
	action = int(input(f'''
***
		{person.name} follows the crowd of students
		onto the Hogwarts Express, anxious to find a
		car to stash their trunk.
		Which car do they enter first?

		Select a car between 1-6.
	'''))
	# first two cars visited
	while visit_tally < 2:
		if action not in range(1,7):
			action = int(input(f'''
***
		Sorry, the Hogwarts Express does not have
		a car {action}. Please select a car between
		1-6 for {person.name} to enter.
	'''))
		else:
			if action in cars_unvisited:
				time.sleep(1)
				visit_tally += 1
				cars_unvisited.remove(action)
				action = int(input(f'''
***
		{person.name} enters car {action}.

		There are three other students in the
		car. They introduce themselves:
		{', '.join(train_dict[action])}

***
		{person.name} decides to visit another car.

		Which car do they visit next?
		Select a new car between 1-6.
	'''))
			else:
				action = int(input(f'''
***
		{person.name} has already entered that car.

		Please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	while action not in cars_unvisited:
		action = int(input(f'''
***
		{person.name} has already entered that car.

		Please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	# successfully visit car 3
	cars_unvisited.remove(action)
	visit_tally += 1
	time.sleep(1)
	print(f'''
***
		{person.name} enters car {action}.

		Again, there are three students in 
		the car:
		{', '.join(train_dict[action])}
	''')
	# trolley witch choice
	time.sleep(1)
	action = input(f'''
***
		As {person.name} leaves car {action}, they see a kindly
		witch pushing a trolley along the corridor. The
		 trolley is piled high with brightly-colored sweets,
		 decadent pastries, and ice-cold drinks.

		'Anything off the trolley, dear?'
***
		Buy snacks off the trolley? (Y/N)
	''')
	if action.lower() == 'y':
		time.sleep(1)
		print(f'''
***
		{person.name} purchases a few snacks and
		continues to walk along the corridor towards
		another car.
	''')
		print(person.add_to_inventory('Trolley Snacks'))
	else:
		time.sleep(1)
		print(f'''
***
		{person.name} is tempted by the snacks, but
		ultimately decides against it. they
		continue to walk along the corridor towards
		another car.
	''')
	time.sleep(1)	
	action = int(input(f'''
***
		Which car does {person.name} enter
		next? Select a car number from 1-6 that has
		not yet been visited.
	'''))
	# choosing car 4 and 5
	while visit_tally < 4:
		if action not in range(1,7):
			action = int(input(f'''
***
		Sorry, the Hogwarts Express does not have
		a car {action}. Please select another car
		between 1-6 for {person.name} to enter.
	'''))
		else:
			if action in cars_unvisited:
				time.sleep(1)
				visit_tally += 1
				cars_unvisited.remove(action)
				action = int(input(f'''
***
		{person.name} enters car {action}.

		Three students are already in the car, 
		deep in conversation:
		{', '.join(train_dict[action])}
***
		{person.name} decides to visit another car.

		What car do they visit next?
		Select a new car between 1-6.
	'''))
			else:
				action = int(input(f'''
***
		{person.name} has already entered that car.

		Please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	time.sleep(1)
	while action not in cars_unvisited:
		action = int(input(f'''
***
		{person.name} has already entered that car.

		Please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	# after car five choice - robes
	visit_tally +=1
	cars_unvisited.remove(action)
	time.sleep(1)
	print(f'''
***
		{person.name} enters car {action}.

		The car has three occupants:
		{', '.join(train_dict[action])}

		They invite {person.name} to sit and talk
		for a little while.
	''')
	time.sleep(1)
	if 'Robes' in person.inventory:
		print(f'''
***
		As the ride continues, the daylight from
		the windows begins to dim. Lanterns are 
		lit along the corridor. {person.name} can hear
		the excited chattering of the other students.

		'We're nearly there!'

		'Must be time to start getting ready.'

		{person.name} withdraws the robes carefully packed
		in their trunk and get dressed, pointed black hat
		placed carefully on their head.
	''')
	else:
		print(f'''
***
		As the ride continues, the daylight from
		the windows begins to dim. Lanterns are 
		lit along the corridor. {person.name} can hear
		the excited chattering of the other students.

		'We're nearly there!'

		'Must be time to start getting ready.'

		As the other students in car {action} begin
		getting dressed, {person.name} is seized with
		panic. They hadn't remembered to purchase robes
		at Diagon Alley.

		'Do you need to borrow a set of robes?'

		It's {random.choice(train_dict[action])}, one of the students
		in the car. They smile and offer {person.name} a neat set 
		of folded robes from their trunk.

		'My parents were extra excited about me coming to
		Hogwarts, so they packed me an extra set of everything.
		You can keep these!'
	''')
		print(person.add_to_inventory('Secondhand Robes'))
	# car six choice
	time.sleep(1)
	action = int(input(f'''
***
		Robes donned, {person.name} is feeling more
		and more excited about the evening to come. They
		decide to walk off some of their excitement by 
		visiting another car.

		Which car does {person.name} enter next?
		Submit a new car number between 1-6.
	'''))
	if action not in range(1,7):
		action = int(input(f'''
***
		Sorry, the Hogwarts Express does not have
		a car {action}. Please select another car
		between 1-6 for {person.name} to enter.
	'''))
	else:
		while action not in cars_unvisited:
			action = int(input(f'''
***
		{person.name} has already entered that car.

		Please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	time.sleep(1)
	print(f'''
***
		{person.name} enters car {action}.

		The students sitting in the car, robes on:
		{', '.join(train_dict[action])}
	''')
	cars_unvisited.remove(action)
	time.sleep(1)
	print(f'''
***
		As the Hogwarts Express comes to a slow stop, 
		{person.name} looks through the nearest window. There
		is little to see through the darkness, save for a
		few flickering torches and the bustle of students
		as they exit with their belongings.
	''')
	return train_dict

if __name__ == '__main__':
	h_express_cars = generate_hogwarts_express(express_dict, hpi.year1_student_list)
	user = hpc.Student('Megan')
	# user.add_to_inventory('Robes')
	print(navigate_hogwarts_express(user, h_express_cars))