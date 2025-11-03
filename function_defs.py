# Unit_2_CodeYour_Own

import sys
import time

def intro():
  print("Welcome to Family Fued")
  print("You have 3 chances to get try to get all of the answers\n")
  print("Try to get as many points as you can!")


def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print() 

def check_answer1(answer_to_q1,current_guess, current_dict):
    user_answer = answer_to_q1.strip().lower()
    answers_dict = current_dict.get("answers") or current_dict.get("answer") or {}

    if user_answer in answers_dict:
        print("Correct!")
        return True
    else:
        print("Incorrect. Try again!")
        return False

#outro
def outro(question_1_dict, question_2_dict, question_3_dict, team_1_answers, team_2_answers):
    
    print("Thank you for playing Family Feud!")
    print("Here are your answers:\n")
    
    typewriter("On question 1 we asked you why are kids late for school.")
    print("Team 1 said:", team_1_answers[0])
    print("Team 2 said:", team_2_answers[0])
    typewriter("Survey says... ")
    for answer in question_1_dict["answers"]:
        print(f"- {answer}")
    
    typewriter("On question 2 we asked you what people might forget when they leave the house.")
    print("Team 1 said:", team_1_answers[1])
    print("Team 2 said:", team_2_answers[1])
    typewriter("Survey says... ")
    for answer in question_2_dict["answers"]:
        print(f"- {answer}")
    
    typewriter("On question 3 we asked you what people do when they are late for work.")
    print("Team 1 said:", team_1_answers[2])
    print("Team 2 said:", team_2_answers[2])   
    for answer in question_3_dict["answers"]:
        print(f"- {answer}")

