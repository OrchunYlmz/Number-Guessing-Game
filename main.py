
import random
from art import logo
def number():
  guess_number=random.randint(1,100)
  return guess_number

attempts=0
def reduce_health():
  global attempts
  #attempts-=1
  return attempts-1

def play_game():
  print(logo)
  
  global attempts
  guessed_number=number()
  
  ask=input("Choose a difficulty. 'easy' or 'hard': ")
  if ask=="easy":
    attempts=10    
  elif ask=="hard":
    attempts=5
  print(guessed_number)
  game_over=False
  while not game_over and attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess < guessed_number:
      print("Too low! Guess again.")
      attempts=reduce_health()
    elif guess > guessed_number:
      print("Too high! Guess again.")
      attempts=reduce_health()
    elif guess==guessed_number and attempts>0:
      print("Congrats, you won!")
      new_game=input("Press 'y' to play again, something else to not play: ")
      if new_game=="y":
        play_game()
      elif new_game!="y":
        game_over=True
      
    if attempts==0:
      print("You've run out of guesses, you lose.")
      new_game=input("Press 'y' to play again, something else to not play: ")
      if new_game=="y":
        play_game()
      elif new_game!="y":
        game_over=True

play_game()