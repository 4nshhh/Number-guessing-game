# 🎯 Number Guessing Game (Python CLI)

## 📄 Description
A simple command-line Python game where the player must guess a randomly generated number between 1 and 100. The player has only 5 attempts, and the game provides feedback for each guess. The best score (minimum attempts) is saved in a text file and displayed when a new high score is achieved.

---

## 🌱 About This Project  
This was one of my early Python practice projects.  
I created this Number Guessing Game to strengthen my understanding of conditionals, loops, and user input.  
I also learned how to use the `random` module and work with files to track and update the best score.

---

## 🛠️ Technologies Used
- Python 3
- Built-in modules: `random`, `os`
- File handling (`best_score.txt`)

---

## 🚀 How to Run
1. Make sure Python 3 is installed.
2. Clone this repository or download the `.py` file.
3. Run the program using:
   ```bash
   python main.py
   ```

---

## 🎮 Features
- 🎲 Random number between 1 and 100
- ⏳ 5 attempts to guess the number
- 🧠 Feedback on each guess ("Too High", "Too Low")
- 🏆 Tracks and saves best score using `best_score.txt`
- 📂 Persistent best score across multiple games

---

## 📚 What I Learned
- Random number generation using `random.randint()`
- Loops, conditionals, and input handling
- File reading/writing and score persistence
- Simple game logic

---

## 📝 Future Improvements
- Add input validation (handle non-integer input)
- Create a GUI using `Tkinter` or `PyGame`
- Track player name and score history
- Add difficulty levels (Easy, Medium, Hard)
- Create a restart/replay option

---

## 📸 Sample Output

```
Welcome to the number guessing game!
Guess the number between 1 to 100. You have 5 attempts.
Enter your guess: 50
Too High!
Attempts left: 4
Enter your guess: 25
Too Low!
Attempts left: 3
Enter your guess: 37
Correct! You guessed the number in 3 attempts.
New Best Score!
```
