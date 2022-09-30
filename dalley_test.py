import hp_items as hpi 
import hp_classes as hpc
from wand_test import choose_wand, wand_options

# test_list = [1, 2, 3, 4, 5, 6, 7, 8]
# test_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
# 			5: 'five', 6: 'six', 7: 'seven', 8: 'eight'}

def say_the_name(name):
	print(f'''
	*
		the name {name}! it worked!
	*''')

def d_alley_get_items(person, test_lst, test_dict):
	numbers_submitted = []
	shops_visited = []
	items_obtained = []
	action = int(input(f'''
***
		hey, submit a number between 1-8, or 0 to exit.

		shops visited: {shops_visited}
	'''))
	while action != 0:
		# non-shop submission
		if action not in list(range(1,9)):
			if action == 111:
				action = int(input(f'''
***
		items purchased: {items_obtained}

		submit a number between 1-8 to visit the shop,
		or 0 to exit.
	'''))
			else:
				action = int(input(f'''
***
		hey, that's not a number between 1-8.

		try again. submit a number between 1-8, or 0 to exit.
		enter '111' to check what you've purchased so far.

		shops visited: {shops_visited}
	'''))
		# shop submissions
		elif action == 5 and action not in numbers_submitted:
			user_wand = choose_wand(person)
			user.get_wand(user_wand)
			numbers_submitted.append(action)
			shops_visited.append((test_lst[action - 1][3:]))
			items_obtained.append(test_dict[action].title())
			action = int(input(f'''
***
		shops visited: {shops_visited}

		submit another number between 1-8, or 0 to exit.
		enter '111' to check what you've purchased so far.
	'''))
		# shops with multiple items
		elif action in [3, 4, 6]:
			if action == 6:
				numbers_submitted.append(6)
				pet_action = input(f'''
***
		welcome to the Magical Menagerie, home of all
		Hogwarts-approved pets!

		Pets available for purchase:
		{', '.join(test_dict[action])}

		select an animal to purchase, or enter '0' to
		return to the shops menu.
	''')
				if pet_action in test_dict[6]:
					items_obtained.append(pet_action.title())
					shops_visited.append((test_lst[5][3:]))
					action = int(input(f'''
***
		congratulations on your new {pet_action}!

		shops visited: {shops_visited}

		submit a number 1-8 to visit, or 0 to exit.
		enter '111' to check what you've purchased so far.
	'''))
				elif pet_action == '0':
					shops_visited.append((test_lst[5][3:]))
					action = int(input('''
***
		no pet selected.

		submit a number 1-8 to visit, or 0 to exit.
	'''))

			print(f'''
		nice choice!''')
			if action not in numbers_submitted and action != 111:
				numbers_submitted.append(action)
				shops_visited.append((test_lst[action - 1][3:]))
				for x in test_dict[action]:
					items_obtained.append(x.title())
			action = int(input(f'''
***
		shops visited: {shops_visited}

		submit another number between 1-8, or 0 to exit.
		enter '111' to check what you've purchased so far.
	'''))
		# shops with one item
		else:
			print(f'''
		nice choice!''')
			if action not in numbers_submitted:
				numbers_submitted.append(action)
				shops_visited.append((test_lst[action - 1][3:]))
				items_obtained.append(test_dict[action].title())
			action = int(input(f'''
***
		shops visited: {shops_visited}

		submit another number between 1-8, or 0 to exit.
		enter '111' to check what you've purchased so far.
	'''))
	if 5 not in numbers_submitted:
		print(f'''
***
		{person.name} cannot leave Diagon Alley without obtaining
		a wand! Heading to Ollivander's...
	''')
		user_wand = choose_wand(person)
		user.get_wand(user_wand)
		numbers_submitted.append(5)
		items_obtained.append(test_dict[5].title())
	person.can_do_magic = False
	return f'''
***
		now leaving Diagon Alley. have a good day!
		items purchased: {items_obtained}
		'''
user = hpc.Student('Megan')

print(d_alley_get_items(user, hpi.year1_dg_alley_shops, hpi.shop_item_dict))
