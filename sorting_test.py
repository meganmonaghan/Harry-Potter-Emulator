import hp_items as hpi 
import hp_classes as hpc 
import random
import time

test_student_list = ['Harry Potter', 'Hermione Granger', 'Roonil Wazlib']

def make_student_dict(student_list):
	student_return_dict = {}
	for x in student_list:
		first_name = (x.split()[0])
		student_return_dict[x] = hpc.Student(first_name)
	return student_return_dict

def sort_students(student_list, student_dict):
	for x in student_list:
		(student_dict[x]).sort()

student_object_dict = make_student_dict(hpi.year1_students)
sort_students(hpi.year1_students, student_object_dict)