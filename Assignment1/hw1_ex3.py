# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 1 
# Exercise 3
# 2/8/2022

"""
Exercise 3: 
Implement a function that computes factorial without utilizing recursion. Use a loop to compute 
factorial of a given number. Name your function factorial(n), where n is the input parameter 
indicating a number for which to compute the factorial. Make sure to account for negative 
numbers in your input. Return -1 for any invalid input. The result should be returned from the 
function.

An example of a using factorial() function: factorial(5) 
And the expected output should be: 120 
An example of a using factorial() function: factorial(-5) 
And the expected output should be: -1 
"""

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
    output = factorial(5)
    print("The factorial is: ", output)


main() #Call the main function
