# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 1 
# Exercise 5
# 2/8/2022

"""
Exercise 5: 
This exercise will provide you with some practice with object oriented programming in Python. 
In this exercise you will work with a list of Student objects. Class Student is a child of class 
Person. Class Person has the following attributes: 
firstname 
lastname 
age

Class Person also has a method named can_consume_alcohol(), which returns True if the student 
is of legal drinking age (21 years old), and False otherwise. Class Person also has two getters, for 
the first name and the last name.

Class Student inherits from class Person and has the following additional attributes: 
gpa 
status

Class Student has a getter named get_name(), which returns first and last name of the student 
concatenated together.  
Create a list of the following Student objects: 
Mike Smith, 21 yo, 3.7 gpa, Senior status 
Larry Mushroom, 19 yo, 2.1 gpa, Sophomore status
Marry Wolf, 22 yo, 3.2 gpa, Senior status 
Tommy Tree, 20 yo, 3.5 gpa, Sophomore status 
Laura Tall, 21 yo, 3.1 gpa, Junior status 
Amy Paris, 18 yo, 3.9 gpa, Freshman status

Part1: 
Iterate over the list of students and calculate how many are legal to drink alcohol. Output the 
computed value in the following format: 
Out of 6 students 3 are legal to consume alcohol.

Part2: 
Tabulate and output how many students of each status are present in the list. Make sure to sort 
the output by the status. Most convenient way to implement this is with a dictionary. Iterate over 
the list and collect counts of each status representation in a dictionary, then sort this dictionary 
and print out its entries. Your output should look like this: 
Senior 2 
Sophomore 2 
Junior 1 
Freshman 1

Part3: 
Sort your list of students by the gpa (in descending order) and output the students in the new 
sorted list in the following format: 
Amy Paris (3.9) 
Mike Smith (3.7) 
Tommy Tree (3.5) 
Marry Wolf (3.2) 
Laura Tall (3.1) 
Larry Mushroom (2.1)
"""

class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def can_consume_alcohol(self):
        return self.age >= 21

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname


 
class Student(Person):
    def __init__(self, firstname, lastname, age, gpa, status):
        Person.__init__(self, firstname, lastname, age)
        self.gpa = gpa
        self.status = status

    def get_name(self):
        return self.firstname + ' ' + self.lastname


 
        
def main():
    student_list = [Student('Mike', 'Smith', 21, 3.7, 'Senior'), Student('Larry', 'Mushroom', 19, 2.1, 'Sophomore'),
                    Student('Marry', 'Wolf', 22, 3.2, 'Senior'), Student('Tommy', 'Tree', 20, 3.5, 'Sophomore'),
                    Student('Laura', 'Tall', 21, 3.1, 'Junior'), Student('Amy', 'Paris', 18, 3.9, 'Freshman')]

    #Part 1:
    legal_num = 0
    i = len(student_list)-1
    while i >= 0: 
        if student_list[i].can_consume_alcohol():
            legal_num = legal_num + 1
        i = i-1
    print("#Part 1:")
    print("Out of", len(student_list), "students", legal_num, "are legal to consume alcohol")

    #Part 2:
    Senior = 0
    Sophomore = 0
    Junior = 0
    Freshman = 0
    i = len(student_list)-1
    while i >= 0: 
        if student_list[i].status == 'Senior':
            Senior = Senior + 1
        elif student_list[i].status == 'Sophomore':
            Sophomore = Sophomore + 1
        elif student_list[i].status == 'Junior':
            Junior = Junior +1
        else:
            Freshman = Freshman +1
        i = i - 1
    print("\n#Part 2:")
    print("Senior ", Senior, "\nSophomore ", Sophomore, "\nJunior ", Junior, "\nFreshman ", Freshman)

    #Part 3:   
    for j in range(1, 6):           #insertion sort
        key = student_list[j]
        i = j - 1
        while (i >= 0) and (key.gpa > student_list[i].gpa):
            student_list[i+1] = student_list[i]
            i = i - 1
        student_list[i + 1] = key
    print("\n#Part 3:")
    for k in range(6):
        print(student_list[k].get_name(), "(", student_list[k].gpa, ")" )
    
            
main() #Call the main function
