import random
from Hangman_words import word_list
from Hangman_art import logo
from Hangman_art import stages

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
word_lenght = len(chosen_word)
for letter in range(word_lenght):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    #Check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!!!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost!!!")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!!!")
    print(stages[lives])