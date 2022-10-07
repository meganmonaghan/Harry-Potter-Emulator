import hp_items as hpi 
import hp_classes as hpc 
import random
import time

test_student_list = ['Harry Potter', 'Hermione Granger', 'Roonil Wazlib']

def make_student_dict(student_list, student_dict):
	for x in student_list:
		first_name = (x.split()[0])
		student_dict[x] = hpc.Student(first_name)
	return student_dict

def sort_students(student_list, student_dict):
	for x in student_list:
		(student_dict[x]).sort()
		student_dict[x]

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

make_student_dict(hpi.year1_student_list, hpi.year1_student_dict)
sort_students(hpi.year1_student_list, hpi.year1_student_dict)
print(return_houses_of_students(hpi.year1_student_dict))