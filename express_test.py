import hp_classes as hpc 
import hp_items as hpi 
import time
import random

test_train_dict = {}
test_student_list = ['Hannah Abbott', 'Terry Boot', 'Vincent Crabbe',
					'Gregory Goyle', 'Draco Malfoy', 'Ron Weasley',
					'Hermione Granger', 'Ernie MacMillan', 'Anthony Goldstein',
					'Susan Bones', 'Lavender Brown', 'Padma Patil',
					'Parvati Patil', 'Pansy Parkinson', 'Seamus Finnegan',
					'Dean Thomas', 'Neville Longbottom', 'Justin Finch-Fletchley']

def generate_hogwarts_express(train_dict, student_list):
	for x in range(1,7):
		students_in_car = []
		for i in range(3):
			student_added = random.choice(student_list)
			students_in_car.append(student_added)
			student_list.remove(student_added)
		test_train_dict[x] = students_in_car
	return train_dict

print(generate_hogwarts_express(test_train_dict, test_student_list))