    # Quiz

while True: 
    
        # Question
    question1 = input("Question 1: \n"
        " What is the capital city of New Zealand, is it  \n"
        " a) Russel  \n"
        " b) Christchurch \n"
        " c) Wellington  \n"
        " d) Auckland \n").lower()
        
    if question1 == "c":
            print("Correct!")
    else:
        input("Invalid, press any key to try again")
        continue
        
        
    question2 = input("Question 2: \n"
    " What is the fastest animal on earth\n"
    " a)Cheetah\n"
    " b)Panther\n"
    " c)Peregrine falcon\n"
    " d)Pigeon\n")
    
    if question2 == "c" or "C":
        print("Correct!")
    else:
        input("Invalid, press any key to try again")
        continue
        
    
    
    
    
    question3 = input("Question 3:\n"
    "What does KHCL stand for\n"
    " a)Keith Hunter central Learning\n"
    " b)Ken Havill Centre for Learning\n"
    " c)Kool Hlucks Clan Location\n"
    " d)Kiev Hiev Ciev Liev\n")
   
    if question3 == "b":
        print("Correct!")
    else:
        input("Invalid, press any key to try again")
        continue
    print("\n")
    
    question4 = input("Question 4:\n"
    "What colour is a Zebra?\n"
    " a)Black with white dots\n"
    " b)Red and black spots\n"
    " c)White with black stripes\n"
    " d)Black with white stripes\n")
    
    if question4 == "d":
        print("Correct!")
    else:
        input("Incorrect, press any key to try again")
        continue 
    print("\n")
    
    question5 = input("Question 5:\n"
    "New South Wales or Queerland\n"
    " a)New south\n"
    " b)Blue south\n"
    " c)Up da blues\n"
    " d)Queer land\n")
    
    if question5 == "d":
        print("New south wales, we're the blues, Queerland, you're gonna lose.")
        break
    else:
        input("You win!")
    print("Aight gap it foolish.")
        
    print("\n")