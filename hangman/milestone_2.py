import random
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_word = random.choice(words)
print (words)
print(random_word)
letter = input("Please enter a single letter: ")
guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
  print("Good guess!")
else:
  print("Oops! That is not a valid input.")
