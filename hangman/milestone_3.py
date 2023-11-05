words = ["apple", "banana", "cherry", "date", "elderberry"]
while True:
  guess = input("Guess a letter: ")
if len(guess) == 1 and guess.isalpha():
   break
    else:
 print("Invalid letter. Please, enter a single alphabetical character.")
def check_guess(guess):
  guess = guess.lower()
if guess in words:
        return True
    else:
        return False
      def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    if check_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid guess.")
