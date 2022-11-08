# creating hangman game without visuals
import string
import words

# filtering the words which contain - or space

# def filtering(words):
#     word = random.choice(words)
#     while '-' in word or ' ' in words:
#         word = random.choice(words)
#
#     return word.upper()
# core of the projects don't mess it jal hero


print("Welcome to the Hangman Game.")


def start():
    word = words.filtering()
    word_letters = set(word)   # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   # what the user has guessed

    # starting life
    lives = 15

    while len(word_letters) > 0 and lives > 0:
        # joins the letter u have used

        print(f"You have {lives} live left and you have used these letter ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        # removing the - by right guessed letter

        print("Current word : ", " ".join(word_list))

        # process regarding the input
        user_input = input("Enter the letter :").upper()
        if user_input in alphabet - used_letters:  # it the valid char in alphabet is typed
            used_letters.add(user_input)  # it adds in used letter group
            if user_input in word_letters:  # if user input in given word than it removes that letter in keyboard option
                word_letters.remove(user_input)
                print("")
            else:
                lives -= 1
                print(f"{user_input} letter not in the word. Try next letter.")
        elif user_input in used_letters:
            print("You have already used this letter .Please try next letter.")
        else:
            print("Invalid character")

    if lives == 0:
        print(f"You have used all your life. The word is {word} .")
    else:
        print(f"Congratulation, you have correctly guessed the word {word} correctly !!")


start()
