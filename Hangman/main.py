import random

#Todo 1: Update the word list to use the 'Wordlist' from hangman.py

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


# Todo2 : Import the logo from hangman_art.py and print it at the start of the game

from hangman_art import logo
print(logo)

#Testing code
print(f'Psst, the solution is {chosen_word}.')

# create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Todo 3: If the user has entered a letter they've already guessed, print the letter and let them know
    if guess in display:
        print(f"You've already guesses {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter =chosen_word[position]
        # print(f"Current position: {position}\n
        # Current letter: {letter}\n
        # Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        # Todo4: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guesses {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game =True
            print("You loose.🤦‍♂️")

    #join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}") 

    # Check if user has got all letters
    if "_" not in display:
        end_of_game =True
        print("You win.😍")

    #  Todo4: Import the stages from hangman_art.py and make the error go away
    from hangman_art import stages
    print(stages[lives])

    
