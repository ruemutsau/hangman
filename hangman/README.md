Project Hangman
I created the Hangman project as a component of my AiCore Data Analytics training. In the classic game of hangman, one player thinks of a word, and the other player has a set number of attempts to guess it. This is an example of how the Hangman game is played: the player attempts to guess the word that the computer randomly selects from a pre-established list.

This project's primary goal was to review and practise fundamental Python syntax. Because it makes use of OOP principles, it is centred on the Hangman class, which has three methods:
__init__(self, word_list, num_lives=5), that initialises the attributes as indicated in the docstring;
check_letter(self, letter) -> None, that checks if the input letter provided by the user is in the random word;
ask_letter(self), that asks the user for a letter and checks if this letter has already been tried, and if the input is correct.


Being a command line application, the program can be executed using the Python3 hangman_solution.py command.


AiCore made available in a publicly accessible template the fundamental rules of the Hangman game. Milestone 1 (M1) was simple and is identified as # TODO 1 in the hangman.solution.py file. M1 essentially needed to change the ask_letter() method to ask the user to input a letter, save it in a variable named letter, and determine if the letter consisted of one or more characters.
letter = input("Please enter a letter: ")
if len(letter) != 1:
    print("Please, enter just one character")
    To test the code, the ask_letter() method can be called within the play_game() function. In case of a wrong input of more than one character
    
    To test the code, the ask_letter() method can be called within the play_game() function. In case of a wrong input of more than one character, the programme is instructed to print the following mess
This is an image of the message that is printed when the user enters an input of more than one character
