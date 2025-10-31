
##     Family Feud Code


# Importing Libraries
import random
import math
import function_defs
from question_1 import question_1_dict
from question_2 import question_2_dict
from question_3 import question_3_dict

# Show the intro to the game
function_defs.intro()

times = 0

team_1 = True

team_1_points = 0

team_2_points = 0
running = True

times = 0

correct_answer = False

## Strikes
guesses_1 = 3
guesses_2 = 3
if team_1:
  current_guess = guesses_1
else:
  current_guess = guesses_2
## While Loop
while running:
    if team_1:
      print("It is currently team one's turn, with " + str(guesses_1) + " guesses remaining.")
    else:
      print("It is currently team two's turn, with " + str(guesses_2) + " guesses remaining.")
    
    # Print the first question
    q1 = question_1_dict
    print(q1["question"])
    answer_to_q1 = input()
    
    correct1 = function_defs.check_answer1(answer_to_q1,guesses_1,question_1_dict)
    print(correct1)
    if not correct1:
      current_guess -= 1
    
    if current_guess == 0 and times == 0:
      team_1 = False
      times += 1
    elif current_guess == 0 and times == 1:
      team_1 = True
      times = 0
    answer = answer_to_q1.lower()
    if answer in question_1_dict["answers"]:
      points = (question_1_dict["answers"][answer])
      correct_answer = True
    if correct_answer and times == 0:
      team_1_points += points
      correct_answer = False
    elif correct_answer and times == 1:
      team_2_points += points
      correct_answer = False
if not running:
  function_defs.outro(question_1_dict,question_2_dict,question_3_dict)
