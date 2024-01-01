    
import random
import os
from art import logo11

def clear_terminal():
    os.system('cls')


def deal_card():
    """값을 덱으로 반환"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw.'
    elif computer_score == 0:
        return 'Lose, opponent has Blackjack.'
    elif user_score == 0:
        return 'You win. Blackjack.'
    elif computer_score > 21:
        return 'You Win'
    elif user_score > 21:
        return 'You Lose.'
    elif user_score > computer_score:
        return 'You win'
    else:
        return 'You Lose'


def play_game():
    print(logo11)
    game_over = False
    user = []
    computer = []

    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not game_over:

        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f'Your Card: {user} ,Score : {user_score}')
        print(f' Computer : {computer[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input('카드를 받을래? y or n : \n')
            if user_should_deal == 'y':
                user.append(deal_card())
            elif user_score > 21:
                game_over = True
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f'  Your final hand :{user}, score : {user_score}')
    print(f'  Computer final hand :{computer}, score : {computer_score}')
    print(compare(user_score, computer_score))


while input('Do you want Blackjack? y or n: \n') == 'y':
  clear_terminal()
  play_game()