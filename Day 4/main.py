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
import random
# 0>2
# 2>1
# 1>2
game = [rock, paper, scissors]
choice = int(input("what you want? choose 0,1,2.\n"))

print(f"you choose {game[choice]}")

print("computer choose:")
com_choice = random.randint(0, 2)
print(game[com_choice])

if choice >= 3 or choice < 0:
    print("invalid number, you lose")
elif choice == 0 and com_choice == 2:
    print("you win")
elif choice == 2 and com_choice == 0:
    print("you lose")
elif choice > com_choice:
    print("you win")
elif choice < com_choice:
    print("you lose")
else:
    print("draw")
