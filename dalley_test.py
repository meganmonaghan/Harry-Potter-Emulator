import hp_items as hpi
import hp_classes as hpc
from wand_test import choose_wand, wand_options
import time

def d_alley_get_items(person, shop_list, shop_dict):
	formatted_shops = '\n'.join(shop_list)
	numbers_submitted = []
	shops_visited = []
	items_obtained = []
	action = int(input(f'''
***
{formatted_shops}
		
		Please select a shop number to visit, or select
		 '0' to leave Diagon Alley.

		NOTE: If {person.name} leaves Diagon Alley, they cannot
		return this summer. Make sure they have all of their 
		items before leaving!
	'''))
	while action != 0:
		# non-shop submission
		if action not in list(range(1,9)):
			if action == 111:
				time.sleep(1)
				action = int(input(f'''
***
		Items purchased:
		{', '.join(items_obtained)}

		Please select a shop number to visit, or select
		 '0' to leave Diagon Alley.
	'''))
			else:
				action = int(input(f'''
***
		Please only select a shop number between 1-8, or
		select '0' to leave Diagon Alley.
		Enter '111' to check what {person.name} has purchased so far.

		Shops visited: {', '.join(shops_visited)}
	'''))
		# shop submissions
		elif action == 5 and action not in numbers_submitted:
			print(f'''
***
		Now entering Ollivander's Wand Shop...
			''')
			time.sleep(1)
			user_wand = choose_wand(person)
			person.get_wand(user_wand)
			numbers_submitted.append(action)
			shops_visited.append((shop_list[action - 1][3:]))
			items_obtained.append(shop_dict[action].title())
			time.sleep(1)
			action = int(input(f'''
***
{formatted_shops}

		Please select another shop number to visit, or
		select '0' to leave Diagon Alley.
		Enter '111' to check what {person.name} has purchased so far.

		Shops visited: {', '.join(shops_visited)}
	'''))
		# shops with multiple items
		elif action in [3, 4, 6]:
			if action == 6:
				time.sleep(1)
				numbers_submitted.append(6)
				pet_action = input(f'''
***
		Welcome to the Magical Menagerie, home of all
		Hogwarts-approved pets!

		Pets available for purchase:
		{', '.join(shop_dict[action])}

		Select an animal to purchase, or enter '0' to
		return to the shops menu.
	''')
				if pet_action in shop_dict[6]:
					time.sleep(1)
					items_obtained.append(pet_action.title())
					if action not in numbers_submitted:
						shops_visited.append((shop_list[5][3:]))
					action = int(input(f'''
***
		Congratulations on your new {pet_action}!

{formatted_shops}

		Please select another shop number to visit, or
		select '0' to leave Diagon Alley.
		Enter '111' to check what {person.name} has purchased so far.

		Shops visited: {', '.join(shops_visited)}
	'''))
				elif pet_action == '0':
					time.sleep(1)
					shops_visited.append((shop_list[5][3:]))
					action = int(input(f'''
***
		No pet selected.

{formatted_shops}

		Please select another shop number to visit, or
		select '0' to leave Diagon Alley.
		Enter '111' to check what {person.name} has purchased so far.

		Shops visited: {', '.join(shops_visited)}
	'''))
			else:
				if action not in numbers_submitted and action != 111:
					numbers_submitted.append(action)
					shops_visited.append((shop_list[action - 1][3:]))
					for x in shop_dict[action]:
						items_obtained.append(x.title())
				time.sleep(1)
				action = int(input(f'''
***
		{person.name} enters {shop_list[action-1][3:]} and 
		purchases their necessary items.

***
{formatted_shops}

		Please select another shop number to visit, or
		select '0' to leave Diagon Alley.
		Enter '111' to check what {person.name} has purchased so far.

		Shops visited: {', '.join(shops_visited)}
	'''))
		# shops with one item
		else:
			if action not in numbers_submitted:
				numbers_submitted.append(action)
				shops_visited.append((shop_list[action - 1][3:]))
				items_obtained.append(shop_dict[action].title())
			time.sleep(1)
			action = int(input(f'''
***
		{person.name} enters {shop_list[action-1][3:]} and 
		purchases their necessary items.

***
{formatted_shops}

		Please select another shop number to visit, or
		select '0' to leave Diagon Alley.
		Enter '111' to check what {person.name} has purchased so far.

		Shops visited: {', '.join(shops_visited)}
	'''))
	if 5 not in numbers_submitted:
		time.sleep(1)
		print(f'''
***
		{person.name} cannot leave Diagon Alley without obtaining
		a wand! Heading to Ollivander's...
	''')
		time.sleep(1)
		user_wand = choose_wand(person)
		person.get_wand(user_wand)
		numbers_submitted.append(5)
		items_obtained.append(shop_dict[5].title())
	person.can_do_magic = False
	time.sleep(3)
	for item in items_obtained:
		person.add_to_inventory(item)
	return f'''
***
		As {person.name} finishes up their school shopping, they
		take one last look around at the bustling street. To think,
		in only a few weeks, their life at Hogwarts would begin...
		'''

if __name__ == '__main__':
	user = hpc.Student('Megan')

	print(d_alley_get_items(user, hpi.year1_dg_alley_shops, hpi.shop_item_dict))
	print(user.inven())
