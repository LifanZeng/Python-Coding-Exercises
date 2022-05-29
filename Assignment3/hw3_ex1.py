# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 3 
# Exercise 1
# 2/12/2022

"""
Exercise 1: 
Using Python list comprehension, implement list conversion from one numeric list to another 
list, which only contains those elements from the first list that are divided by 3 without 
remainder. 
Example of your code execution: 
list1 = range(30) 
list2 = [your code goes here] 
print(list2) 
Expected output: 
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
"""

def conversion(list1):
    list2 = list()
    for i in list1:
        if list1[i] % 3 == 0:
            list2.append(list1[i])
    return list2

def main():
    j=0
    list3 = conversion(range(30))
    print (list3)

main() #Call the main function
    
