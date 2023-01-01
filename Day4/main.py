import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choice = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

options = [rock, paper, scissors]
print(options[player_choice])
print(f"Computer chose:\n{options[computer_choice]}")

if player_choice == 0:
    if computer_choice == 0:
        print("You Draw")
    elif computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")
elif player_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("You draw")
    elif computer_choice == 2:
        print("You lose")
elif player_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    elif computer_choice == 2:
        print("You draw")
