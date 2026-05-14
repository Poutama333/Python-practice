### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item
print("Budget tracker")
# Create a constant to hold your budget
# Create a constant to hold your savings (percentage) goal
BUDGET = int(input("How much money do you have(in dollars)"))
# Ask user for item name and save in variable
item = input("What would you like to buy? ")
# Ask user for cost and save in variable
cost = int(input("How much does it cost? "))

# Change the cost into an integer

# Calculate the percentage of budget (cost / budget) * 100
percent = int((cost/BUDGET)*100)
# Tell your user the percentage of your budget
print("The",item,"costs",percent,"percent of your budget")
# Check if percentage is 0 and say it's free if it is
if percent == 0:
    print("The",item,"is free")
# Check if the percentage is less then 10 and say it's a small treat so enjoy
elif percent <= 10:
    print("Thats a small treat, enjoy")
# Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it
elif percent <= 50:
    print("It's a major spend, you should sleep on it")
# Check if it's over 100 and if it is tell them they don't have enough money
elif percent >= 100:
    print("You can't afford that broke boy.")
# Otherwise, tell them it costs way too much and isn't worth it

# _______________________

# EXTENSION
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 