transfig_qs = {1: ('Who is the Transfiguration Professor at Hogwarts?', 'McGonagall'),
			2: ('question', 'answer'),
			3: ('question', 'answer'),
			4: ('question', 'answer'),
			5: ('question', 'answer')}

charms_qs = {1: ('Who is the Charms Professor at Hogwarts?', 'Flitwick'),
			2: ('question', 'answer'),
			3: ('question', 'answer'),
			4: ('question', 'answer'),
			5: ("Who is the author of 'The Standard Book of Spells (Grade 1)'?", 'Goshawk')}

potions_qs = {1: ('Who is the Potions Professor at Hogwarts?', 'Snape'),
			2: ('question', 'answer'),
			3: ('question', 'answer'),
			4: ('question', 'answer'),
			5: ('question', 'answer')}

dada_qs = {1: ('Who is the Defense Against the Dark Arts Professor at Hogwarts?', 'Quirrell'),
			2: ('question', 'answer'),
			3: ('question', 'answer'),
			4: ('question', 'answer'),
			5: ('question', 'answer')}

history_qs = {1: ('Who is the History of Magic Professor at Hogwarts?', 'Binns'),
			2: ('question', 'answer'),
			3: ('question', 'answer'),
			4: ('question', 'answer'),
			5: ('question', 'answer')}

user_input = input(f'''
	{charms_qs[5][0]}
''')
while (charms_qs[5][1]).lower() not in user_input:
	user_input = input(f'''
	I'm sorry, that is not correct. Please try again.
	{charms_qs[5][0]}
''')
print('''
	Congratulations! That is correct!''')