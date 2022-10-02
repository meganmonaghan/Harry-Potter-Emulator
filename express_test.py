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

def generate_hogwarts_express(train_dict, student_list):
	for x in range(1,7):
		students_in_car = []
		for i in range(3):
			student_added = random.choice(student_list)
			students_in_car.append(student_added)
			student_list.remove(student_added)
		test_train_dict[x] = students_in_car
	return train_dict

def navigate_hogwarts_express(person, train_dict):
	cars_visited = []
	visit_tally = 0
	action = int(input(f'''
***
		{person.name} enters the hogwarts express.
		which car do they enter?

		select a car between 1-6.
	'''))
	while visit_tally < 3:
		if action not in cars_visited:
			visit_tally += 1
			cars_visited.append(action)
# 			print(f'''
# ***
# 		{person.name} enters car {action}.

# 		students in car:
# 		{', '.join(train_dict[action])}
# ''')
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
		print = (f'''
***
		{person.name} purchases a few snacks and
		continues to walk along the corridor towards
		another car.
	''')
	else:
		print = (f'''
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
	while visit_tally < 5:
		if action not in cars_visited:
			visit_tally += 1
			cars_visited.append(action)
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
	return f'''
***
		trip is over! {person.name} is ready to leave
		the hogwarts express.

		cars visited: {cars_visited}
	'''

if __name__ == '__main__':
	h_express_cars = generate_hogwarts_express(test_train_dict, test_student_list)
	user = hpc.Student('Megan')
	print(navigate_hogwarts_express(user, h_express_cars))