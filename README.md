# Control Flow
## If statements, else, elif
If statements evaluate a condition and perform an action if True. They follow the syntax:

```
if <condition>:
    <action>
```


## For loops
For loops iterate through data and complete an action provided the condition is satisfied. The syntax is as follows:
```
for variable in <data_collection>:
    <action>
```


## While Loops
* While loops are executed when a certain condition is True.

* They will continue to execute until the condition has been met.
* They are typically used for monitoring purposes.
* The ```break``` and ```continue``` keywords are important in while loops as they help control the flow of the loop. 
* The syntax is as follows:
```
while <condition> is True:
    <action>
```
### Why do we have while loops if we have for loops?
For loops only loop for amount of data in a loop
whereas while loops continue looping until a certain condition is met.
### Example - Take user input with while loop

1. The user input must have characters for it to run.
2. While this is True, we cn ask the user to input their age.
3. We must then sanity check. The ```isdigit()``` command checks if the input is all digits. This ensures the input is not characters. We must also check that the value is realistic i.e less than 117 as humans cannot be older than that.
4. If the sanity checks fail, the user_prompt is False so the user is asked to re-input their age. This will continue until user_prompt is True. 
5. The age is then printed to the console
```python
user_prompt = True
while user_prompt:
    # Ask the user to input their age
    age = input("Please enter your age: ")
    #  sanity checks, if failed, user_prompt becomes False.
    if age.isdigit() and int(age) < 117:
        user_prompt=False
    else:
        print("Please provide age in digits: ") # Tells the user to reenter their age.

print("Your age is {}!".format(age))

```
