# ask user for their age
print("Please enter your age")

# Read the user's response
age = int(input())

# check if the user is an adult abd display correct message
if age >= 18:
    print("You are an adult")
    print("because you are older than 18 years old")
elif age >= 13:
    print("You are a teenager")
    print("because you are 13 or above")

else:
    print("You are not a child")
    print("because you are below the age of 13")
print()
print("End of program")
