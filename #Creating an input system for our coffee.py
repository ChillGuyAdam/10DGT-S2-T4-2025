#Creating an input system for our coffee prgram
#Author: André Vorster
#Date: 10/10/25
#Version: 3.0

#  TODO:Ask the user if they like coffee 
#       Record the answer
#       Give a response back to the answer

#Ask the user if they want coffee
'''LikeCoffee = input("Do you like coffee?       ")
print(f'You answered "{LikeCoffee}".')

if LikeCoffee == "yes" or "Yes" or "YES": 
    print("That is great!I like coffee too!")

else: 
    print("That's ok!")'''

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
        print("I don't understand. Please answer with Yes or No")

