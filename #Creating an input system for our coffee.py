#Creating an input system for our coffee prgram
#Author: André Vorster
#Date: 17/10/25
#Version: 4.0 

#  TODO:Ask the user if they like coffee 
#       Record the answer
#       Give a response back to the answer

#Ask the user if they want coffee
'''LikeCoffee = input("Do you like coffee?       ")
print(f'You answered "{LikeCoffee}".')

if LikeCoffee == "yes" or "Yes" or "YES": 
    print("That is great!I like coffee too!")

else: 
    print("That's ok!")

#Version 2
#While loop
keepGoing = ""
while keepGoing == "": 
    likeCoffee = input("Do you like coffee? ")

    if likeCoffee == "Yes": 
        print("That is great! I like coffee too!")
        keepGoing = "Finished"

    elif likeCoffee == "No":
        print("That's ok!")
        keepGoing = "Finished"
    else: 
        print("I don't understand. Please answer with Yes or No")'''

#Version 4
#Making the program more pythonic

keep_going = ""
while keep_going == "":
    #Convert answer to lower case using .lower()
    like_coffee = input("Do you like coffee?  ").lower()
    if like_coffee == "yes" or like_coffee == "y": 
        print("That's great")

    elif like_coffee == "no" or like_coffee == "n":
        print("Thats too bad!") 

        like_tea = input("Do you like tea instead? ").upper() #convert input into an upper case using .upper()
        if like_tea == "YES" or like_tea == "Y": 
            print("Good for you")

        elif like_tea == "NO" or like_tea == "N": 
            print("well dang")
    #Error message
    else: 
        print("I dont understand. Please answer with either Yes or No.")

    keep_going = input("Press any key and say enter to close program.")
        
