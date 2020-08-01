from Question_file import Questions 

question_promt = [
    "What color are apples?\n(a) Red\n(b) Purple\n\n",
    "What color are banana?\n(a) Magneta\n(b) Yellow\n\n",
    "What color are papaya?\n(a) Red\n(b) Yellow\n\n",
]

questions = [
    Questions(question_promt[0], "a"),
    Questions(question_promt[1], "b"),
    Questions(question_promt[2], "b")
]

def run_test(questions): 
    score = 0
    for question in questions:
        answer = input(question.promt)
        if answer == question.answer:
            score +=1
   

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")      

run_test(questions)