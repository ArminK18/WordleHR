def get_words_from_file(file_path):
    words = []

    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = line.strip().split()
            words.extend(words_in_line)

    return words

file_path = 'words.txt'
word_list = get_words_from_file(file_path)

print(word_list)
