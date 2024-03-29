import hp_classes as hpc
import hp_items as hpi
import dalley_brick_test as dbt
import dalley_test as dat
import express_test as ext
import sorting_test as srt
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
user.add_to_inventory('Supplies Letter')
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
dbt.enter_d_alley(user, hpi.tap_solution)
time.sleep(1)

print(diagon_alley(party))
time.sleep(1)

print(f'''
***
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

print(f'''
***
		{hpi.supplies_letter}
	''')
time.sleep(1)

action = input(f'''
***
		Before going shopping, {user.name} needs to
		know where to go!

		Type 'shops' to see the list of locations available
		in Diagon Alley.
	''')

while action.lower() != 'shops':
	action = input('''
***
		Please type 'shops' to access the list of shops.
	''')
# diagon alley item purchasing
print(dat.d_alley_get_items(user, hpi.year1_dg_alley_shops, hpi.shop_item_dict))

# september first woooo
time.sleep(1)
print(hpi.september_1)

h_express_cars = ext.generate_hogwarts_express(ext.express_dict, hpi.year1_student_list)
ext.navigate_hogwarts_express(user, h_express_cars)

# sorting block
srt.sorting_block(user)