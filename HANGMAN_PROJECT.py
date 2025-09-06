#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hp
#
# Created:     17/08/2025
# Copyright:   (c) hp 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
from hangman_words import word_list,logo
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]


lives=6
print(logo)
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"

print(placeholder)

game_over= False
correct_letter=[]

while not game_over:
    print(f"{lives}/6 lives left")
    guess=input("guess a letter: ").lower()

    if guess in correct_letter:
        print(f"you've already guessed {guess}")
    display=""
    for letter in chosen_word:
        if letter==guess:
            display +=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display +="_"

    print("word to guess: " + display)

    if guess not in chosen_word:
        lives-=1
        print(f"you've guessed {guess}, that's not in the word.You lose a life")
        if lives==0:
            game_over=True
            print(f"it was {chosen_word}! you lose")

    if "_" not in display :
        game_over= True
        print("you win")

    print(stages[lives])
