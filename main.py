import hp_classes as hpc
import hp_items as hpi
import time
import sys
import random

# test instances
v_dursley = hpc.Muggle('Vernon')
h_potter = hpc.Student('Harry', '')
m_mcgonagall = hpc.Professor('McGonagall', 'Transfiguration')


# keeps track of "active users"
party = []
party_members = []
def party_add(*args):
	global party
	for x in args:
		if x not in party:
			party.append(x)
			party_members.append(x.name)
			print(f'''
		{x.name} has been added to the party.''')
		else:
			print(f'''
		{x.name} is already in the party.''')
	print('''
		Current party: ''', party_members)

def party_remove(*args):
	global party
	for x in args:
		if x in party:
			party.remove(x)
			party_members.remove(x.name)
			print(f'''
		{x.name} has been removed from the party.''')
		else:
			print(f'''
		{x.name} is not currently in the party.''')
	print('''
		Current party: ''', party_members)


# magic access - also hogwarts express?
def diagon_alley(group):
	for x in group:
		if x.is_magic:
			x.can_do_magic = True
			return f'''
		Tap... tap... tap...
		Welcome to Diagon Alley!
		{x.name} can now perform magic.
			'''
		else:
			return f'{x.name} tapped the brick wall, but nothing happened.'

# for lumos/nox
lights = False

def lumos(char):
	global lights
	if char.can_do_magic and not lights:
		lights = True
		return '''
		~* Lumos! *~
		The lights are now on.
		'''
	elif char.can_do_magic and lights:
		return f'''
		{char.name} cast Lumos, but the lights were already on.
		'''
	else:
		return '''
		Lumos was unsuccessful.
		'''

def nox(char):
	global lights
	if char.can_do_magic and lights:
		lights = False
		return '''
		~* Nox! *~
		The lights are now off.
		'''
	elif char.can_do_magic and not lights:
		return f'''
		{char.name} cast Nox, but the lights were already off.
		'''
	else:
		return '''
		Nox was unsuccessful.
		'''

# harry's true love spell
def expelliarmus(char1, char2):
	if char1.can_do_magic and char2.can_do_magic:
		char2.can_do_magic = False
		return f'''
		~* Expelliarmus! *~
		{char1.name} has disarmed {char2.name}.
		'''
	elif char1.can_do_magic and not char2.can_do_magic:
		return f'''
		{char1.name} cast Expelliarmus, but nothing happened.
		'''
	else:
		return '''
		Expelliarmus was unsuccessful.
		'''


# actual storyline code !!!!
# here we go !!!

# intro/letter
user_name = (input('''
		What is your name? 
	''')).title()
user = hpc.Student(user_name)
print('***')
party_add(user)
time.sleep(1)

print('***')
letter_counter = 1
action = input(f'''
		A letter arrives one day, addressed to {user.name}.
		Open the letter? (Y/N)
	''')

while action.upper() != 'Y':
	letter_counter += 1
	action = input(f'''
***
		The next day, {letter_counter} letters arrive, addressed to {user.name}.
		Open one of these letters? (Y/N)
	''')
time.sleep(1)

print('***')
print(f'''
		The letter reads: 

		Dear {user.name}, 
''' + hpi.hogwarts_letter)
user.add_to_inventory('Supplies Letter', hpi.supplies_letter)
time.sleep(1)

print('***')
action = input('''
		Send return owl? (Y/N)
	''')

if action.upper() != 'Y':
	action2 = input(f'''
***
		If {user.name} doesn't respond to this owl, they may not 
		be able to attend Hogwarts.
		Send return owl? (Y/N)
	''')
	if action.upper() == action2.upper():
			print(f'''
	***
		{user.name} has chosen not to attend Hogwarts.

		Ministry wizards arrive at {user.name}'s home to wipe
		their memory. {user.name} does not remember the owls,
		their letter, or any knowledge of the wizarding world.
		''')
			sys.exit()
time.sleep(1)

# diagon alley block
print('***')
print(f'''
		{user.name} travels to London to buy school supplies
		from Diagon Alley.
		To enter Diagon Alley, tap three bricks.
		\x1B[4m             \x1B[0m
		\x1B[4m| 1 | 2 | 3 |\x1B[0m
		\x1B[4m| 4 | 5 | 6 |\x1B[0m
		\x1B[4m| 7 | 8 | 9 |\x1B[0m
		''')
action = input(f'''
		Which bricks does {user.name} tap? Choose three 
		different numbers (1-9), separated by spaces.
	''')
tap_list = action.split()
tap_list.sort()
hint_count = 0
while tap_list != hpi.tap_solution:
	hint_count +=1
	action = input(f'''
***
		{user.name} taps three bricks, but nothing happens.
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
		{user.name} taps three bricks, but nothing happens.
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
print(diagon_alley(party))
time.sleep(1)

print('***')
print(f'''
		{user.name} has arrived in Diagon Alley!

		Check the user inventory to access the supplies list.
		''')
action = input('''
		Type 'inventory' to access the inventory.
	''')

while action.lower() != 'inventory':
	action = input('''
***
		Please type 'inventory' to access the inventory.
	''')

print(user.inven())
action = input('''
***
		Select the item you would like to access.
	''')

print('***')
print(user.access_item(action))
time.sleep(1)

print('***')
action = input(f'''
		Before going shopping, {user.name} needs money!

		Type 'shops' to see the list of locations available
		in Diagon Alley.
	''')

while action.lower() != 'shops':
	action = input('''
***
		Please type 'shops' to access the list of shops.
	''')

print('***')
print(f'''
		Shops in Diagon Alley:
{', '.join(hpi.year1_dg_alley_shops)}
		''')

# wand selection function
wand_options = hpi.wand_properties
def choose_wand(user):
	global wand_options
	action = input(f'''
***
		'Welcome to Ollivander's Wand Shop. I am
		Ollivander. I believe that the wand chooses the
		wizard, so let us try out a few wands and see
		what chooses you.

		'{user.name}, are you right- or left-handed?'
	''')

	action = input('''
***
		'I see, I see. Let me pull a few boxes and we
		can try them out.'

		Enter 'select box' to continue.
	''')

	while action.lower() != 'select box':
		action = input('''
***
		'Please select a box so that we may proceed.'

		Enter 'select box' to continue.
	''')
	action = input(f'''
***
		'Ah, yes. A {random.choice(wand_options['Wood'])} wand with
		a {random.choice(wand_options['Core'])} core. {random.choice(wand_options['Length'])}
		inches, {random.choice(wand_options['Flexibility'])}.
		Give it a try, {user.name}.

		'Move the wand around, please.'
	''')
	action = input(f'''
***
		The wand vibrates slightly, but nothing else happens.

		'No, no, that's not it. I'll just take that one back...
		Select another wand, please.'

		Enter 'select box' to continue.
	''')
	while action.lower() != 'select box':
		while action.lower() != 'select box':
			action = input('''
***
		'Please select a box so that we may proceed.'

		Enter 'select box' to continue.
	''')
	action = input(f'''
***
		'Now, this one looks better. Let's see... 
		{random.choice(wand_options['Wood'])}, {random.choice(wand_options['Core'])} core. {random.choice(wand_options['Length'])} inches, and
		{random.choice(wand_options['Flexibility'])}. Wave it for me, if you please.'
	'''	)
	action = input(f'''
***
		The wand has barely started to move when Ollivander snatches
		it out of {user.name}'s hand.

		'Absolutely not.'

		He walks around the shelves, talking quietly to himself.

		\x1B[3m'Could it be? I suppose it is possible...'\x1B[0m

		Finally, he pulls a thin, narrow box from a shelf and
		places it on the counter.

		'Open this box, if you please.'

		Open the box to proceed.
	'''	)

	while 'open' not in action:
		action = input(f'''
***
		'We do not have all day, {user.name}. Please open
		the box.'
	''')

	user_wand = tuple((random.choice(wand_options['Wood']),
						random.choice(wand_options['Core']),
						random.choice(wand_options['Length']),
						random.choice(wand_options['Flexibility'])))

	action = input(f'''
***
		{user.name} opens the box and holds the wand in their hand.

		'A real beauty, this one. {user_wand[0]} wood, with a
		particularly fine {user_wand[1]} core. {user_wand[2]} inches,
		{user_wand[3]}. Try it out.'
	''')
	print(f'''
***
		At once, a warmth flows from the tips of {user.name}'s fingers
		up through their arm. The {user_wand[0]} wand moves through the
		air, leaving behind an arc of shimmering stars. Ollivander
		watches the stars with satisfaction.

		'Yes, indeed! Very good, very good. And curious...'

		He takes the wand from {user.name} and packs it carefully in
		its box. Ollivander fixes them with his pale stare.

		'I remember every wand I've ever sold. It is curious that you
		should be granted this wand when its brother belonged to the
		greatest -- and darkest -- wizard of all time. I think we must
		expect great things from you, {user.name}.
	''')
	return user_wand

# gathering items from diagon alley
# THIS DOES NOT WORK YOU NEED TO FIX IT
def diagon_alley_get_items(user, shops):
	shops_visited = []
	while shops_visited.sorted() != range(1,9):
		action = input(f'''
***
		Please select a shop number to visit, or select
		 '0' to leave Diagon Alley.

		NOTE: If you leave Diagon Alley, you cannot return this
		summer. Make sure you have all of your items before 
		leaving!		
	''')
		if action == 0:
			# placeholder code
			return 'Exited function'
		elif action not in range(1,9):
			action = input(f'''
***
		{', '.join(shops)}

		Please select a shop from this list to visit, or
		select '0' to leave Diagon Alley. Only submit a
		number between 1 and 8, with no spaces before or
		after.
	''')
		elif action == 5:
			shops_visited.append(5)		
			user.add_to_inventory('Wand', choose_wand(user))
			shops['\u0336'.join(action) + '\u0336'] = shops.pop(action)
			# test code
			# return shops
		else:
			shops_visited.append(action)
			current_shop = shops[action - 1]
			# placeholder
			return f'current shop: {current_shop}'

print(diagon_alley_get_items(user, hpi.year1_dg_alley_shops)

# print('***')
# print(hpi.september_1)
