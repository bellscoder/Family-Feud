  # Importing Libraries
import random
import math
import function_defs
from question_1 import question_1_dict
from question_2 import question_2_dict
from question_3 import question_3_dict

## Set ups
current_dict = question_1_dict
function_defs.intro()

times = 0
team_1 = True
team_1_points = 0
team_2_points = 0
running = True
correct_answer = False
team_answered = False
## Strikes
guesses_1 = 3
guesses_2 = 3
current_guess = guesses_1

## Put answers in list
team_1_answers = ["", "", ""]
team_2_answers = ["", "", ""]

## Current question
question_number = 1

## While Loop
while running:

  ## Change Dictionaries
  if question_number == 1:
    current_dict = question_1_dict
  elif question_number == 2:
    current_dict = question_2_dict
  elif question_number == 3:
    current_dict = question_3_dict

  ## Output of team strikes and points
  if team_1:
    print(f"It is currently team one's turn, with {current_guess} guesses remaining.")
    print(f"They have {team_1_points} points in total")
  else:
    print(f"It is currently team two's turn, with {current_guess} guesses remaining.")
    print(f"With {team_2_points} points in total")

  ## Print the current question
  q1 = current_dict
  print(q1["question"])
  answer_to_q1 = input()
  answer = answer_to_q1.lower()
  print("storing answer," + answer)
  
  if answer == "quit" or answer == "exit":
    print("If you say so...")
    function_defs.outro(question_1_dict, question_2_dict, question_3_dict, team_1_answers, team_2_answers)
    break

  index = question_number - 1
  # Save user answers
  if question_number == 1:
    
    if team_1:
        team_1_answers[index] = answer_to_q1
    else:
        team_2_answers[index] = answer_to_q1
  
  elif question_number == 2:
    
    if team_1:
        team_1_answers[index] = answer_to_q1
    else:
        team_2_answers[index] = answer_to_q1
  
  elif question_number == 3:
    
    if team_1:
        team_1_answers[index] = answer_to_q1
    else:
        team_2_answers[index] = answer_to_q1
  
  ## Call check answer function
  correct1 = function_defs.check_answer1(answer_to_q1, current_guess, current_dict)
  
  ## Check if correct
  if correct1 == False:
    
    if current_guess > 0:
      current_guess -= 1
      if team_1:
        guesses_1 -= 1
      else:
        guesses_2 -= 1
    '''##  Check if the team is out of guesses
    if current_guess == 0:
      team_1 = not team_1
      
      ## Check which team is guessing
      if team_1:
        current_guess = guesses_1
      else:
        current_guess = guesses_2'''
  
  ## Change the question and reset guesses
  if current_guess == 0:
    
    if not team_answered:
      team_1 = not team_1
      
      if team_1:
        current_guess = guesses_1
      else:
        current_guess = guesses_2
      team_answered = True 
    else:
      question_number += 1
      ## Stop the game here(more to be added later)  
      if question_number > 3:
        print("Sorry more questions soon.")
        running = False
        break
      guesses_1 = 3
      guesses_2 = 3
      team_answered = False  # reset for next question
        
      if team_1:
          current_guess = guesses_1
      else:
          current_guess = guesses_2

    if team_1:
      current_guess = guesses_1
    else:
      current_guess = guesses_2  

  ## Is answer in a dict?
  if answer in current_dict["answers"]:
    points = current_dict["answers"][answer]

    ## Give points to the correct team
    if team_1:
      team_1_points += points
    else:
      team_2_points += points

## If game is over
if not running:
  print("Team 1 answers:", team_1_answers)
  print("Team 2 answers:", team_2_answers)

  ## Use outro Function
  function_defs.outro(question_1_dict, question_2_dict, question_3_dict, team_1_answers, team_2_answers)
