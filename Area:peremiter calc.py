#Creating an area and perimiter calculator
#Date: 31 October 2025
#Author: André Vorster
#Version: 1.0

#Creating a function for asking what the width and length is, then displaying it. 
def dimensions(question): 
    repeat = True
    error = "Please give a number above zero."
    while repeat == True: 
        try:
            response = dimensions(float(input(question)))
            return response
        except ValueError:
            print(error)
