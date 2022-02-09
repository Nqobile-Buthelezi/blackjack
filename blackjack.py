import random
from art import logo

def deal_card():
  """Returns a random card from a list of cards."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card_list):
  """Returns the sum of all cards in a list, checks for a blackjack or that the sum of all cards does not exceed 21."""
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  if 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)

def compare(user_total, computer_total):
  """Returns the outcome of comparing the user's final hand and the computer's final hand, by declaring a draw, a winner or a disqualification result."""
  if user_total > 21 and computer_total > 21:
    return "You went over. You lose 😤"
  if user_total == computer_total:
    return "Draw 🙃"
  elif computer_total == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_total == 0:
    return "Win with a Blackjack 😎"
  elif user_total > 21:
    return "You went over. You lose 😭"
  elif computer_total > 21:
    return "Opponent went over. You win 😁"
  elif user_total > computer_total:
    return "You win 😃"
  else:
    return "You lose 😤"


def blackjack():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"You current hand is: {user_cards}, and your current score is {user_score}")
    print(f"The computer's first card is: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      another_card = input("Would you like to draw another card? Type 'y' for yes or 'n' for no: ")
      if another_card == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

  print(compare(user_score, computer_score))
      

while input("Would you like to play a game of blackjack? Type 'y' for yes and 'n' for no: ") == "y":
  blackjack()
  