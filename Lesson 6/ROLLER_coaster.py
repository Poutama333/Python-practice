# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
print("Roller coaster!")
vippass = input("Do you have a VIP pass?(yes/no)").lower()
if vippass == "yes":
    print("Welcome, you're allowed on the ride!")

else:
    age = int(input("How old are you? "))
    height = float(input("How tall are you?(in cm)"))
    heart = input("Do you have any heart conditions? (yes/no)")
    if age > 10 and height > 150 and heart == "yes":
        print("Great, you're allowed on the ride")
    else:
        print("Sorry, you aren't allowed on this ride")
        






# Check conditions and output verdict




# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient