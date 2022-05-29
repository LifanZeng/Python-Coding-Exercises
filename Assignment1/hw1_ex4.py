# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 1 
# Exercise 4
# 2/8/2022

"""
Exercise 4: 
This exercise is an extension of the previous exercise. Write a function named 
multiple_factorials(n), where n is the maximum number for which the factorial is computed. A 
factorial should also be computed for each value less than n. The function does not return any 
value but instead print the result of each factorial computation on a separate line, starting from 
the largest number and going down to the output for factorial for 1. For any invalid input n the function should print “ERROR: invalid input”. In this exercise you should utilize the function 
you wrote for the previous exercise.  
An example of a using factorial() function: multiple_factorials(10) 
And the expected output should be: 
3628800 
362880 
40320 
5040 
720 
120 
24 
6 
2 
1 
An example of a using factorial() function: multiple_factorials(0) 
And the expected output should be: 
ERROR: invalid input
"""

def multiple_factorials(m):
    j=m
    while j>0:
        print(factorial(j))
        j=j-1
    
            
def factorial(n):
    f=1
    if n<0:
        return -1
    elif n==0:
        return 0
    else:
        for i in range(1, n+1):
            f = f * i
        return f
    
def main():
    multiple_factorials(10)
    
main() #Call the main function
