import random
from colorama import init, Fore, Style
import sys

def main():
    init()

    # Read words from file
    def read_words(filename: str) -> list[str]:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return [word.lower() for line in f for word in line.strip().split()]
        except FileNotFoundError:
            print(f"{Fore.RED}Greška{Style.RESET_ALL}: datoteka {filename} nije pronađena.")
            return []
        except IOError:
            print(f"{Fore.RED}Greška{Style.RESET_ALL}: nemoguće čitanje datoteke {filename}.")
            return []
        
    # Color map for coloring the letters
    color_map: dict[bool, str] = {True: Fore.GREEN, False: Fore.YELLOW}

    # Check if the given letter is in the word
    def check_letter(given_word: str, word_letters: list) -> None:
        for given_letter, word_letter in zip(given_word, word_letters):
            color= color_map[given_letter == word_letter] if given_letter in word_letters else Fore.WHITE
            print(f"{color}{given_letter.upper()}{Style.RESET_ALL}", end=" ")
        print("\n")
    
    # Filenames for words and valid words
    filename_words: str = "words.txt"
    filename_valid_words: str = "valid_words.txt"

    # Read words and valid words and stores them in a list and in a set
    words: list[str] = [word for word in read_words(filename_words) if len(word) == 5 and word.isalpha()]
    valid_words: set = set(word for word in read_words(filename_valid_words) if len(word) == 5 and word.isalpha())

    # Check if list is not empty and choose a random word from the list
    if not words or not valid_words:
        print(f"{Fore.RED}Greška{Style.RESET_ALL}: datoteka {'words file' if not words else 'valid words file'} je prazna ili ne sadržava nijednu valjanu riječ.")
        return
    word: str = random.choice(words)
    word_letters: list[str] = list(word)

    tries: int = 0
    used_letters: set = set()

    print(f"Unesi {Style.BRIGHT}hrvatsku{Style.RESET_ALL} riječ od 5 slova:")
    no_of_tries = 0

    # Do until the word is guessed or the user gives up
    guessed_words: list[str] = []
    while True:
        input_word: str = input().lower()
        guessed_words.append(input_word)

        # If the user gives up, print the word and break
        if no_of_tries == 5:
            print(f"Žao mi je. Tražena riječ bila je: {Fore.GREEN}{word}{Style.RESET_ALL}")
            break
        
        # If the input is not a valid 5-letter word, print an error message and continue
        if input_word not in valid_words:
            print("To nije valjana riječ. Pokušaj ponovno!")
            continue
        
        # If the word has already been guessed, print an error message and continue
        if input_word in guessed_words[:-1]:
            print("Već si probao tu riječ. Pokušaj ponovno!")
            continue
        
        # Erase the input line and print the colored guess
        sys.stdout.write('\033[1A\033[2K')
        sys.stdout.flush()
        check_letter(input_word, word_letters)
        used_letters.update(input_word)

        # If user guesses the word, print a message and break
        tries += 1
        if input_word == word:
            print("Bravo!")
            print(f"Riješeno iz {tries}. pokušaja!!!\n" if tries == 1 else f"Riješeno u {tries} pokušaja.\n")
            break
        else:
            print(f"({no_of_tries+1}) Iskorištena slova:", " ".join(sorted(used_letters - set(word_letters))), "\n")
        
        print("-------------------")
        no_of_tries += 1

if __name__ == "__main__":
    main()
