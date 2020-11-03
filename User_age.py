# Task- Calculating user year of birth


# Part 1
# Define the variables `age` and `name`
age=23
name="Harry"
# Make a calculation for the year in which the person was born
year=2020-23
# Print out "OMG <person>,you are <age> years old so you were born in <year>"
print("OMG {}, you are {} years old so you were born in {}".format(name,age,year))



# Part 2
# Import the datetime library. We will need this to get the the current date and time.
from datetime import datetime
# Prompt the user for input and re-assign the variable `age` and `name`
name=input("Please enter your name: ")
age=int(input("Please enter your age: "))

# It is important to restrict the form of DOB on entry so we can later extract the relevant values.
DOB=input("Please enter your DOB in the format dd-mm-yyyy")

# The year of birth can be calculated by subtracting age from the current datetime
# If the month of birth is greater than or equal to the month now and the day is greater than today, the birthday has not happened.
# Thus, we do not include this year and subtract it.
if int(DOB[3:5])>=datetime.now().month and int(DOB[0:2])>datetime.now().day:
    year_of_birth = datetime.now().year - 1 - age
# Otherwise, we include this year
else:
    year_of_birth = datetime.now().year - age
# Print out the statement.
print("OMG {}, you are {} years old so you were born in {}".format(name.capitalize(),age,year_of_birth))

