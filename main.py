import hp_classes as hpc
import hp_items as hpi
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
print(ext.navigate_hogwarts_express(user, h_express_cars))

# sorting block
print(f'''
***
		{user.name} follows the line of students heading into
		the castle. Once inside, a severe-looking woman with
		her hair pulled back tightly addresses them.

		'Welcome to Hogwarts. In just a moment, you will enter
		the Great Hall and be sorted into your houses. While at
		Hogwarts, your house will be somethting like your family.
		You will take classes with your housemates, live in your
		house dormitories, and gain - or lose - points for your
		house through varies activities.

		'There are four houses at Hogwarts: Gryffindor, Hufflepuff,
		Slytherin, and Ravenclaw.'
	''')
m_mcgonagall = hpc.Professor('McGonagall', 'Transfiguration')
m_mcgonagall.assign_head('Gryffindor')
time.sleep(1)
action = input(f'''
***
		A voice pipes up suddenly from {user.name}'s right.

		'Are you nervous?'

		It's {random.choice(hpi.year1_student_list)}, from the train. The question
		gives {user.name} pause. \x1B[3mAre\x1B[0m they nervous? (Y/N)
	''')
time.sleep(1)
if action.lower() == 'y':
	print(f'''
***
		{user.name} tries to swallow the tight feeling in their
		throat before answering.

		'Yeah, I am. A little.'

		'I am too. Who knows, maybe we'll be in the same house!'

		Before {user.name} can answer, the crowd starts to move. The
		students begin to sort themselves into a single file line,
		and {user.name} can just barely see the front of the line 
		walking throughthe large doors into the Great Hall.
	''')
elif action.lower() == 'n':
	print(f'''
***
		{user.name} is surprised by the question.

		'No, I don't think I am. Haven't really had the time
		to think aobut it - trying to take everything in, you
		know?'

		But as the mass of students begins to assemble into
		a single-file line, approaching the Great Hall, {user.name}
		is suddenly unsure. Was there something to be scared of
		after all?
	''')
else:
	print(f'''
***
		{user.name} considers the question, but ultimately does not
		know what to say. Thankfully, a moment later the crowd
		of students starts to file into the Great Hall, sparing
		them the pressure of answering.
	''')
time.sleep(1)
action = input(f'''
***
		Walking through the doors, the enormity of the Great
		Hall emerges into view. There are candles suspended in
		air, casting a warm, active light over the room. The
		ceiling perfectly reflects the night sky. Smoky-looking 
		clouds swirl and a few stars twinkle weakly.

		The row of students walks down the center of the
		Hall, between two long tables where students are seated.
		Some of them crane their necks to look at the incoming
		line, while others are chatting with their friends. Two
		more tables flank either side, also filled with students.

		At the front of the Hall, there is yet another long table.
		This one is filled with what must be teachers: an earthy-
		looking witch with dirty hands and flyaway hair, a thin
		man with a large turban that overwhelms his skinny frame,
		a sallow-skinned wizard whose hooked nose and lank hair
		looked decidedly unfriendly.

		The severe-looking woman brings out a rickety stool and
		places it on the floor in view of the room. Upon it, she 
		gently puts a ragged and patched hat with a wide brim.

		Take a closer look at the hat.
	''')
print(f'''
***)
		{user.name} is shocked when the brim opens wide, and the
		hat - somehow - begins to sing.
***
	''')
time.sleep(1)
print(hpi.year1_sorting_hat_song)
# other students are sorted
srt.sort_students(hpi.year1_student_list, hpi.year1_student_dict)
# start actual student sorting
time.sleep(1)
action = input(f'''
***
		At the conclusion of the song, the seated students
		and faculty applaud the hat. Professor McGonagall
		approaches the stool with a long scroll.

		'When your name is called, please step forward and
		sit. Once you have been sorted, you will join your
		fellow housemates at your assigned table.'

		{user.name} glances nervously at the nearest table.
		Up close, it's clear that some students are wearing
		the same colors - these colors must be related to 
		their house.

		Enter any letter to continue.
	''')
student1 = random.choice(hpi.year1_student_list)
student2 = random.choice(hpi.year1_student_list)
student3 = random.choice(hpi.year1_student_list)
student4 = random.choice(hpi.year1_student_list)
action = input(f'''
***
		'{student1.split()[1]}, {student1.split()[0]}.'

		There is a small pause at the student walks
		up and sits upon the stool, looking small. The
		hat seems to deliberate for a moment, twitching
		its brim and shifting.

		'{(hpi.year1_student_dict[student1].house).upper()}!'

		Look right to see the {hpi.year1_student_dict[student1].house} table.
	''')
time.sleep(1)
action = input(f'''
***
		{user.name} looks to the right and sees {student1}
		sitting at their new table. The surrounding students
		seem welcoming.

		'{student2.split()[1]}, {student2.split()[0]}.'

		This time, the hat thinks (can a hat think?) for much
		longer. {student2.split()[0]} fidgets on the stool,
		looking petrified. Finally, the hat speaks.

		'{(hpi.year1_student_dict[student2].house).upper()}!'

		{student2.split()[0]} scampers off the stool and to their
		table, nearly tripping on their overlong robes. {user.name}
		wonders how small and nervous they'll look up on the stool.

		'...{user.name}.'

		Maybe the hat will be unable to sort {user.name} at all.
		Could their time at Hogwarts be ended before term has
		even begun?

		{user.name} feels a nudge at their back. It's another
		student from the train, {student3}.

		'She's called your name.'

		Walk towards the hat? (Y/N)
	''')
time.sleep(1)
if action.lower() == 'y':
	print(f'''
***
		{user.name} squares their shoulders, trying to look
		as tall as possible, and cuts through the crowd and up
		towards the stool.
	''')
else:
	print(f'''
***
		Before {user.name} can consciously move themself, the
		crowd seems to move them forward. Suddenly they are
		standing before the stool.
	''')
time.sleep(1)
print(user.sort())
if user.house == 'Gryffindor':
	hpi.Gryffindor.append(user.name)
elif user.house == 'Hufflepuff':
	hpi.Hufflepuff.append(user.name)
elif user.house == 'Slytherin':
	hpi.Slytherin.append(user.name)
else:
	hpi.Ravenclaw.append(user.name)