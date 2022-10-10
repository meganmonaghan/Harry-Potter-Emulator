import hp_items as hpi 
import hp_classes as hpc 
import random
import time

test_student_list = ['Harry Potter', 'Hermione Granger', 'Roonil Wazlib']

def sort_students(student_list, student_dict):
	for x in student_list:
		first_name = (x.split()[0])
		student_dict[x] = hpc.Student(first_name)
		(student_dict[x].sort())
	return student_dict

def return_houses_of_students(student_dict):
	for x in student_dict.keys():
		if student_dict[x].house == 'Gryffindor':
			hpi.Gryffindor.append(x)
		elif student_dict[x].house == 'Hufflepuff':
			hpi.Hufflepuff.append(x)
		elif student_dict[x].house == 'Slytherin':
			hpi.Slytherin.append(x)
		else:
			hpi.Ravenclaw.append(x)
	return f'''
		Gryffindor Students:
		{', '.join(hpi.Gryffindor)}

		Hufflepuff Students:
		{', '.join(hpi.Hufflepuff)}

		Slytherin Students:
		{', '.join(hpi.Slytherin)}

		Ravenclaw Students:
		{', '.join(hpi.Ravenclaw)}
	'''

if __name__ == '__main__':
	user = hpc.Student('Megan')
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
	sort_students(hpi.year1_student_list, hpi.year1_student_dict)
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

	print(return_houses_of_students(hpi.year1_student_dict))