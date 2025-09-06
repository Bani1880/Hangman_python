# Hangman_python
Hangman Game 🎮

A classic command-line Hangman game built with Python.

Project Description:

This project is a simple, single-player Hangman game where you try to guess a hidden word one letter at a time. Each incorrect guess costs you a life, and a part of the hangman is drawn. The game is over when you either guess the word correctly or run out of lives.

Features:

Random Word Selection: The game chooses a random word from a predefined list.

Life System: You start with a set number of lives (6 in this game).

Visual Feedback: The hangman figure is drawn piece by piece with each wrong guess.

Input Validation: The game checks for duplicate guesses.

Code Structure:

HANGMAN_PROJECT.py: The main Python script that contains the game logic.

hangman_words.py: A separate file that holds the word_list and the logo for the game. This separation keeps the main script clean.

logo.py (assumed): This file likely contains the ASCII art for the game's logo.
