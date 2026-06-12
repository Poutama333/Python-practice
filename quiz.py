    # Quiz

#while True: 
#    
#        # Question
#    question1 = input("Question 1: \n"
#        " What is the capital city of New Zealand, is it  \n"
#        " a) Russel  \n"
#        " b) Christchurch \n"
#        " c) Wellington  \n"
#        " d) Auckland \n").lower()
correct = 0
incorrect = 0
KEY_QUESTION = "question"
KEY_ANSWER = "answer"
question_and_answer_dictionary = [
    {KEY_QUESTION:"What is the fastest animal on earth is it: \n a)Cheetah \n b)Panther \n c)Peregrine Falcon \n d)Pigeon \n",KEY_ANSWER:"c"},
    {KEY_QUESTION:"What is the capital of New Zealand is it: \n a)Auckland \n b)Russel \n c)Christurch \n d)Wellington \n",KEY_ANSWER:"d"},
    {KEY_QUESTION:"What does KHCL stand for: \n a)Keith Hunter central Learning \n b) Ken Havill Centre for Learning \n c) Kool Hlucks Clan Location \n d)Kiev Hiev Ciev Liev \n",KEY_ANSWER:"b"},
    {KEY_QUESTION:"What colour is a Zebra?: \n a)Black with white dots \n b)Red and black spots \n c)White with black stripes \n d)Black with white stripes \n",KEY_ANSWER:"d"},
    {KEY_QUESTION:"What team will win the 2026 Ampol state of origin: \n a)New south \n  b)Blue south \n c)Up da blues \n d)Queer land \n", KEY_ANSWER:"a"},
]
while True:
    for amount_of_questions in question_and_answer_dictionary:     
        question = input(amount_of_questions[KEY_QUESTION]).lower()
        if question == (amount_of_questions[KEY_ANSWER]):
            print("Nice, You got it correct \n")
            correct += 1
        elif question == "a" or question == "b" or question == "c" or question == "d":
            print("Sorry, you got it incorrect.")
            incorrect += 1
        else:
            invalid = input("Sorry, thats an invalid input, try typing a letter (a,b,c,d). Press a to restart the whole quiz or press b to repeat the question. ").lower()
            if invalid == "a":
                break
            elif invalid == "b":
                continue

    
print("Nice, you've finished the quiz. You got",correct,"questions correct, and",incorrect,"questions incorrect.")

        
   
