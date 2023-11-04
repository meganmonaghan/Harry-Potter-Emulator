import hp_classes as hpc

# TODO: lectures for each subject (levels 1-4)

# questions for each subject and level
level_qs = {
	1 : {1: ('Who is the Charms Professor at Hogwarts?', 'Flitwick'),
		2: ('What does the Wingardium Leviosa charm do?', 'fly'),
		3: ('What is the incantation to make an object fly?', 'Wingardium Leviosa'),
		4: ('Describe the wand movement required to make an object fly.', 'swish and flick'),
		5: ("Who is the author of 'The Standard Book of Spells (Grade 1)'?", 'Goshawk')},
	2: {1: ('Who is the Transfiguration Professor at Hogwarts?', 'McGonagall'),
		2: ('question', 'answer'),
		3: ('question', 'answer'),
		4: ('question', 'answer'),
		5: ('question', 'answer')},
	3: {1: ('Who is the Potions Professor at Hogwarts?', 'Snape'),
		2: ('question', 'answer'),
		3: ('question', 'answer'),
		4: ('question', 'answer'),
		5: ("Who is the author of 'Magical Drafts and Potions?", 'Jigger')},
	4: {1: ('Who is the Defense Against the Dark Arts Professor at Hogwarts?', 'Quirrell'),
		2: ('question', 'answer'),
		3: ('question', 'answer'),
		4: ('question', 'answer'),
		5: ('question', 'answer')},
	5: {1: ('Who is the History of Magic Professor at Hogwarts?', 'Binns'),
		2: ('question', 'answer'),
		3: ('Who is the current Minister for Magic?', 'Fudge'),
		4: ('Which former Durmstrang student was the instigator of the last Wizarding War?', 'Grindelwald'),
		5: ("Who is the author of 'A History of Magic'?", 'Bagshot')}
			}

# eventually - access level per subject for user object
def class_lesson(level, user):
	subject = int(input(f'''
	Please select a subject to study. Enter a
	number, 1-5, or 0 to exit.
	1. Charms, 2. Transfiguration, 3. Potions,
	4. Defense Against the Dark Arts, 5 . History of Magic
'''))
	if subject == 0:
		return f'''
	{user.name} is done studying for today!
	'''
	ques = level_qs[subject][level][0]
	ans = level_qs[subject][level][1]
	user_input = input(f'''
	Level {level}:
	{ques}
''')
	while ans.lower() not in user_input.lower():
		user_input = input(f'''
	I'm sorry, that is not correct. Please try again.
	{ques}
''')
	level = level + 1
	print(f'''
	Congratulations {user.name}! That is correct!
	New level: {level}''')

# option to quit if you get the wrong answer instead of just looping?

megan = hpc.Student('Megan')
print(class_lesson(3, megan))
