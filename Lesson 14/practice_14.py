"""
PROGRAM: Geometry Helper
This program helps to calculate the area and circumference of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing functions for calculating the area and circumference 
# taking the user input and returning it, 
# and calling each function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# TODO ------->>>> Write a function here for calculating the area of a rectangle using passed values. 
# TODO ------->>>> Return the result.
def calculate_area(width,length):
    area = width * length
    return area

def calculate_circumference(radius):
    circumference = 2 * 3.141592653589793 * radius
    return circumference


# TODO ------->>>> Write a function here for calculating the circumference using passed values. 
# TODO ------->>>> Return the result.

def display_result(message):
    print("\n------------------")
    print(message)
    print("------------------")

# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Circumference Calculator")


    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "1":
        width = int(input("What is the width of your rectangle"))
        length = int(input("What is the length of your rectangle"))
        area = calculate_area(width,length)
        # TODO ------->>>> Call the function for calculating area here and save it into variable 'area'
        
        display_result(f"The area of your rectangle is {area}².")

    elif choice == "2":

        # TODO ------->>>> Call the function for calculating circumference here and save it into variable 'circumference'
        circumference = calculate_circumference(int(input("What is the radius of your circle. ")))
        display_result(f"The circumference of your circle is {circumference}.")

    else:
        print("Invalid choice. Exiting dashboard.")


# =====================================================================
# EXECUTION
# =====================================================================

main()