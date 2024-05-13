#Number Guessing Game Objectives:


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
import os

# Include an ASCII art logo.
logo = """
╔═╗┬ ┬┌─┐┌─┐┌─┐  ╔╦╗┬ ┬┌─┐  ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐
║ ╦│ │├┤ └─┐└─┐   ║ ├─┤├┤   ║║║│ ││││├┴┐├┤ ├┬┘
╚═╝└─┘└─┘└─┘└─┘   ╩ ┴ ┴└─┘  ╝╚╝└─┘┴ ┴└─┘└─┘┴└─

"""

def check_guess(guess, answer,turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
  os.system("cls")
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(0,100)
  print(f"Pssst, the correct answer is {answer}")
  
  #Repeat the guessing functionality if they get it wrong.
  turns = set_difficulty()
  guess = 0
  
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
  
    # Allow the player to submit a guess for a number between 1 and 100.
    guess =int(input("Make a guess: ")) 
    
    turns = check_guess(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

should_continue =True
while should_continue:
  game()
  if input("Do you want to play again? Type 'y' or 'n': ") == "n":
    should_continue =False