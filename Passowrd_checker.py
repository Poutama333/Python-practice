def pass_checker():
    password = input("What is your password? ").lower().strip()
    has_number = False
   
    if any(char.isdigit() for char in password):
       has_number = True
         
    if len(password) >= 8  and has_number == True:
        print("Password valid.")
    else:
        print("Password invalid.")
        
pass_checker()