print("Please enter the first number.")
first_number = int(input())

print("Please enter the second number.")
second_number = int(input())

# Determine which message to display
if first_number < second_number:
    print("The first number is the smallest.")
elif first_number > second_number:
    print("The second number is the small est.")
else:
    print("The two numbers are equal.")