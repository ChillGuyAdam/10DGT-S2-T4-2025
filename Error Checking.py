#Error checking 
# Author: André Vorster
#Date: 22nd of October 2025
#Version: 1.0

#Code that tests whether a valid input is given: 
'''done = False #Boolian variable that will help me exit the program 
while not done: 
    num = float(input("Please enter your value:   ")) 
    done = True
print(f"The number that you entered is {num}")''' 


#Code that tests whether a valid input is given (v1.1)
#Use the try and exvept method to catch errors 
'''done = False
while not done: 
    try: #Thise method tries for a valid input
        num = float(input("Please enter your number: ")) 
        done = True
    except ValueError: 
        print("That is not a valid number! Try entering an integer (1,2,3,4,5 etc)\n")

print(f"Then number that you entered is {num}.") '''

#Code that tests whether a valid input is given (v1.2)
#Create a function to call everytime I ask the user
#for a number. A funtion is a chunk of code that does 
#something. 
#Functions can be used over and over again.
#To use a function (call it), write out its name with 
#paranthesis at the end. 
#To create a function, starts with the word def
#(stands for define)
'''def test_int_num(): 
    done = False
    while not done: 
        try: 
            num = int(input("Please enter your number(integer): "))
            done = True
        except ValueError: 
            print("That is not a valid number. Try a integer like 1, 2, 3 etc \n")
            print("Try again")
    
    print(f"The number that you entered is {num}.") 

#Main routine
test_int_num() #This calls the function
'''

#Code that tests wheter a valid input is given (v1.3)
#Use the funciton parameters to make my code more 
#pythonic. 

def test_int(question): # 'question is a place holder
    done = False
    error = "That is not a valid number. Try an integer (Whole number) like 1,2,3 etc"
    while not done: 
        print(question)
        try:
            num = int(input())
            done = True

        except ValueError:
            print(error)
    return(num) # This gives back the value of num 
# so that I can use it outside
#of the function. 

#Main routine
num1 = test_int("please enter your first number:")
print(f"Your first number you entered is {num1}.")

num2 = test_int("Please enter your second number:")
print (f"Your second number you entered is {num2}")



