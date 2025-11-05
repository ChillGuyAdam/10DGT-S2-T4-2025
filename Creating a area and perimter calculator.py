#Creating an area and perimter calculator
#Date: 4 November 2025
#Author: André Vorster
#Version: 3.1

#Creating a function for asking what the width and length is, then displaying it. 

error = "Please enter a number that is more than zero."
loop = ""
print("This is a area and a perimeter calculator, the calculator will ask you for the width and length, \n when you fill them in make sure that you put numbers above zero. :)\n\n\n" )
while loop == "":  
    try:
        width = 0 
        while width <= 0: 
            width = float(input("What is your width?  "))
            print(error)
        print(f"Your width is {width}.")  

        length = 0 
        while length <= 0: 
            length = float(input("What is your length?  "))
            print(error)
        print(f"Your length is {length}") 
        
        perimeter = 2 * (length + width)
        area = length * width 
        print(f"\n The perimeter is {perimeter} and the area is {area}")
    
        loop = input("Would you like another calculation, if yes press enter. If no, type No and enter.")
    except ValueError:
        print(error) 