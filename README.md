# GUESS-NUMBER
This is a simple Python number guessing game where the player selects a difficulty level and tries to guess a randomly chosen number within limited chances.

How it works:
1.Select Difficulty Level
The player chooses between:
Easy → number between 1 and 30
Medium → number between 1 and 60
Hard → number between 1 and 100
Based on the choice, the game randomly picks a secret number within that range.

2.Guessing the Number
The player has 4 chances to guess the secret number.
For each guess:
If the guess is correct → You win! 🎉
If the guess is very close (within 5 of the secret number) → "It's very close!"
If the guess is wrong, the game gives a hint whether the guess is too high or too low.

3.Game End
If the player guesses the number correctly within the chances → they win.
If they run out of chances → the game reveals the correct number.

4.Replay Option
After the game ends, the player can choose to play again or exit.
