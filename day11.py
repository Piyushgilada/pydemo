import random


def deal_card():
    """return a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


user_card = []
computer_card = []
is_game_over = False
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)
print(f" your card {user_card} and score :{user_score}")
print(f" computer first card :{computer_card[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
else:
    user_should_deal = input("type 'y' to draw another card ,type 'n' to pass:")
    if user_should_deal == 'y':
        user_card.append(deal_card())
    else:
        is_game_over == True
