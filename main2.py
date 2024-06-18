from random import randint
from art import logo
elt=10
hlt=5

def check_answer(guess,answer,turns):
  """Checks if guess equals to answer. Returns number of remaining turns."""
  if guess < answer:
    print("Too low!")
    return turns-1
  elif guess > answer:
    print("Too high!")
    return turns-1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  diff = input("Choose a difficulty, type 'easy' or 'hard': ")
  if diff =="easy":
    return elt
  elif diff=="hard":
    return hlt
    
def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer=randint(1,100)
  turns=set_difficulty()

  
  guess=0
  while guess!=answer:
    print(f"You have {turns} attempts remaining to guess the number!")
    guess=int(input("Make a guess: "))
    
    turns=check_answer(guess,answer,turns)
    if turns==0:
      print("You have run out of guesses, you lose!")
      return
    elif guess!=answer:
      print("Wrong guess, guess again!")

play_game()