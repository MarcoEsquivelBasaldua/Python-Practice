"""
Python is easy

Author: Marco Antonio Esquivel Basaldua
Project: 3
Date: 13/6/2021

Code Description:
    Play the card game crazy eights
    This game is for 2 to 5 players

    To check the rules go to  https://gamerules.com/rules/crazy-eights-card-game/ and https://www.youtube.com/watch?v=iDQjn3k76Mw
    Rules are available during the game.

    Passing and picking from deck are made automatically.

    HAVE FUN !!!!!!!!!!!!
"""
from random import shuffle
from numpy import argmin

deck = []

suits = ['Hearts','Tiles','Clovers','Pikes']
letters = ['A','J','Q','K']
for s in suits:
    for l in letters:
        deck.append(tuple((s,l)))

    for i in range(2,11):
        deck.append(tuple((s,i)))


rules = [
    '                        Crazy Eights Rules\n', 
    'OBJECTIVE: The goal is to be the first player to get rid of all your cards.', 
    'NUMBER OF PLAYERS: 2-5 players',
    'NUMBER OF CARDS: 52 deck cards',
    'RANK OF CARDS: 8 (50 points); K, Q, J (court cards 10 points); A (1 point); 10, 9, 7, 6, 5, 4, 3, 2 (no jokers)',
    'TYPE OF GAME: Shedding-type',
    'AUDIENCE: Family/Kids\n',
    'HOW TO DEAL:',
    'After the deck has been correctly shuffled, the dealer must deal five cards to each player.',
    'The rest of the deck is placed in the center and the top card of the deck is flipped over for all players to see.', 
    'If an eight is flipped over, randomly place it back inside the deck and turn over another card.\n',
    'HOW TO PLAY:',
    'The player to the left of the dealer goes first. They have the option of either drawing a card or playing a card',
    'on top of the discard pile. To play a card, the card played must either match the suit or the rank of the card shown',
    'on the discard pile. If you don’t have a card that can be played, then you must draw one from the pile, you have',
    'three chances to pick a valid card otherwise you will have to pass and keep the drawn cards. Once a player',
    'has either drawn (at most three times) from the pile or discarded, it then becomes the next players turn.\n',
    'Eights are wild. When a player plays an eight, they get to state the suit that gets played next. For example, you play',
    'an eight, you can state hearts as the next suit, and the player after you must play a heart.\n',
    'The first player to get rid of all their cards wins!\n',
    'NOTE:',
    'If the draw pile is gone and a player can not play, that player must pass. If every player can not play the round is',
    'over and every player gets the points of their unplayed cards according to the RANK OF CARDS. The player with the',
    'lowest points score is the winner.\n'
    'Type \'--resume\' to resume the game.\n',
    'Rules from: https://gamerules.com/rules/crazy-eights-card-game/ and https://www.youtube.com/watch?v=iDQjn3k76Mw']

def printRules():
    for line in rules:
        print(line)

def all_players_pass():
    scores = []
    for p in players:
        p_score = 0
        for card in p.hand:
            if card[1] == 'A':
                p_score += 1
            elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
                p_score += 10
            elif card[1] == 8:
                p_score += 50
            else:
                p_score += card[1]
        scores.append(p_score)

        print(p.name + ' ' + 'score is ' + str(p_score))

    print('\nThe winner is ' + players[argmin(scores)].name)

def pass_turn(current_player):
    current_player += 1
    if current_player == TOTAL_PLAYERS:
        current_player = 0
    
    return current_player


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

# Game
TOTAL_PLAYERS = 0

while True:
    TOTAL_PLAYERS = int(input('Enter the number of players '))

    if 1<= TOTAL_PLAYERS <= 5:
        break
    
    print('Invalid number of players. Playes must be in the range 1-5')

players = []
for i in range(1,TOTAL_PLAYERS+1):
    name = input('Enter player ' + str(i) + ' name ')
    players.append(Player(name))

#print(players[0].name)
# Deck is shuffled
shuffle(deck)

# Five cards are dealed to each player
for p in players:
    hand = deck[0:5]
    p.hand =  hand

    for i in range(5):
        deck.pop(0)

# If first card is 8, suffle again
while deck[0][1] == 8:
    shuffle(deck)

playing_card = deck[0]
deck.pop(0)
current_player = 0
pass_times = 0
winner = False
while True:
    print(chr(27) + "[2J")

    # Check winner when the deck is empty
    if not deck and pass_turn == TOTAL_PLAYERS:
        all_players_pass()
        break

    print('Current playing card: ' + str(playing_card))

    print(players[current_player].name + '\'s turn')
    print('These are your cards')

    playable = False
    for card in players[current_player].hand:
        print(card, end=' ')
        if card[0] == playing_card[0] or card[1] == playing_card[1] or card[1] == 8:
            playable = True

    if playable:
        pass_times = 0
        print('\nPick the card you want to play (they are ordered from 1 to the total cards you have) or type \'--help\' to print the rules')
        action = input()

        if action == '--help':
            printRules()
            while input() != '--resume':
                pass

        else:
            while True:
                try:
                    choosed_card = int(action) - 1

                    while True:
                        if players[current_player].hand[choosed_card][0] == playing_card[0] or players[current_player].hand[choosed_card][1] == playing_card[1] or players[current_player].hand[choosed_card][1] == 8:
                            playing_card = players[current_player].hand[choosed_card]
                            players[current_player].hand.pop(choosed_card)
                            break
                        else:
                            action = input('\nYou can not play that card, please choose another ')
                            choosed_card = int(action) - 1

                    if not players[current_player].hand:
                        print(players[current_player].name + ' is the winner')
                        winner = True

                    current_player = pass_turn(current_player)
                    break

                except ValueError:
                    print('Please enter a valid number')
                    action = input()
                except IndexError:
                    print('The card you try to use is out of index')
                    action = input()
            

    else:
        print('\nYou can not play with your hand, you have to pick a card or pass')
        if not deck:
            print('The deck is empty, you have to pass')
            current_player = pass_turn(current_player)
            pass_turn += 1
            input('Press any key+ENTER to end turn ')
        else:
            print('Picking from deck...')

            total_pick = 0
            while total_pick < 3:
                if deck:
                    if deck[0][0] == playing_card[0] or deck[0][1] == playing_card[1] or deck[0][1] == 8:
                        playing_card = deck[0]
                        deck.pop(0)
                        print('Current playing card: ' + str(playing_card))
                        break
                    else:
                        players[current_player].hand.append(deck[0])
                        deck.pop(0)
                
                total_pick += 1
                if total_pick == 2:
                    print('You have to pass')
            
            print('This is your hand now')
            print(players[current_player].hand)
            current_player = pass_turn(current_player)

            input('Press any key+ENTER to end turn ')

        
    if winner:
        break