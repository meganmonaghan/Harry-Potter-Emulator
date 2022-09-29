import hp_items as hpi 
import hp_classes as hpc

# test_list = [1, 2, 3, 4, 5, 6, 7, 8]
# test_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
# 			5: 'five', 6: 'six', 7: 'seven', 8: 'eight'}

def say_the_name(name):
	print(f'''
	*
		the name {name}! it worked!
	*''')

def test_the_loop(name, test_lst, test_dict):
	numbers_submitted = []
	shops_visited = []
	items_obtained = []
	action = int(input(f'''
***
		hey, submit a number between 1-8, or 0 to exit.

		shops visited: {shops_visited}
	'''))
	while action != 0:
		if action not in list(range(1,9)):
			action = int(input(f'''
***
		hey, that's not a number between 1-8.

		try again. submit a number between 1-8, or 0 to exit.

		shops visited: {shops_visited}
		items obtained: {items_obtained}
	'''))
		elif action == 5 and action not in numbers_submitted:
			say_the_name(name)
			numbers_submitted.append(action)
			shops_visited.append(test_lst[action - 1])
			items_obtained.append(test_dict[action])
			action = int(input(f'''
***
		shops visited: {shops_visited}
		items obtained: {items_obtained}

		submit another number between 1-8, or 0 to exit.
	'''))
		else:
			print(f'''
		nice choice!''')
			if action not in numbers_submitted:
				numbers_submitted.append(action)
				shops_visited.append(test_lst[action - 1])
				items_obtained.append(test_dict[action])
			action = int(input(f'''
***
		shops visited: {shops_visited}
		items obtained: {items_obtained}

		submit another number between 1-8, or 0 to exit.
	'''))
	return f'''
***
		now leaving the loop. have a good day!
		items obtained: {items_obtained}
		'''
user = hpc.Student('Megan')

print(test_the_loop(user.name, hpi.year1_dg_alley_shops, hpi.shop_item_dict))	