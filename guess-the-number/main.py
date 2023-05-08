import random
import os
from art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(logo)
print("Welcome to the Number Guessing Game!")
again = "yes"
while again == "yes":
  number = random.randint(1, 100 )
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
  correct = False
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5
  print(f"You have {attempts} attempts.")
  while attempts > 0 and correct == False:
    guess = int(input("Make a guess: "))
    if guess > number:
      attempts -= 1
      print(f"Too high. You have {attempts} attempts left.")
    elif guess < number:
      attempts -= 1
      print(f"Too low. You have {attempts} attempts left.")
    else:
      print(f"You got it! The answer was {guess}!")
      correct = True
  if attempts == 0:
    print("No more attempts. You lost.")
  again = input("Do you want to play again? Type 'yes' or 'no'. ").lower()
  if again == "yes":
    cls()
    continue
  else:
    again == "no"