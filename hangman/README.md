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
All required functionalities implemented in M2 are marked in hangman_solution.py as # TODO 2. M2 required the initialisation of the program's attributes as required in the docstring. These were as below:

 def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.list_letters = []
        print(f"The mistery word has {self.num_letters} characters")
        print(f"{self.word_guessed}")


'apple', 'banana', 'orange', 'pear', 'strawberry', and 'watermelon' are among the six items in the word_list list that make up the attribute word of the string type that is given to a word selected at random by a computer from that list. I imported the random package in order to make this random pick possible. I chose to utilise the len() string function to create the word_guessed list attribute, which has as many '_' strings as there are characters in the word that was randomly selected. The integer number of distinct letters in the word that have not yet been guessed is stored in the variable num_letters. In order to accomplish this, I used the list() technique to first convert word into a list type. Then, I used len() on the unique letters inside the list.

To check whether the __init__ method worked, __init__(word_list) can be called within the play_game() function, thus initialising the messages seen in the introduction

As a bonus task, we were additionally invited to find a way to print diagrams that resembled the classic Handman drawings. My solution to the challenge was to create the following list of visuals, which I called self.list_visual.


self.list_visual = [
            '''
            __________
              |      |
              |    \ O /
              |      |
              |     /\\
            __|____
            ''',''' 
            __________
              |      |
              |      O
              |      |
              |     /\\
            __|____
            ''','''
             __________
              |      |
              |      O
              |      |
              |     /
            __|____
            ''','''
             __________
              |      |
              |      O
              |      |
              |
            __|____
            ''','''
             __________
              |      |
              |      O
              |
              |
            __|____
            ''']


            
