# For loops - Practice
shopping_list=["eggs","milk","supermalt"]

# This for loop iterates through shopping_list and for every item, it prints it.
for items in shopping_list:
    print(items)

# We can now introduce control flow as a nested loop. If this condition is met, the for loop acts.
# In this example, if the item is milk, the item will be printed.
for items in shopping_list:
    if items=="milk":
        print(items)

# This is a dictionary which we can apply control flow to
my_details={
    "Full Name":"Jane Doe",
    "DOB":" 00-00-0000",
    "Address":"100 Generic Lane, NO9 W34",
    "Course":"DevOps",
    "Grades":66,
    "Hobbies":["Hiking","Murder Mystery","Baking"]
}

# The for loop iterates through all items in the dictionary and prints the key and value.
for items,values in my_details.items():
   print(items + ": " + str(values))

# The break keyword can be used to stop the loop. In this example, if milk is present the loop will break so no output will be shown in the console
for items in shopping_list:
    if items=="milk":
        break
# Likewise the continue keyword can be used to continue the loop.
for items in shopping_list:
    if items=="milk":
        continue





