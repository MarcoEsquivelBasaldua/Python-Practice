"""
Python is easy

Author: Marco Antonio Esquivel Basaldua
Project: 2
Date: 30/5/2021

Code Description:
    Hang man game is played.
    At the begining of the game 2-player or 1-player option must be chosen
    For player 1 mode english_words is required to install
        pip install english-words
    In 2 player mode every player has to enter the word for the other to guess,
    every player will have a chance to guess a word before the other.

    HAVE FUN !!!!!!!!!!!!
"""
import time
from english_words import english_words_set
from random import choice

patibulo = [[' ','_','_','_','_',' _',' '], [' ','|',' ',' ',' ','|',' '], [' ','|',' ',' ',' ',' ',' '], [' ','|',' ',' ',' ',' ',' '], [' ','|',' ',' ',' ',' ',' '], ['_','|','_',' ',' ',' ',' ']]
head = [2,5]
l_arm = [3,4]
r_arm = [3,6]
body = [3,5]
l_leg = [4,4]
r_leg = [4,6]

class HangMan:
    def __init__(self, word_to_guess):
        self.word = word_to_guess
        self.total_fails = 0
        self.word_len = len(word_to_guess)
        self.guessed_word = []
        for _ in range(self.word_len):
            self.guessed_word.append(' ')
        self.pat = [[' ','_','_','_','_',' _',' '], [' ','|',' ',' ',' ','|',' '], [' ','|',' ',' ',' ',' ',' '], [' ','|',' ',' ',' ',' ',' '], [' ','|',' ',' ',' ',' ',' '], ['_','|','_',' ',' ',' ',' ']]
        self.count_to_win = self.word_len

    def guess(self, guess_letter):
        found = False
        for i in range(self.word_len):
            if guess_letter == self.word[i]:
                found = True
                self.guessed_word[i] = guess_letter
                self.count_to_win -= 1

        if not found:
            self.total_fails += 1

    def draw_hang_man(self):
        if self.total_fails == 1:
            self.pat[head[0]][head[1]] = '0'
        elif self.total_fails == 2:
            self.pat[body[0]][body[1]] = '|'
        elif self.total_fails == 3:
            self.pat[r_arm[0]][r_arm[1]] = '\\'
        elif self.total_fails == 4:
            self.pat[l_arm[0]][l_arm[1]] = '/'
        elif self.total_fails == 5:
            self.pat[l_leg[0]][l_leg[1]] = '/'
        elif self.total_fails == 6:
            self.pat[r_leg[0]][r_leg[1]] = '\\'

        for row in self.pat:
            print(''.join(row))

        print('\n')
        for letter in self.guessed_word:
            if letter == ' ':
                print('_',end='')
            else:
                print(letter, end='')
            print(' ', end='')
        print('\n')
        print('\n')




mode = None

print('Select 1-player or 2-player mode')
mode = int(input('Type 1 for 1-player mode or 2 for 2-player mode  '))
if not(1<= mode <= 2):
    print('Error mode')
    time.sleep(3)
    print(chr(27) + "[2J")

if mode == 1:
    word = choice(list(english_words_set))
    hangMan = HangMan(word)

    while True:
        hangMan.draw_hang_man()
        l1 = input('Guess a letter ')
        hangMan.guess(l1)
        print(chr(27) + "[2J")
        hangMan.draw_hang_man()
        time.sleep(2)
        print(chr(27) + "[2J")

        if hangMan.count_to_win == 0:
            print('You are the winner')
            break

        if hangMan.total_fails == 6:
            print('You lose')
            break
    
    print('The word is:', word)

if mode == 2:
    word2 = input('Player 1 write your word ')
    hangMan2 = HangMan(word2)
    print(chr(27) + "[2J") 

    word1 = input('Player 2 write your word ')
    hangMan1 = HangMan(word1)
    print(chr(27) + "[2J")

    while(True):
        hangMan1.draw_hang_man()
        l1 = input('player 1, guess a letter ')
        hangMan1.guess(l1)
        print(chr(27) + "[2J")
        hangMan1.draw_hang_man()
        time.sleep(2)
        print(chr(27) + "[2J")


        hangMan2.draw_hang_man()
        l2 = input('player 2, guess a letter ')
        hangMan2.guess(l2)
        print(chr(27) + "[2J")
        hangMan2.draw_hang_man()
        time.sleep(2)
        print(chr(27) + "[2J")

        if hangMan1.count_to_win == 0 and hangMan2.count_to_win == 0:
            print('Both players have guessed correctly')
        elif hangMan1.count_to_win == 0:
            print('Player 1 is the winner')
        elif hangMan2.count_to_win == 0:
            print('Player 2 is the winner')

        if hangMan1.total_fails == 6 and hangMan2.total_fails == 6:
            print('Both players lose')
        elif hangMan1.total_fails == 6:
            print('Player 1 loses')
        elif hangMan2.total_fails == 6:
            print('Player 2 loses')

        if hangMan1.count_to_win == 0 or hangMan2.count_to_win == 0 or hangMan1.total_fails == 6 or hangMan2.total_fails == 6:
            break

    print('Word for player 1: ',word1)
    print('Word for player 1: ',word2)
