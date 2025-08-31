import helper
import re
import pyinputplus as pyip
from datetime import datetime
from helper import *

print ("\nHello. ")

# Start the timer
start_time = default_timer()
current_date_time("\nThis task began at")


# The first 10 digits of pi (π) are 3.1415926535
pi = 3.1415926535
print()
print(f"The first 10 digits of pi (π) are 3.1415926535 ")
print("rounded to 5 decimal places Pi = {:.5f}".format(pi))
print("rounded to 2 decimal places Pi = {:.2f}".format(pi))
print()

# print and input on one line
# print("Hello " + input("What is your name? ") + "!")


first_name = input ("Please enter your first name: ")
last_name = input ("\nPlease enter your last name: ")
# input validation txt@some.domain
email_address = pyip.inputEmail("\nEnter your email address:")
city = input("\nWhat city did you grow up in? ")
pet_name = input("\nEnter the name of an animal or pet? ")

first_name_initial = first_name[0:1]
first_name_initial = get_initial(first_name)
first_name_length = len(first_name)
print("\nHello, " + first_name.capitalize())
print("Your first name has " + str(first_name_length) + " letters")

last_name_initial = last_name[0:1]
last_name_initial = get_initial(last_name)
last_name_length = len(last_name)
print("Your last name has " + str(last_name_length) + " letters")

# use input validation. input must be a number, and must be greater than 0
age = pyip.inputInt("\nand " + first_name.capitalize() + " how old are you? ", min=1)
print()

print (first_name.capitalize(), last_name.capitalize(), 'is' ,int(age), "years old.")
print (f"your initials are, " + first_name_initial.capitalize(), last_name_initial.capitalize())
#print(f'Howdy, ' + first_name_initial,last_name_initial)
#print(f'Today is: ' + str(current_date.day))

print("and your Operating System is " + os_version)
print()

print("Is", city + " " + pet_name, "a cool name for a band?")
# choose from a lettered list
yes_no = pyip.inputMenu(["Yes", "No"], lettered=True, numbered=False)
print("You chose",yes_no)
print("I agree!")

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phone = "an example phone number is 123-456-7890."
result = phoneNumRegex.search(phone)

if result:
    print("\nWarning! a phone number was found!")
    print("The area code is:", result.group()[0:3])
    print("The exchange is:", result.group()[4:7])
    print("The complete phone number is:", result.group())

"""
\n creates a new line before printing 'The current working directory is:'
\n creates a new line before printing the current working directory
"""

print("\nThe current working directory is :\n" + str(cwd))

# Create full path name by joining path and filename
new_file = Path.joinpath(cwd, "new_file.txt")
print("\nFull path:\n" + str(new_file))

# check if a file exists
print("Does this file exist? " + str(new_file.exists()) + "\n")

old_file = Path.joinpath(cwd, "old_file.txt")
print(str(old_file))
print("Does this file exist? " + str(old_file.exists()) + "\n")

current_date_time('This task completed at')
print()

"""
print("Hello"[0])
print("Hello"[-1])

# String
print("123" + "45"6)

# Integer = Whole number
print(123 + 456)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

print(len("0123456789"))
"""

 # Print our timer results
elapsed_time = default_timer() - start_time
# print(f'The operation took {elapsed_time:.2} seconds')

print(f'The operation took {elapsed_time:.4} seconds')


