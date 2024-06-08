import random
from art import logo, vs
from game_data import data
from replit import clear

player_score = 0
a = random.choice(data)
a_followers = a['follower_count']

print(f"{logo}\n")

continue_game = True
while continue_game:
  
  b = random.choice(data)
  b_followers = b['follower_count'] 
  
  print(f"Compare_A: {a['name']}, a {a['description']}, from {a['country']}.")
  
  print(vs)
  
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.\n")

  player_answer = input("Who has more followers? Type 'A' or 'B':  ").lower()

  clear()
  
  print(f"{logo}\n")
  
  if player_answer == 'a' and a_followers > b_followers:
    player_score += 1
    print(f"You're right! Current score: {player_score}.\n")

  elif player_answer == 'b' and b_followers > a_followers:
    player_score += 1
    a=b
    print(f"You're right! Current score: {player_score}.\n")

  else:
    print(f"Sorry, that's wrong. Final score: {player_score}.")
    continue_game = False
