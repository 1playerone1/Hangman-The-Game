import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

guess = input("Guess a letter: ").lower()

display = []

word_lenght = len(chosen_word)

for letter in range(word_lenght):
    display += "_"

for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)