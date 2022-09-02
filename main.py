import hp_classes as hpc
import hp_items as hpi
import time
import sys

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

# actual storyline code
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
time.sleep(1)

print('***')
action = input('''
		Send return owl? (Y/N)
	''')

return_counter = 1
while action.upper() != 'Y':
	return_counter +=1
	action = input(f'''
***
		If {user.name} doesn't respond to this owl, they may not 
		be able to attend Hogwarts.
		Send return owl? (Y/N)
	''')
	if return_counter == 3:
		print(f'''
***
		{user.name} has chosen not to attend Hogwarts.

		Ministry wizards arrive at {user.name}'s home to wipe
		their memory. {user.name} does not remember the owls,
		their letter, or any knowledge of the wizarding world.
		''')
		sys.exit()


print('***')
print(f'''
		{user.name} travels to London to buy school supplies
		from Diagon Alley.
		To enter Diagon Alley, tap three bricks.
		''')
action = input(f'''
		Which bricks does {user.name} tap? Choose three 
		different numbers (1-10), separated by spaces.
	''')
tap_list = action.split()
tap_list.sort()

while tap_list != hpi.tap_solution:
	action = input(f'''
		{user.name} taps three bricks, but nothing happens.
		Try again.
		Choose three numbers (1-9) separated by spaces.
		Note: the order of the bricks matter!
	''')
	tap_list = action.split()


print('***')
print(diagon_alley(party))
time.sleep(1)

# print('***')
# print(hpi.september_1)
# # print(user.sort())
