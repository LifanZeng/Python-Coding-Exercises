# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 1 
# Exercise 1
# 2/8/2022

"""
Exercise 1: 
Michael is searching for a job and is applying to various companies. He has some restrictions 
though. He loves the west coast of the US (the states of California, Oregon, Washington) and will 
accept any position that pays over $80,000/year in those states. In order to accept a job in another 
state, he wants an offer of at least least $100,000 a year. He also is not willing to move to some 
states: Arizona, New Mexico, and Texas. It is too hot for his liking in those states. He is not 
willing to accept any offer in those three states.   
Michael wants to automate the process of selecting companies to which he will apply. Your task 
is to help Michael by implementing a function named select_company(state, salary), which 
accepts two input parameters: state and salary the position pays. This function will return either 
true or false, indicating whether Michael should apply to this company or not. Use conditionals 
to implement the logic flow for whether Michael should send in an application for a given 
position.

An example of a using select_company() function: select_company(“California”, 85000) 
And the expected output should be: True 
An example of a using select_company() function: select_company(“New Mexico”, 160000) 
And the expected output should be: False 
An example of a using select_company() function: select_company(“Colorado”, 110000) 
And the expected output should be: True
"""

def select_company(state, salary):
    if (salary <= 80000):
        return False
    elif (salary > 80000 and salary < 100000):
        if (state == "California" or state == "Oregon" or state == "Washington"):
            return True
        else:
            return False
    else:
        if (state == "Arizona" or state == "New Mexico" or state == "Texas"):
            return False
        else:
            return True
        

def main():
    output = select_company("Colorado", 110000)
    print("Michael should apply to this company?", output)


main() #Call the main function
