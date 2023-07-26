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

##
images = [rock, paper, scissors]
user = int(input("Let's play Rock, Paper, and Scissors! Use 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if user >= 3 or user < 0:
    print("Invalid Entry.")
else:
    
    print(f"You choose {images[user]}")
    computer = random.randint(0,2)
    print(f"Computer choose {images[computer]}")


    if user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You loose")
    elif computer > user:
        print("Computer Wins.")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("It's a draw.")

 

