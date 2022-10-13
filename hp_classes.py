import random

class Muggle:
	is_magic = False

	def __init__(self, name):
		self.name = name


class Wizard:
	is_magic = True


houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']


class Student(Wizard):
	can_do_magic = False

	# as of 10/2 list, anything that's an item/name pair will be an attribute
	inventory = []

	def __init__(self, name, house='', wand=''):
		self.name = name
		self.house = house
		self.wand = wand

	# def greeting(self):
	# 	return f'Hello! My name is {self.name}, and I am a student at Hogwarts.'

	# sort into house
	def sort(self):
		self.house = random.choice(houses)
		return f'''
***
		'{self.name}!'

		The Sorting Hat beckons. {self.name} approaches and
		sits on the small stool, feeling the eyes of the 
		crowd upon them.

		Sorting... sorting...
		
		'{self.name} has been sorted into...

		{(self.house).upper()}!'
		'''

	# give a wand
	def get_wand(self, wand_item):
		self.wand = wand_item

	# display inventory
	def inven(self):
		return f'''
***
		Inventory:
		{', '.join(self.inventory)}'''


	def add_to_inventory(self, item):
		if item.title() not in self.inventory:
			self.inventory.append(item.title())
			return f'''
***
		{item.title()} has been added to the inventory.'''
			self.inven()


	def access_item(self, item):
		while item.title() not in self.inventory:
			item = input('''
***
		Hmm... that item does not appear to be in your inventory.
		Try again.
	''')
		return item


class Professor(Wizard):
	can_do_magic = True

	def __init__(self, name, discipline):
		self.name = name
		self.discipline = discipline

	def greeting(self):
		return f'Hello! My name is Professor {self.name}, and I am the {discipline} professor at Hogwarts.'

	# points
	def give_points(self, char, points):
		house_points[char.house] += points
		num = house_points[char.house]
		return f'''
***
		{char.name} gained {points} points for {char.house}!
		New total: {num}'
	'''

	def take_points(self, char, points):
		house_points[char.house] -= points
		num = house_points[char.house]
		return f'''
***
		{char.name} lost {points} points for {char.house}.
		New total: {num}'
	'''

	def assign_head(self, house):
			self.house = house

house_points = {'Gryffindor': 0,
				'Ravenclaw': 0, 
				'Hufflepuff': 0, 
				'Slytherin': 0}

def display_points():
	for x in house_points.keys():
		print(f'''
***
		{x} has {house_points[x]} points.
	''')

