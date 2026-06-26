
"""Constants"""

KEY_QUESTION = "question"
KEY_ANSWER = "answer"

"""Functions"""

def quiz_loop():
    
    correct = 0

    incorrect = 0

    


    question_and_answer_dictionary = [
    {KEY_QUESTION:"What is the fastest animal on earth is it: \n a)Cheetah \n b)Panther \n c)Peregrine Falcon \n d)Pigeon \n",KEY_ANSWER:"c"},
    {KEY_QUESTION:"What is the capital of New Zealand is it: \n a)Auckland \n b)Russel \n c)Christurch \n d)Wellington \n",KEY_ANSWER:"d"},
    {KEY_QUESTION:"What does KHCL stand for: \n a)Keith Hunter central Learning \n b) Ken Havill Centre for Learning \n c) Kool Hlucks Clan Location \n d)Kiev Hiev Ciev Liev \n",KEY_ANSWER:"b"},
    {KEY_QUESTION:"What colour is a Zebra?: \n a)Black with white dots \n b)Red and black spots \n c)White with black stripes \n d)Black with white stripes \n",KEY_ANSWER:"d"},
    {KEY_QUESTION:"What is 9+9x3(2-8): \n a) -153  \n b)153 \n c) 60 \n d) -60 \n", KEY_ANSWER:"a"},
    ]
    while True:
        play = input("Would you like to play my quiz? y/n ").strip().lower()
        if play == "y" or play == "n":
            break
        else:
            print("Invalid, press y or n.")
            continue

    while play == "y":
        for amount_of_questions in question_and_answer_dictionary:     
            while True:    
                question = input(amount_of_questions[KEY_QUESTION]).lower().strip()
    
                if question == (amount_of_questions[KEY_ANSWER]):
    
                    print("Nice, You got it correct \n")
                    correct += 1
                    break
    
                elif question == "a" or question == "b" or question == "c" or question == "d":
    
                    print("Sorry, you got it incorrect.")
                    incorrect += 1 
                    break
    
                else:
    
                    print("Sorry, that was invalid. Press a,b,c, or d to select your answer. ")
                    continue
        while True:
            play = input("Press y to play again, press n to end. ").strip().lower()  
            if play == "y" or play == "n":
                break
            else:
                print("Invalid, press y or n.")
                continue
        

    return correct,incorrect      
                 
"""Main"""        

def main():
    print("This is a quiz, press a,b,c, or d to select your answer.")
    
    results = quiz_loop()
                    
    print("Nice, you've finished the quiz. You got",results[0],"questions correct, and",results[1],"questions incorrect.")

        
   
main()