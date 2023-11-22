def check_letter(given_word, word_letters):
    for given, word in zip(given_word, word_letters):
        print(given, word)

check_letter('apasi', ['a', 'p', 'a', 's', 'i'])