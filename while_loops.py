# Lets cretae a while loop
# keyword break and continue - control the flow of the while loop
# syntax : while variable_name condition value:

# number = 0
#
# while number <10:
#     print("it's working->{}".format(number))
#     if number ==5:
#         break
#     number +=1

# Example - Take user input with while loop

# The user input must have characters for it to run
user_prompt = True
while user_prompt:
    # Ask the user to input their age
    age = input("Please enter your age: ")
    #  isdigit() checks if the input is all digits
    # We must also sanity check the value - it must be less than 117 as humans do not live longer than that.
    if age.isdigit() and int(age) < 117:
        user_prompt=False
    else:
        print("Please provide age in digits: ") # Tells the user to reenter their age.

print("Your age is {}!".format(age))

