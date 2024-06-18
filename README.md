# Number-Guessing-Game

This repository contains two versions of a simple number guessing game. The player tries to guess a randomly selected number between 1 and 100. The game has two difficulty levels: easy and hard.

## Description (main)
In this version, the game is implemented using a global variable for the number of attempts. The player selects the difficulty level, which determines the number of attempts they have to guess the number correctly. The game provides feedback if the guess is too low or too high.

## Description (main2)
In this version, the game logic is improved for better readability and structure. The number of attempts is managed within functions, and the game uses helper functions to check guesses and set difficulty levels. This version also provides more detailed feedback and is easier to maintain.

## Gameplay:

  -The game starts by displaying a logo and asking the player to choose a difficulty level ('easy' or 'hard').
  -The player makes guesses, and the game indicates if the guess is too low or too high.
  -The player wins if they guess the correct number within the allowed attempts. If they run out of attempts, they lose.
  -The player can choose to play again or exit after each game.
