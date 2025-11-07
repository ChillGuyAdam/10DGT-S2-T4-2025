#Creating a fence - cost calculator
#Author: André Vorster
#Date: 7 November 2025
#Version: 1.1
#Main routine starts here 
keep_going = ""
error = "Please enter an number (also has to be higher than 0)\n" 
width = 0 
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
    length = 0
    while length <= 0: 
        try: 
            length = float(input("\nWhat is your length in metres?:  "))
            if length > 0: 
                print(f"Your length is {length}m")
            else:
                print(error)
        except ValueError: 
            print(error) 
    perimeter = 2 * (width + length) 
    cost_per_meter = 0
    while cost_per_meter <= 0: 
        try: 
            cost_per_meter = float(input(f"\nHow much does it cost per metre of fence?:   $")) 
            if cost_per_meter > 0: 
                print(f"The cost per meter is ${cost_per_meter}")
            else: 
                print(error)
        except ValueError: 
            print(error) 
        
    #Calculate the perimiter of the fence, and how much the total fence costs: 
    total_cost = cost_per_meter * perimeter
    print(f"\nSo with your total perimeter of {perimeter}m and the cost of ${cost_per_meter} per meter of fence,\nthe total cost to fully fence the desired area is ${total_cost}.") 
    keep_going = input("\n\nPlease press <Enter> for another calculation or type\nany key and press enter to close program. ")
print("Thank you for using the calculator!") 