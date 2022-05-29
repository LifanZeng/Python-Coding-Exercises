# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 3 
# Exercise 2
# 2/12/2022

"""
Exercise 2: 
Using Python list comprehension, implement computing an intersection between two lists and 
save it in a third list.
Example of your code execution: 
list1 = range(20) 
list2 = range(15, 30,1) 
list3 = [your code goes here] 
print(list3) 
Expected output: 
[15, 16, 17, 18, 19] 
"""

def intersection(lst1, lst2):
    lst3 = []
    for i in lst1:
        if lst1[i] in lst2:
            lst3.append(lst1[i])
    return lst3
        
def main():
    list1 = range(20)
    list2 = range(15, 30, 1)    #range(start, stop, step)
    list3 = intersection(list1, list2)
    print (list3)

main() #Call the main function
