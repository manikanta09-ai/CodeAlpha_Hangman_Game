import random

# Predefined list of 5 words
word_list = ['python', 'hangman', 'codealpha', 'intern', 'project']

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Display settings
display = ['_' for _ in range(word_length)]
guessed_letters = []
attempts = 6

print(" Welcome to Hangman Game!")
print("Guess the word. You have 6 incorrect guesses allowed.\n")

while attempts > 0 and '_' in display:
    print("Current word:", ' '.join(display))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try another.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(" Good guess!\n")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}\n")

if '_' not in display:
    print(" Congratulations! You guessed the word:", chosen_word)
else:
    print(" Game Over! The correct word was:", chosen_word)