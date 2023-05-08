
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
import os

from art import logo
print(logo)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def hand_value(hand):
  value = 0
  for card in hand:
    value += card
  return value

def add_card(hand):
  hand.append(random.choice(cards))
  return hand

def display(p_hand, d_hand, d_cards_view):
  print(f"Your cards: {p_hand}.")
  print(f"Current score: {hand_value(p_hand)}")
  if d_cards_view == 1:
    print(f"The dealer's first card: {d_hand[0]}")
  else:
    print(f"The dealer's cards: {d_hand}")
    print(f"The dealer's score: {hand_value(d_hand)}")

def play_game():
  p_hand = []
  d_hand = []
  p_hand = add_card(p_hand)
  p_hand = add_card(p_hand)
  d_hand = add_card(d_hand)
  d_hand = add_card(d_hand)
  more_cards = "y"
  cls()
  display(p_hand, d_hand, 1)
  while more_cards == "y" or more_cards == "hit me":
    more_cards = input("Type 'y' to get another card. Type 'n' to stop. ").lower()
    if more_cards == "y" or more_cards == "hit me":
      p_hand = add_card(p_hand)
      display(p_hand, d_hand, 1)
    p_score = hand_value(p_hand)
    if p_score > 21:
      if 11 in p_hand:
        p_hand[p_hand.index(11)] = 1
      else:
        more_cards = "bust"
        break
  if more_cards != "bust":
    d_score = hand_value(d_hand)
    dealer = "fine"
    while d_score < 17:
      add_card(d_hand)
      d_score = hand_value(d_hand)
      if d_score > 21:
        if 11 in d_hand:
          d_hand[d_hand.index(11)] = 1
        else:
          dealer = "bust"
          break
  display(p_hand, d_hand, 0)
  if more_cards == "bust":
    print("You lose!")
  elif dealer == "bust":
    print("You win!")
  elif p_score > d_score:
    print("You win!")
  elif d_score > p_score:
    print("You lose!")
  else:
    print("It's a draw!")
  if input("Do you want to play again? type 'yes' or 'no'. ").lower() == "yes":
    play_game()

play = ""
while play != "yes" and play != "no":
  play = input("Do you want to play a game? Type 'yes' or 'no' ").lower()
  if play == "no":
    print("I didn't want to play with you either.")
  elif play != "yes":
    print("'yes' or 'no' only.\n")
  else:
    play_game()
print("Bye!")

