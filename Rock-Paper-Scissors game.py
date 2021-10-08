import random
from RPS_ASCII_Art import rock, paper, scissors

choices = [rock, paper, scissors]

user_choice = int(input('What do u choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(choices[user_choice])
computer_choice = random.randint(0, 2)
print("Computer choice:\n" + choices[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number, you lose!')
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif user_choice == 2 and computer_choice == 0:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif user_choice < computer_choice:
    print('You lose!')
else:
    print("It's a draw!")
