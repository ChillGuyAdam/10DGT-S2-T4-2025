#Creating a fence - cost calculator
#Author: André Vorster
#Date: 7 November 2025
#Version: 1.0
#Main routine starts here 
keep_going = ""
error = "Please enter an number (higher than 0)"
width = 0 
while keep_going == "": 
    while width <= 0:
        #get width and height and display it
        try:
            width = float(input("What is your width?:   "))
            if width > 0: 
                print(f"Your width is {width}") 
            else:
                print(error)
        except ValueError:
            print(error) 
        #looping the length
    length = 0
    while length <= 0: 
        try: 
            length = float(input("What is your length?:  "))
            if length > 0: 
                print(f"Your length is {length}")
            else:
                print(error)
        except ValueError: 
            print(error) 
    perimeter = 2 * (width + length) 
    cost_per_meter = float(input(f"How much does it cost per metre of fence?:   ")) 
    #Calculate the perimiter of the fence, and how much the total fence costs: 
    total_cost = cost_per_meter * perimeter
    print(f"So with your total perimeter of {perimeter}m and the cost of ${cost_per_meter} per meter of fence,\n the total cost to fully fence the desired area is ${total_cost}.") 
    keep_going = input("Please press <Enter> for another calculation or type\nany key and press enter to close program. ")