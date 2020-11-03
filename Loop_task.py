# Control Flow Practice Exercise

# Task 1 - Make a loop with a range that says hello 10 times
# Range is used to define a range with a start, stop and step. In this example, the range starts at 0, stops at (but doesn't include) 10 and increments in steps of 1 i.e. 0,1,2,3,4,5...9
for x in range(0,10,1):
     print("Hello")

# Task 2 - Create another loop with a range that asks for names and appends to list_names
list_names=[] # Create an empty list to which we can append
for names in range(0,3,1):
    names=input("Please enter your name: ").title() # Takes user input and capitalises
    list_names.append(names) # Adds name to list_names
print(list_names) # Prints the final list

# Task 3 - Make a loop that iterates over each name in list_name and format's it into lowercase in a new variable called list_names_lower
for names in list_names:
    list_names_lower=names.lower() # Converts all the names back into lower case and stores in a new variable
    print(list_names_lower) # Prints the new variable

# Task 4 - Iterate over the list of values to find if the are even
for numbers in range(1,11,1): # Specifies a range from 0 to 10.
    if numbers%2==0: # The modulus operator can be used to determine whether a number is even as the remainder should be 0.
        print(str(numbers) + " is even") # If the number is even, 'the <number> is even' is printed.
    else:
        print(numbers) # Otherwise, just the number is printed
