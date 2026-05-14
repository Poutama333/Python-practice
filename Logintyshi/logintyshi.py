


loginorsignup = input("login or Sign up? ")
if loginorsignup == "Signup" or "sign up" or "signup":
    username = input("What will your username be? ")
    password = input("What will your password be? ")
    with open("Users/Poutama/Documents/GitHub/Python practice/Logintyshijmk /logintyshii.txt", "a") as f:
        f.write(username)
        f.write(password)

#open and read the file after the appending:
    print("Great, now you can login")
    usernametypein = input("What is your username? ")
else:
    usernametypein = input("What is your username? ")
