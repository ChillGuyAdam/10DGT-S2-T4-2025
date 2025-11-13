#Creating a fence - cost calculator
#Author: André Vorster
#Date: 14 November 2025
#Version: 1.2
#Main routine starts here 

#Creating variables: keep_going to help loop the program at the end and error, so that I can print an error and not use 
#any extra characters than I need to to print error messages. 
keep_going = ""
error = "Please enter an number (also has to be higher than 0)\n" 

width = 0  #takin in the desired width of the user and displaying it. If it doesn't work then print error
while keep_going == "": 
    while width <= 0:
        #get width and height and display it
        try:
            width = float(input("What is your width in metres?:   "))
            if width > 0: 
                print(f"Your width is {width}m") 
            else:
                print(error)
        except ValueError:
            print(error) 
        #looping the length

    length = 0 #taking in the desired length of the user and displaying it. If it doesn't work then print error
    while length <= 0: 
        try: 
            length = float(input("\nWhat is your length in metres?:  "))
            if length > 0: 
                print(f"Your length is {length}m")
            else:
                print(error)
        except ValueError: 
            print(error) 

    perimeter = 2 * (width + length) #calculate the perimeter to print later
    cost_per_meter = 0 #taking in the cost per meter of fence and printing it. Otherwise if something goes wrong
    # print an error message if it doesn't work. 
    while cost_per_meter <= 0: 
        try: 
            cost_per_meter = float(input(f"\nHow much does it cost per metre of fence?:   $")) 
            if cost_per_meter > 0: 
                print(f"The cost per meter is ${cost_per_meter}")
            else: 
                print(error)
        except ValueError: 
            print(error) 
        
    #Calculate the perimeter of the fence, and how much the total fence costs, then printing it and showing the results to the user:  
    total_cost = cost_per_meter * perimeter
    print(f"\nSo with your total perimeter of {perimeter}m and the cost of ${cost_per_meter} per meter of fence,\nthe total cost to fully fence the desired area is ${total_cost}.") 
    #Ask the user if they want another calculation or if they want to stop the program. 
    keep_going = input("\n\nPlease press <Enter> for another calculation or type\nany key and press enter to close program. ")
print("Thank you for using the calculator!") 