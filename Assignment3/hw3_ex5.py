# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 3 
# Exercise 5
# 2/12/2022

"""
Exercise 5: 
In this exercise let’s practice closures in Python. Implement an outer function named 
make_multiplier(factor), where factor is the factor by which to multiply a given value. The inner 
function should return a value multiplied by that factor.
Part1: 
For part 1, simply create closures named doubler and trippler create multiplier factories by 2 and 
3 correspondingly. Print the output of the doubler and trippler variables using value 3. 
Example of your code execution: 
doubler = make_multiplier(2) 
trippler = make_multiplier(3) 
print(doubler(3)) 
print(trippler(3)) 
The expected output is: 
6 
9 
Part2: 
For part 2, you will work with your implementation of make_multiplier() from part 1. Now use 
list comprehension to create a list of functions that multiply some value by a given factor. Simply 
use range(1,11,1) to create a list of factors. Your list of functions will contain functions as its 
elements, each function uses different factor to multiply a given value. Then use another list 
comprehension line of code to print values returned by these functions for values 3, 4, 5, and 6. 
In other words, the result of using the list of functions on each of these values should be another 
list.  
Example of your code execution: 
multiplier_list = [ your code goes here ] 
result3 = [ your code goes here ] 
result4 = [ your code goes here ] 
result5 = [ your code goes here ] 
result6 = [ your code goes here ] 
print(result3) 
print(result4) 
print(result5) 
print(result6) 
The expected output of using multiplier_list to make a list of results : 
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30] 
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40] 
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60] 
"""

def make_multiplier(factor):        #Part 1:
    def inner(n):
        return n * factor
    return inner

def multiplier_list(factor,range_lst):  #Part 2:
    result = make_multiplier(factor)
    i=0
    lst = list(range_lst)
    while i < len(lst):
        lst[i] = result(lst[i])
        i = i + 1
    return lst
    
    
def main():
    #part 1:
    doubler = make_multiplier(2)
    trippler = make_multiplier(3) 
    print(doubler(3)) 
    print(trippler(3))

    #part 2:
    range_list = range(1,11,1)
    result3 = multiplier_list(3,range_list)
    result4 = multiplier_list(4,range_list)
    result5 = multiplier_list(5,range_list)
    result6 = multiplier_list(6,range_list)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    
main() #Call the main function
