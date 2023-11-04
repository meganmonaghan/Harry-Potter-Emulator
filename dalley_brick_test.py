import hp_classes as hpc
import hp_items as hpi

def enter_d_alley(person, solution):
	print('***')
	print(f'''
		{person.name} travels to London to buy school supplies
		from Diagon Alley.
		To enter Diagon Alley, tap three bricks.
		\x1B[4m             \x1B[0m
		\x1B[4m| 1 | 2 | 3 |\x1B[0m
		\x1B[4m| 4 | 5 | 6 |\x1B[0m
		\x1B[4m| 7 | 8 | 9 |\x1B[0m
	''')
	action = input(f'''
		Which bricks does {person.name} tap? Choose three 
		different numbers (1-9), separated by spaces.
	''')
	tap_list = action.split()
	tap_list.sort()
	hint_count = 0
	while tap_list != solution:
		hint_count +=1
		action = input(f'''
***
		{person.name} taps three bricks, but nothing happens.
		Try again.
		\x1B[4m             \x1B[0m
		\x1B[4m| 1 | 2 | 3 |\x1B[0m
		\x1B[4m| 4 | 5 | 6 |\x1B[0m
		\x1B[4m| 7 | 8 | 9 |\x1B[0m

		Choose three numbers (1-9) separated by spaces.
		Note: the order of the bricks doesn't matter!
	''')
		tap_list = action.split()
		tap_list.sort()
		if hint_count == 2:
			action = input(f'''
***
		{person.name} taps three bricks, but nothing happens.
		Try again.
		\x1B[4m             \x1B[0m
		\x1B[4m| 1 | 2 | 3 |\x1B[0m
		\x1B[4m| 4 | 5 | 6 |\x1B[0m
		\x1B[4m| 7 | 8 | 9 |\x1B[0m
		
		Choose three numbers (1-9) separated by spaces.
		Hint: try some of the corner bricks!
	''')
			tap_list = action.split()
			tap_list.sort()
	print('***')
	return solution

if __name__ == '__main__':
	user = hpc.Student('Megan')

	print(enter_d_alley(user, hpi.tap_solution))