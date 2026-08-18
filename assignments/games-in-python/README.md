
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, conditionals, and user input. Students will practice tracking game state, validating guesses, and ending the game based on win or lose conditions.

## 📝 Tasks

### 🛠️ Create the secret word system

#### Description
Set up the word list and choose a hidden word for the player to guess.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Hide the word so the player starts with a blank progress display
- Show the word length or blank placeholders to help the player understand the challenge

### 🛠️ Build the guessing loop

#### Description
Create the main game loop that accepts guesses, updates the display, and ends the game when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Accept letter guesses from the player one at a time
- Update the visible word display when a correct letter is guessed
- Track incorrect guesses and reduce the number of attempts remaining
- Prevent the game from continuing after the word is fully guessed or attempts are exhausted
- Display clear win and lose messages at the end of the game
