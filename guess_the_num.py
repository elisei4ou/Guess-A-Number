import random
from colorama import Fore, Style

computer_number = random.randint(1, 100)
next_move = ""
counter = 0

while True:
    if next_move == "yes":
        player_input = (input(Fore.LIGHTWHITE_EX + "Guess the number (1-200), but u have only 7 tries: "))
    else:
        player_input = (input(Fore.LIGHTWHITE_EX + "Guess the number (1-100), but u have only 7 tries: "))
    if not player_input.isdigit():
        print(Fore.RED + "Invalid input! Please try again...")
        continue

    if computer_number == int(player_input):
        counter = 0
        print(Fore.GREEN + "You guessed it!")
        next_move = input(Fore.LIGHTWHITE_EX + "Do you want to continue [yes/no]?: ")
        if next_move == "yes":
            computer_number = random.randint(1, 200)
            continue
        elif next_move == "no":
            raise SystemExit(Fore.YELLOW + "Thanks for playing")

    elif computer_number > int(player_input):
        counter += 1
        print(Fore.LIGHTGREEN_EX + "Too Low!")
        continue
    else:
        counter += 1
        print(Fore.LIGHTRED_EX + "Too High!")
        continue
    if counter == 7:
        print(Fore.RED + "You ran out of tries!")
        break