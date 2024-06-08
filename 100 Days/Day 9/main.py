from replit import clear

# #HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)

new_users = False
bidding_details = {}


def highest_bidder(bidding_details):
  highest_bid = 0
  winner = ""
  for bid_value in bidding_details:
    bid_price = bidding_details[bid_value]
    if bid_price > highest_bid:
      highest_bid = bid_price
      winner = bid_value

  print(
      f"Congratulations, the winner is {winner}, with the highest bid of {highest_bid}."
  )


while new_users == False:
  name = input("What is your name?: ")
  bid = int(input("what is your bid?: $"))
  bidding_details[name] = bid
  users = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if users == "no":
    new_users = True
    highest_bidder(bidding_details)


def highest_bidder(bidding_details):
  highest_bid = 0
  for bid_value in bidding_details:
    bid_price = bidding_details[bid_value]
    if bid_price > highest_bid:
      highest_bid = bid_price
  print(highest_bid)


# Bidders = "yes"
# dict = {}

# def highest_bidder(dict):
#   highest_bid = 0
#   for bidder in dict:
#     bidder_value = dict[bidder]
#     if bidder_value > highest_bid:
#       highest_bid = bidder_value
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while Bidders == "yes":
#   name = input("What is your name?: ")
#   bid = int(input("What is your bid?: $"))
#   dict[name] = bid
#   Bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#   if Bidders == "yes":
#     clear()
#   if Bidders == "no":
#     Bidders = False
#     clear()
#     highest_bidder(dict)
