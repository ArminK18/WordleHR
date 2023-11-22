import random
from colorama import init, Fore, Style

init()

def read_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [word.lower() for line in f for word in line.strip().split()]
    
color_map = {True: Fore.GREEN, False: Fore.YELLOW}

def check_letter(given_word, word_letters):
    for given_letter, word_letter in zip(given_word, word_letters):
        color = color_map[given_letter == word_letter] if given_letter in word_letters else Fore.WHITE
        print(f"{color}{given_letter}{Style.RESET_ALL}", end=' ')
    print("\n")

filename_words = "words.txt"
filename_valid_words = "valid_words.txt"

words = [word for word in read_words(filename_words) if len(word) == 5]
valid_words = set(word for word in read_words(filename_valid_words) if len(word) == 5)

word = random.choice(words)
word_letters = list(word)

tries = 0
used_letters = set()

print(f"Enter a 5-letter word (enter {Fore.CYAN}Q{Style.RESET_ALL} to give up)")

while True:
    input_word = input().lower()

    if input_word == 'q':
        print(f"Target word was: {Fore.GREEN}{word}{Style.RESET_ALL}")
        break

    if input_word not in valid_words:
        print("That is not a valid 5-letter word. Try again!")
        continue

    check_letter(input_word, word_letters)
    used_letters.update(input_word)

    tries += 1
    if input_word == word:
        print("Bravo!")
        print(f"Done in {tries} try!!!\n" if tries == 1 else f"Done in {tries} tries.\n")
        break
    else:
        print("Used letters:", ' '.join(sorted(used_letters - set(word_letters))), "\n")