import random
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6
for letter in chosen_word:
    display += "_"

print(hangman_art.logo)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")


    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(hangman_art.stages[lives])
