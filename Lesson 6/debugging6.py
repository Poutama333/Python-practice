MEMBER_STATUS = "GOLD"
passenger_row = input("Enter your seat row: ").strip()
has_ticket = input("Do you have a valid ticket? (yes/no): ").lower()
if has_ticket == "no":
    print("Access Denied. Please ensure you have a valid ticket before boarding.")
elif passenger_row <= 8 or MEMBER_STATUS == "GOLD":
    print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")
else:
    print("Please wait for general boarding.")
destination = input("Enter your destination code: ")
if destination == "AKL" or "WLG":
    print("Flight is delayed 5 minutes.")
# PSEUDOCODE START
# IF NOT destination is equal to "CHC" THEN print "Flight is on time."
# ELSE print "Flight has been cancelled"