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

year1_dg_alley_shops = {'Gringotts Wizarding Bank': 'money',
				'Flourish and Blotts': 'books',
				'Madame Malkin\'s Robes for All Occasions': ['robes', 'cloak', 'gloves'],
				'The Apothecary': ['cauldron', 'phials', 'scales', 'telescope'],
				'Ollivander\'s Wand Shop': 'wand',
				'Magical Menagerie': ['cat', 'owl', 'toad'],
				'Leaky Cauldron': 'butterbeer',
				'Quality Quidditch Supplies': 'broomstick'}

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
		\x1B[3mChoo choo!\x1B[0m
		All aboard the Hogwarts Express!

		At 11:00am sharp, the scarlet steam engine begins to move.
		It begins to gather speed, chugging along, and as it rounds
		the corner, Kings Cross station disappears from view.

		\x1B[3mchug, chug, chug...\x1B[0m

		Hours later, all the students have donned their robes. The
		Howarts Express pulls into Hogsmeade station.
		'''

