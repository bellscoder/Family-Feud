
##     Family Feud Code


# Importing Libraries
import random
import math
import function_defs
import random
from question_1 import question_1_dict
from question_2 import question_2_dict
from question_3 import question_3_dict
## set ups
current_dict = question_1_dict
# Show the intro to the game
function_defs.intro()

times = 0

team_1 = True

team_1_points = 0

team_2_points = 0
running = True

correct_answer = False

## Strikes
guesses_1 = 3
guesses_2 = 3

current_guess = guesses_1
## While Loop
while running:
  ##dict change
  if times == 2:
    current_dict = question_2_dict

  elif times == 4:
    current_dict = question_3_dict
  ##output of team strikes and points
  if team_1:
    print(f"It is currently team one's turn, with {current_guess} guesses remaining.")
    print(f"With {team_1_points} points in total")
  
  else:
    print(f"It is currently team two's turn, with {current_guess} guesses remaining.")
    print(f"With {team_2_points} points in total")
  # Print the first question
  
  q1 = current_dict
  print(q1["question"])
  answer_to_q1 = input()
  
  correct1 = function_defs.check_answer1(answer_to_q1,guesses_1,question_1_dict)
  print(correct1)
  if correct1 == False:
    current_guess -= 1
  
  if current_guess == 0 and times == 0 or times == 2 or times == 4:
    team_1 = False
    times += 1
    current_guess = guesses_2
  elif current_guess == 0 and times == 1 or times == 3 or times == 5:
    team_1 = True
    times += 1
    current_guess = guesses_1

  answer = answer_to_q1.lower()

  if answer in question_1_dict["answers"]:
    points = (question_1_dict["answers"][answer])
    correct_answer = True

  if correct_answer and times == 0 or times == 2 or times == 4:
    team_1_points += points
    correct_answer = False

  elif correct_answer and times == 1 or times == 3 or times == 5:
    team_2_points += points
    correct_answer = False

  if times == 2:
    running = False
    break
    
if not running:
  function_defs.outro(question_1_dict,question_2_dict,question_3_dict)
