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

	def __init__(self, name, house=''):
		self.name = name
		self.house = house

	def greeting(self):
		return f'Hello! My name is {self.name}, and I am a student at Hogwarts.'

	def sort(self):
		self.house = random.choice(houses)
		return f'''
		The Sorting Hat beckons.
		Sorting... sorting...
		Congratulations! {self.name} has been sorted into {self.house}!
		'''

class Professor(Wizard):
	can_do_magic = True

	def __init__(self, name, discipline):
		self.name = name
		self.discipline = discipline

	def greeting(self):
		return f'Hello! My name is Professor {self.name}, and I am the {discipline} professor at Hogwarts.'

	def give_points(self, char, points):
		house_points[char.house] += points
		num = house_points[char.house]
		return f'{char.name} gained {points} points for {char.house}! New total: {num}'

	def take_points(self, char, points):
		house_points[char.house] -= points
		num = house_points[char.house]
		return f'{char.name} lost {points} points for {char.house}. New total: {num}'

house_points = {'Gryffindor': 0,
				'Ravenclaw': 0, 
				'Hufflepuff': 0, 
				'Slytherin': 0}

def display_points(house):
	num = house_points[house]
	return f'{house} has {num} points.'

