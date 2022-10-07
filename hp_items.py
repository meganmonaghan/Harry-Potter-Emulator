hogwarts_letter = '''
		   We are pleased to inform you that you have a place 
		at Hogwarts School of Witchcraft and Wizardry. Please 
		find enclosed a list of all necessary books and 
		equipment.
		   Term begins on 1 September. We await your owl by 
		no later than 31 July.

		Yours sincerely,
		Minerva McGonagall
		Deputy Headmistress
'''

supplies_letter = '''
		REQUIRED MATERIALS:
		3 sets of plain work robes (black)
		1 winter cloak (black, silver fastenings)
		1 wand
		1 cauldron (pewter, standard size 2)
		1 set glass or crystal phials
		1 telescope
		1 set brass scales

		Students may also bring an owl OR a cat OR a toad

		PARENTS ARE REMINDED THAT FIRST YEARS ARE NOT
		ALLOWED THEIR OWN BROOMSTICKS
	'''

tap_solution = ['1', '3', '7']

shop_item_dict = {1: 'money',
				2: 'books',
				3: ['robes', 'cloak', 'gloves'],
				4: ['cauldron', 'phials', 'scales', 'telescope'],
				5: 'wand',
				6: ['cat', 'owl', 'toad'],
				7: 'butterbeer',
				8: 'broomstick'}

year1_dg_alley_shops = ['1. Gringotts Wizarding Bank',
						'2. Flourish and Blotts',
						'3. Madame Malkin\'s Robes for All Occasions',
						'4. The Apothecary',
						'5. Ollivander\'s Wand Shop',
						'6. Magical Menagerie',
						'7. Leaky Cauldron',
						'8. Quality Quidditch Supplies']

wand_properties = {
				'Wood': ['Ash', 'Beech', 'Blackthorn', 'Cedar', 'Cherry',
						'Chestnut', 'Cypress', 'Dogwood', 'Ebony', 'Elder',
						'Elm', 'Fir', 'Hawthorn', 'Hazel', 'Holly',
						'Hornbeam', 'Laurel', 'Maple', 'Pine', 'Poplar',
						'Red Oak', 'Redwood', 'Rowan', 'Spruce',
						'Sycamore', 'Walnut', 'Willow', 'Yew'],
				'Core': ['unicorn hair', 'unicorn hair', 'dragon heartstring',
						'dragon heartstring', 'phoenix feather'],
				'Length': [9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5,
						13, 13.5, 14, 14.5],
				'Flexibility': ['bendy', 'flexible', 'swishy', 'whippy',
						'springy', 'stiff', 'unyielding', 'inflexible', 'rigid']
					}

september_1 = '''
***
		September First, King's Cross Station

		After furtively following a group of people with trunks
		through a solid metal barrier, Platform 9 3/4 has
		materialized into view.

		\x1B[3mChoo choo!\x1B[0m
		All aboard the Hogwarts Express!

		At 11:00am sharp, the scarlet steam engine begins to move.
		It begins to gather speed, chugging along, and as it rounds
		the corner, Kings Cross station disappears from view.

		\x1B[3mchug, chug, chug...\x1B[0m
	'''

year1_student_list = ['Hannah Abbott', 'Susan Bones', 'Terry Boot',
					'Lavender Brown', 'Millicent Bullstrode', 'Michael Corner',
					'Vincent Crabbe', 'Justin Finch-Fletchley', 'Seamus Finnegan',
					'Anthony Goldstein', 'Gregory Goyle', 'Hermione Granger',
					'Daphne Greengrass', 'Neville Longbottom', 'Ernie MacMillan',
					'Draco Malfoy', 'Theodore Nott', 'Pansy Parkinson',
					'Padma Patil', 'Parvati Patil', 'Sally-Anne Perks',
					'Dean Thomas', 'Ron Weasley', 'Blaise Zabini']

year1_student_dict = {}

year1_sorting_hat_song = '''
		\x1B[3mOh, you may not think I'm pretty,
		But don't judge on what you see,
		I'll eat myself if you can find
		A smarter hat than me.
		You may keep your bowlers black,
		Your top hats sleek and tall,
		For I'm the Hogwarts Sorting Hat
		And I can cap them all.
		There's nothing hidden in your head
		The Sorting Hat can't see,
		So try me on and I will tell you
		Where you ought to be!

		You might belong in \033[1mGryffindor\033[0m,
		\x1B[3mWhere dwell the brave of heart,
		Their daring, nerve, and chivalry
		Set Gryffindors apart;
		You might belong in \033[1mHufflepuff\033[0m,
		\x1B[3mWhere they are just and loyal,
		Those patient Hufflepuffs are true
		And unafraid of toil;
		Or yet in wise old \033[1mRavenclaw\033[0m,
		\x1B[3mIf you've a ready mind,
		Where those of wit and learning,
		Will always find their kind;
		Or perhaps in \033[1mSlytherin\033[0m
		\x1B[3mYou'll make your real friends,
		Those cunning folk use any means
		To achieve their ends.

		So put me on! Don't be afraid!
		And don't get in a flap!
		You're in safe hands (though I have none)
		For I'm a Thinking Cap!\x1B[0m
'''

Gryffindor = []
Hufflepuff = []
Ravenclaw = []
Slytherin = []
