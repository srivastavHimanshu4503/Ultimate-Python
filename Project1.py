"""
We all have played snake, water gun game in our childhood. If you haven't, google the
rules of this game and write a python program capable of playing this game with the
user.
"""
import random

def program_run():
    continue_to_play = True
    options = ["Snake", "Water", "Gun"]
    count_of_attempt = 0
    while continue_to_play:
        # Assigning variables their values
        random_number = random.randint(0, 2)
        user_input = input(f"Choose one of the options from the list {options}: ")
        computer_input = options[random_number]

        # Used match case to check whether the user won or not.
        match user_input.lower():
            case "snake":
                if computer_input == "Snake":
                    print("Draw, Better Luck next time!")
                    count_of_attempt += 1
                elif computer_input == "Water":
                    print("Snake drinks the water, you won.")
                    count_of_attempt += 1
                    print(f"You took {count_of_attempt} took to complete this game.")
                    continue_to_play = False if input("Do you want to play again?\nTrue/False: ").capitalize() == "False" else True
                else:
                    print("Gun kills the snake, you loose.")
                    count_of_attempt += 1

            case "water":
                if computer_input == "Snake":
                    print("Snake drinks the water, you loose.")
                    count_of_attempt += 1
                elif computer_input == "Water":
                    print("Draw, Better Luck next time!")
                    count_of_attempt += 1
                else:
                    print("Water damged the gun, you won.")
                    count_of_attempt += 1
                    print(f"You took {count_of_attempt} took to complete this game.")
                    continue_to_play = False if input("Do you want to play again?\nTrue/False: ").capitalize() == "False" else True

            case "gun":
                if computer_input == "Snake":
                    print("Gun kills the snake, you won.")
                    count_of_attempt += 1
                    print(f"You took {count_of_attempt} took to complete this game.")
                    continue_to_play = False if input("Do you want to play again?\nTrue/False: ").capitalize() == "False" else True
                elif computer_input == "Water":
                    print("Water damaged the gun, you loose")
                    count_of_attempt += 1
                else:
                    print("Draw, Better Luck next time!")
                    count_of_attempt += 1


if __name__ == "__main__":
    
    program_run()

    print("Thank you for playing this game.\nVisit next time soon.")