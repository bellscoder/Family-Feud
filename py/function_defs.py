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

def check_answer1(answer_to_q1,guesses_1,question_1_dict):
    user_answer = answer_to_q1.strip().lower()
    answers_dict = question_1_dict.get("answers") or question_1_dict.get("answer") or {}

    if user_answer in answers_dict:
        print("Correct!")
        return True
    else:
        print("Incorrect. Try again!")
        return False

#outro
def outro(question_1_dict,question_2_dict,question_3_dict):
  print("Thank you for playing Bells Fued!")
  print("Here are your answers: ")
  print()
  typewriter("On question 1 we asked you why are kids late for school.")
  print("You said: " + question_1_dict["question"])
  print()
  typewriter("Survey says... " + question_1_dict["answers"])
  typewriter("On question 2 we asked you what people might forget when they leave the house.")
  print("You said: " + question_2_dict["question"])
  print()
  typewriter("Survey says... " + question_3_dict["answers"])
  typewriter("On question 1 we asked you what people do when they are late for work.")
  print("You said: " + question_3_dict["question"])
  print()
  typewriter("Survey says... " + question_3_dict["answers"])
