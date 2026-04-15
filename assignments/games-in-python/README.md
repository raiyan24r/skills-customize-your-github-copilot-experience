
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python that uses loops, conditionals, and string operations. By the end of this assignment, you will create an interactive terminal game where players guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description
Create the initial game structure by defining a word list, selecting one word randomly, and preparing variables to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Store multiple possible words in a predefined list
- Randomly select one target word at the start of the game
- Initialize the display state using underscores for unguessed letters
- Set a fixed number of incorrect guesses allowed


### 🛠️ Implement the Guessing Loop

#### Description
Build the main game loop that accepts letter guesses, updates progress, tracks mistakes, and ends with a win or lose message.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per turn
- Reveal correctly guessed letters in the word display
- Decrease remaining attempts for incorrect guesses
- End the game when the full word is guessed or attempts reach zero
- Display a clear win or lose result message
