import random
from colorama import init, Fore, Style

def main():
    init()

    # Read words from file
    def read_words(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return [word.lower() for line in f for word in line.strip().split()]
        except FileNotFoundError:
            print(f"{Fore.RED}Error{Style.RESET_ALL}: The file {filename} was not found.")
            return []
        except IOError:
            print(f"{Fore.RED}Error{Style.RESET_ALL}: There was an issue reading the file {filename}.")
            return []
        
    # Color map for coloring the letters
    color_map = {True: Fore.GREEN, False: Fore.YELLOW}

    # Check if the given letter is in the word
    def check_letter(given_word, word_letters):
        for given_letter, word_letter in zip(given_word, word_letters):
            color = color_map[given_letter == word_letter] if given_letter in word_letters else Fore.WHITE
            print(f"{color}{given_letter}{Style.RESET_ALL}", end=' ')
        print("\n")
    
    # Filenames for words and valid words
    filename_words = "words.txt"
    filename_valid_words = "valid_words.txt"

    # Read words and valid words and stores them in a list and in a set
    words = [word for word in read_words(filename_words) if len(word) == 5 and word.isalpha()]
    valid_words = set(word for word in read_words(filename_valid_words) if len(word) == 5 and word.isalpha())

    # Check if list is not empty and choose a random word from the list
    if not words or not valid_words:
        print(f"{Fore.RED}Error{Style.RESET_ALL}: The {'words file' if not words else 'valid words file'} is empty or does not contain any valid words.")
        return
    word = random.choice(words)
    word_letters = list(word)

    tries = 0
    used_letters = set()

    print(f"Enter a 5-letter {Style.BRIGHT}Croatian{Style.RESET_ALL} word (enter {Fore.CYAN}Q{Style.RESET_ALL} to give up)")

    # Do until the word is guessed or the user gives up
    while True:
        input_word = input().lower()

        # If the user gives up, print the word and break
        if input_word == 'q':
            print(f"Target word was: {Fore.GREEN}{word}{Style.RESET_ALL}")
            break
        
        # If the input is not a valid 5-letter word, print an error message and continue
        if input_word not in valid_words:
            print("That is not a valid 5-letter word. Try again!")
            continue
        
        # If the input is a valid 5-letter word, check if the letters are in the word
        check_letter(input_word, word_letters)
        used_letters.update(input_word)

        # If user guesses the word, print a message and break
        tries += 1
        if input_word == word:
            print("Bravo!")
            print(f"Done in {tries} try!!!\n" if tries == 1 else f"Done in {tries} tries.\n")
            break
        else:
            print("Used letters:", ' '.join(sorted(used_letters - set(word_letters))), "\n")

if __name__ == '__main__':
    main()