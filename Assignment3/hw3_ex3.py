# CS152 Spring 2022 
# Lifan Zeng 
# 014172171 
# Homework assignment 3 
# Exercise 3
# 2/12/2022

"""
Exercise 3: 
Using Python list comprehension, implement processing of the following text: 
According to statistics, there are more trees on Earth than there are stars in the Milky Way. 
Today, there are around 3 trillion trees and 400 billion stars.  
You should compute a list that contains only words that are numeric values in the above text. 
Feel free to implement any helper functions for this exercise. At the end print the resulting list as 
follows: 
print(result) 
The expected output is: 
['3', '400'] 
"""

def findNumeric(text_list):
    lst = text_list.split(" ")
    lst2 = []
    i=0
    while i < len(lst):
        if(lst[i].isnumeric()):
            lst2.append(lst[i])
        i = i + 1
    return lst2
        
def main():
    result = findNumeric("According to statistics, there are more trees on Earth than there are stars in the Milky Way. Today, there are around 3 trillion trees and 400 billion stars.")
    print (result)

main() #Call the main function
