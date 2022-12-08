import hp_classes as hpc
import hp_items as hpi 
import random
import time

class CourseNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

course_levels = [1, 2, 3, 4, 5]
course_linked_list = []
