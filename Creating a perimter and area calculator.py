#Creating an area and perimter calculator
#Date: 4 November 2025
#Author: André Vorster
#Version: 2.1

#Creating a function for asking what the width and length is, then displaying it. 

error = "Please enter a number that is more than zero."
loop = ""
while loop == "": 
    try:
        width = float(input("What is your width?"))
        if width > 0:
            print(f"Your width is {width}.") 
            
        else: 
            print(error)

        length = float(input("What is your length?"))
        if length > 0:
            print(f"Your length is {length}")
            perimeter = length + width 
            area = length * width 
            print(f"\n The perimeter is {perimeter} and the area is {area}")
            
        else: 
            print(error)
        loop = input("Would you like to repeat the program, if yes press enter. If no press any key> ")
    except ValueError:
        print(error) 



 

    