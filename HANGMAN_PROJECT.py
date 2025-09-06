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
from hangman_words import word_list,logo #imports word list and logo from a different python code file "hangman_word
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
chosen_word=random.choice(word_list) # chooses a random word from the list of words 
print(chosen_word)
placeholder="" # an empty string variable 
word_length=len(chosen_word) #counts the number of letters in the word
for position in range(word_length):
    placeholder+="_" # add _ = counted number of letters to our variable 

print(placeholder)

game_over= False 
correct_letter=[] # empty list to store guessed letters 

while not game_over: # loop runs till player has lives left and has not guessed the correct word 
    print(f"{lives}/6 lives left")
    guess=input("guess a letter: ").lower()

    if guess in correct_letter: # check for repeated guessed lestters 
        print(f"you've already guessed {guess}")
    
    display="" # empty string 
    for letter in chosen_word:
        if letter==guess:
            display +=letter # if the letter guessed is correct it is added to the display 
            correct_letter.append(guess) # letter added to the list
        elif letter in correct_letter: # checks if letter is already in list
            display+=letter # adds that letter to the display 
        else: #if wrong letter guessed 
            display +="_" #adds _ to the display 

    print("word to guess: " + display)

    if guess not in chosen_word: 
        lives-=1 # deducts a life from 6 lives 
        print(f"you've guessed {guess}, that's not in the word.You lose a life")
        if lives==0: # when all lives are over 
            game_over=True 
            print(f"it was {chosen_word}! you lose")

    if "_" not in display: # if all letters are guessed correctly 
        game_over= True 
        print("you win")

    print(stages[lives]) # prints the ASCII art corresponding to the number of lives left 

