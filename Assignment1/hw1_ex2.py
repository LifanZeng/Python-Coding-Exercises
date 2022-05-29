# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 1 
# Exercise 2
# 2/8/2022

"""
Exercise 2: 
Implement a function to compute cumulative sum of the values in numeric list. Name your 
function cum_sum(lst, limit), with two input parameters: lst is the list of numeric values, limit 
indicates up to which element in the list the sum is computed. Parameter limit should be optional 
and, if not specified, then the entire list should be used. The result should be returned from the 
function.

An example of a using cum_sum() function: cum_sum(range(10)) 
And the expected output should be: 45 
An example of a using cum_sum() function: cum_sum(range(10), 4) 
And the expected output should be: 6
"""

def cum_sum(lst, limit=0):                  # If only input one parameter lst, set the default value limit=0
    if limit==0:
        return sum(lst)
    else:
        list1=[x for x in lst if x<limit]   # If input two parameter, set the limitation for the list.
        return sum(list1)
    
def main():
    output = cum_sum(range(10))
    print("The sum is: ", output)


main() #Call the main function
