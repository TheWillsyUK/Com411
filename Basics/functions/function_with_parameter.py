# The function with a single parameter named 'Plan'
def escape_by(plan):
    # Determine which message to display
    if plan == "Jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "Running around":
        print("We cannot escape that way! The boulder is moving too fast")
    elif plan == "Going deeper":
        print("That might just work! Let's go deeper")
    else:
        print("Not sure about the plan!")


# Calls to the function
escape_by("Jumping over")
escape_by("Running around")
escape_by("Going deeper")
