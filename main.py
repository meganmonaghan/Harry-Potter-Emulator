import hp_classes as hpc
import hp_items as hpi
import time

# test instances
v_dursley = hpc.Muggle('Vernon')
h_potter = hpc.Student('Harry', '')
m_mcgonagall = hpc.Professor('McGonagall', 'Transfiguration')

# magic access - also hogwarts express?
def diagon_alley(char):
	if char.is_magic:
		char.can_do_magic = True
		return f'''
		Tap... tap... tap...
		Welcome to Diagon Alley!
		{char.name} can now perform magic.
		'''
	else:
		return f'{char.name} tapped the brick wall, but nothing happened.'

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
user_name = (input('''
	What is your name? 
	''')).title()
user = hpc.Student(user_name)
time.sleep(2)

# letter_counter = 1
# action = input(f'''
# 	A letter arrives one day, addressed to {user_name}.
# 	Open the letter? (Y/N)
# 	''')

# while action.upper() != 'Y':
# 	letter_counter += 1
# 	action = input(f'''
# 	The next day, {letter_counter} letters arrive, addressed to {user_name}.
# 	Open one of these letters? (Y/N)
# 	''')
# time.sleep(2)
# print(f'''
# 	The letter reads: 

# Dear {user_name}, 
# ''' + hpi.hogwarts_letter)
# time.sleep(2)


# print(diagon_alley(user))
# time.sleep(3)
# print(user.sort())
