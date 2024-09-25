"""
The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
"""
import random

def game():
    current_score = random.randint(1, 100)
    
    with open("Practice 9 File IO/Hi_score.txt") as f:
        current_high_score = f.read()
        if current_high_score != '':
            current_high_score = int(current_high_score)
        else:
            current_high_score = 0
    
    print(f"Your score is {current_score}")
    
    if current_score > current_high_score:
        with open("Practice 9 File IO/Hi_score.txt", "w") as f:
            f.write(str(current_score))


if __name__ == "__main__":

    game()