# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 3 
# Exercise 4
# 2/12/2022

"""
Exercise 4: 
Use a lambda function for this exercise. Utilize map() Python function to implement a mapping 
for a list of integers to produce a new list in which each element is the result of the following 
functions for each corresponding element in the original list:
    y = x^4 - 4x^3 + 6x^2 - 4x + 1


Example of your code execution: 
orig_list = range(10) 
new_list = list( map( mapping of the original list to the function above ) ) 
print(new_list) 
"""

def mapping(lst):
    list1 = map(lambda x: x**4 - 4 * x**3 + 6 * x**2 - 4 * x + 1, lst)
    return (list(list1))
           
def main():
    orig_list = range(10)
    new_list = mapping(orig_list)
    print(new_list)
    
main() #Call the main function
