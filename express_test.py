import hp_classes as hpc 
import hp_items as hpi 
import time
import random

test_train_dict = {}
test_student_list = ['Hannah Abbott', 'Terry Boot', 'Vincent Crabbe',
					'Gregory Goyle', 'Draco Malfoy', 'Ron Weasley',
					'Hermione Granger', 'Ernie MacMillan', 'Anthony Goldstein',
					'Susan Bones', 'Lavender Brown', 'Padma Patil',
					'Parvati Patil', 'Pansy Parkinson', 'Seamus Finnegan',
					'Dean Thomas', 'Neville Longbottom', 'Justin Finch-Fletchley']

# create the train
def generate_hogwarts_express(train_dict, student_list):
	for x in range(1,7):
		students_in_car = []
		for i in range(3):
			student_added = random.choice(student_list)
			students_in_car.append(student_added)
			student_list.remove(student_added)
		test_train_dict[x] = students_in_car
	return train_dict

# actually go on the train
def navigate_hogwarts_express(person, train_dict):
	cars_unvisited = [1, 2, 3, 4, 5, 6]
	visit_tally = 0
	action = int(input(f'''
***
		{person.name} enters the hogwarts express.
		which car do they enter?

		select a car between 1-6.
	'''))
	# first two cars visited
	while visit_tally < 2:
		if action not in range(1,7):
			action = int(input(f'''
***
		sorry, the hogwarts express does not have
		a car {action}. please select a car between
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

		students in car:
		{', '.join(train_dict[action])}

***
		{person.name} decides to visit another car.

		what car do they visit next?
		select a new car between 1-6.
	'''))
			else:
				action = int(input(f'''
***
		{person.name} has already entered that car.

		please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	while action not in cars_unvisited:
		action = int(input(f'''
***
		{person.name} has already entered that car.

		please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	# successfully visit car 3
	cars_unvisited.remove(action)
	visit_tally += 1
	print(f'''
***
		{person.name} enters car {action}.

		students in car:
		{', '.join(train_dict[action])}
	''')
	# trolley witch choice
	time.sleep(1)
	action = input(f'''
***
		as {person.name} leaves car {action}, they
		see a kindly witch pushing a trolley along
		the corridor. the trolley is piled high with
		brightly-colored sweets, decadent pastries,
		and ice-cold drinks.

		'anything off the trolley, dear?'
***
		buy snacks off the trolley? (Y/N)
	''')
	if action.lower() == 'y':
		print(f'''
***
		{person.name} purchases a few snacks and
		continues to walk along the corridor towards
		another car.
	''')
	else:
		print(f'''
***
		{person.name} is tempted by the snacks, but
		ultimately decides against it. they
		continue to walk along the corridor towards
		another car.
	''')	
	action = int(input(f'''
***
		which car does {person.name} enter
		next? select a car number from 1-6 that has
		not yet been visited.
	'''))
	# choosing car 4 and 5
	while visit_tally < 4:
		if action not in range(1,7):
			action = int(input(f'''
***
		sorry, the hogwarts express does not have
		a car {action}. please select another car
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

		students in car:
		{', '.join(train_dict[action])}
***
		{person.name} decides to visit another car.

		what car do they visit next?
		select a new car between 1-6.
	'''))
			else:
				action = int(input(f'''
***
		{person.name} has already entered that car.

		please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	time.sleep(1)
	while action not in cars_unvisited:
		action = int(input(f'''
***
		{person.name} has already entered that car.

		please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	# after car five choice - robes
	visit_tally +=1
	cars_unvisited.remove(action)
	print(f'''
***
		{person.name} enters car {action}.

		students in car:
		{', '.join(train_dict[action])}
	''')
	if 'Robes' in person.inventory:
		print(f'''
***
		as the ride continues, the daylight from
		the windows begins to dim. lanterns are 
		lit along the corridor. {person.name} can hear
		the excited chattering of the other students.

		'We're nearly there!'

		'Must be time to start getting ready.'

		they withdraw the robes carefully packed in 
		their trunk and get dressed. once their hat is
		placed carefully on their head, they decide to
		continue exploring the train.
	''')
	else:
		print(f'''
***
		as the ride continues, the daylight from
		the windows begins to dim. lanterns are 
		lit along the corridor. {person.name} can hear
		the excited chattering of the other students.

		'We're nearly there!'

		'Must be time to start getting ready.'

		as the other students in car {action} begin
		getting dressed, {person.name} is seized with
		panic. they hadn't remembered to purchase robes
		at diagon alley.

		'Do you need to borrow a set of robes?'

		it's {random.choice(train_dict[action])}, one of the students
		in the car. they smile kindly and offer {person.name} a 
		neat set of folded robes.

		'My parents were extra excited about me coming to
		Hogwarts, so they packed me an extra set of everything.
		You can keep these!'
	''')
		person.add_to_inventory('Secondhand Robes')
	# car six choice
	action = int(input(f'''
***
		which car does {person.name} enter next?

		submit a new car number between 1-6.
	'''))
	if action not in range(1,7):
		action = int(input(f'''
***
		sorry, the hogwarts express does not have
		a car {action}. please select another car
		between 1-6 for {person.name} to enter.
	'''))
	else:
		while action not in cars_unvisited:
			action = int(input(f'''
***
		{person.name} has already entered that car.

		please select another car between 1-6
		that {person.name} has not already visited.
	'''))
	print(f'''
***
		{person.name} enters car {action}.

		students in car:
		{', '.join(train_dict[action])}
	''')
	cars_unvisited.remove(action)
	return f'''
***
		trip is over! {person.name} is ready to leave
		the hogwarts express.

		cars left unvisited: {cars_unvisited}
	'''

if __name__ == '__main__':
	h_express_cars = generate_hogwarts_express(test_train_dict, test_student_list)
	user = hpc.Student('Megan')
	print(navigate_hogwarts_express(user, h_express_cars))