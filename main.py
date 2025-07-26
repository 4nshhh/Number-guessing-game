# Number Guessing Game (with Score Tracker)
# Goal: Build an interactive game where user guesses a number between 1–100.

# Additions to Make it Interesting:
# Limit to 5 chances
# Give hints: "Too high" / "Too low"
# Keep score and save it to a file
# Track best score (best_scoreimum guesses)

import random

number = random.randint(1,100)
print(number)

counter = 0
print("Welcome to the number guessing game!")
print("Guess the number between 1 to 100. You have 5 attempts.")
while True:
    guess = int(input("Enter your guess: "))
    counter+=1

    if counter > 5:
        print("You lost, Better luck next time!")
        print(f"Correct number was: {number}")
        break

    if guess > number:
        print(f"Too High!\nAttempts left: {5-counter}")
    elif guess < number:
            print(f"Too Low!\nAttempts left: {5-counter}")
    
    elif guess == number:
        print(f"Correct! You guessed number in {counter} attempts.")
        with open("best_score.txt","r") as f:
            lines = f.readlines()
            scores = [int(line.strip()) for line in lines if line.strip().isdigit()]
            best_score = min(scores)

            if counter <= best_score:
                print("New Best Score!")
                with open("best_score.txt","w") as f:
                    f.write(f"\n{counter}")
        break
