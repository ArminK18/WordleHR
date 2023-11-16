import random
from colorama import init, Fore, Style
import time

init()

filename = "words.txt"

words = []

with open(filename, 'r') as f:
    for line in f:
        words_in_line = line.strip().split()
        lowercased_words = [word.lower() for word in words_in_line]
        words.extend(lowercased_words)

input_word = "....."

# def check_letter(given_word):
#     for i in range(len(word)):
#         if given_word[i] in word_letters:
#             if given_word[i] == word_letters[i]:
#                 print(f"{Fore.GREEN}{given_word[i]}{Style.RESET_ALL}", end=' ')
#             else:
#                 print(f"{Fore.YELLOW}{given_word[i]}{Style.RESET_ALL}", end=' ')
#         else:
#             print(f"{Fore.WHITE}{given_word[i]}{Style.RESET_ALL}", end=' ')
#     print("\n")

def check_letter(given_word):
    color_map = {True: Fore.GREEN, False: Fore.YELLOW}
    for i in range(len(word)):
        color = color_map[given_word[i] == word_letters[i]] if given_word[i] in word_letters else Fore.WHITE
        print(f"{color}{given_word[i]}{Style.RESET_ALL}", end=' ')
    print("\n")

tries = 0
again = 'y'

while again != 'n':
    used_letters = []
    word = random.choice(words)
    if len(word) != 5:
        print("Error in word length.")

    word_letters = []
    for letter in word:
        word_letters.append(letter)

    print(f"Enter a 5-letter word (enter {Fore.CYAN}Q{Style.RESET_ALL} to give up)")
    while input_word != word:
        input_word = input().lower()

        if input_word == 'q':
            print(f"Target word was: {Fore.GREEN}{word}{Style.RESET_ALL}")
            break
        
        if len(input_word) != 5 and not input_word.isalpha():
            print(f"You have entered a {str(len(input_word))}-letter non-alphabetic word! Try again.")
            continue

        if len(input_word) != 5:
            print(f"You have entered a {str(len(input_word))}-letter word! Try again.")
            continue

        if not input_word.isalpha():
            print("Only letters allowed! Try again.")
            continue

        check_letter(input_word)
        for letter in input_word:
            used_letters.append(letter)

        tries += 1
        if tries > 0 and input_word != word:
            print("Used letters: ", end='')
            for letter in sorted(set(used_letters)):
                if letter not in word_letters:
                    print(letter, end=' ')
            print("\n")
        
    if input_word == word:
        print("Bravo!")
        if tries == 1:
            print(f"Done in {tries} try!!!\n")
        else:
            print(f"Done in {tries} tries.\n")

    print(f"\nWanna play again ({Fore.CYAN}y{Style.RESET_ALL}/{Fore.CYAN}n{Style.RESET_ALL})? ", end='')
    again = input().lower()
    print("\n")

    if again not in ['y', 'n']:
        print(f"Type {Fore.CYAN}y{Style.RESET_ALL} or {Fore.CYAN}n{Style.RESET_ALL}!")
        again = input().lower()

    elif again == 'n':
        print("Thank you for playing!\n")
        time.sleep(2)