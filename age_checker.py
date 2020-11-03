# First we take the user's age
age=int(input("Please enter your age: "))

# Control Flow is as follows.
# If the user is 18 or over, they can watch any movie.
if age>=18:
    print("Congratulations, you may watch any movie")
# If the user is 15 or over, they can watch any movie rated 15,12,PG or U
elif age>=15:
    print("You may watch a movie rated 15, 12, PG or U ")
# If the user is 12 or over, they can watch any movie rated 12,PG or U
elif age>=12:
    print("You may watch a movie rated 12 or U ")
# If the user is 10 or over, they can watch any movie rated PG or U
elif age>=10:
    print("You may watch a movie rated PG or U")
# If the user younger than 10, they can watch a movie rated U.
elif age<10:
    print("You may watch a U movie")


