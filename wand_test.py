import hp_classes as hpc
import hp_items as hpi
import time
import random

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
	time.sleep(1)
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
	time.sleep(1)
	action = input(f'''
***
		'Ah, yes. A {random.choice(wand_options['Wood'])} wand with a {random.choice(wand_options['Core'])}
		core. {random.choice(wand_options['Length'])} inches, {random.choice(wand_options['Flexibility'])}.
		Give it a try, {user.name}.

		'Move the wand around, please.'
	''')
	time.sleep(1)
	action = input(f'''
***
		The wand vibrates slightly, but nothing else happens.

		'No, no, that's not it. I'll just take that one back...
		Select another wand, please.'

		Enter 'select box' to continue.
	''')
	while action.lower() != 'select box':
		action = input('''
***
		'Please select a box so that we may proceed.'

		Enter 'select box' to continue.
	''')
	time.sleep(1)
	action = input(f'''
***
		'Now, this one looks better. Let's see... 
		{random.choice(wand_options['Wood'])}, {random.choice(wand_options['Core'])} core. {random.choice(wand_options['Length'])} inches, and
		{random.choice(wand_options['Flexibility'])}. Wave it for me, if you please.'
	'''	)
	time.sleep(1)
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
	time.sleep(1)
	action = input(f'''
***
		{user.name} opens the box and holds the wand in their hand.

		'A real beauty, this one. {user_wand[0]} wood, with a
		particularly fine {user_wand[1]} core. {user_wand[2]} inches,
		{user_wand[3]}. Try it out.'
	''')
	time.sleep(1)
	print(f'''
***
		At once, a warmth flows from the tips of {user.name}'s fingers
		up through their arm. The {user_wand[0]} wand moves through the
		air, leaving behind an arc of shimmering stars. Ollivander
		watches the stars with satisfaction.

		'Yes, indeed! Very good, very good. And curious...'
	''')
	time.sleep(1)
	print(f''')
		He takes the wand from {user.name} and packs it carefully in
		its box. Ollivander fixes them with his pale stare.

		'I remember every wand I've ever sold. It is curious that you
		should be granted this wand when its brother belonged to the
		greatest -- and darkest -- wizard of all time. I think we must
		expect equally great things from you, {user.name}.'
	''')
	return user_wand

if __name__ == 'main':
	user_name = input('What is your name? ')
	test_user = hpc.Student(user_name)

	test_user.add_to_inventory('Wand', choose_wand(test_user))
	print(test_user.inven())