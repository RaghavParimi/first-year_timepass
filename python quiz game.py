#python quiz game
questions = (
    "what is the format of a python file? ",
"what keyword is used to define a function in python? ",
    "which data type is used to store multiple items in a single variable? ",
    "who invented the world wide web (www.)? ",
    "who is the founder of microsoft? ",
    "who is the founder of linux? "
    )
options= (("A.txt","B..py","C..python","D..pyt"),
          ("A.def","B.function","C.define","D.fun"),
          ("A.dict","B.list","C.set","D.tuple"),
          ("A.Mark Zuckerberg","B.Bill Gates","C.Steve Jobs","D.Tim Berners-Lee"),
          ("A.Bill Gates","B.Steve Jobs","C.Linus Torvalds","D.Mark Zuckerberg"),
          ("A.Steve Jobs","B.Bill Gates","C.Linus Torvalds","D.Mark Zuckerberg")
        )

    
answers = ("B","A","B","D","A","C")
guesses = []
score = 0
question_num = 0
 
print("-------------------------")
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()

    while(guess != 'A' or guess != 'B' or guess != 'C' or guess != 'D'):
        if(guess == 'A' or guess == 'B' or guess == 'C' or guess == 'D'):
            guesses.append(guess)
            break
        else:
            print("-------------------------")
            print("Please Enter (A, B, C, or D):")
            print(question)
            for option in options[question_num]:
                    print(option)
            guess = input("Enter (A, B, C, or D): ").upper()


    if guess == answers[question_num]:
        score += 1
        print("Correct!")
        question_num += 1
    else:
        print("Wrong!")
        print(f"The correct answer is: {answers[question_num]}")
        question_num += 1
            

print("-------------------------")
print("Quiz complete!")
print(f"Your score: {score}/{len(questions)}")