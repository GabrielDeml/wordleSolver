import json


def check_if_word_is_possable(word, set_letters, wild_letters, bad_letters):
    # Get the number of unique letters in wild_letters dict
    set_letters_count = 0
    wild_letters_count = 0
    set_letters = set_letters.copy()
    wild_letters = wild_letters.copy()

    # Check if the word is possable
    for letter_pos in range(len(word)):
        letter = word[letter_pos]

        if letter_pos in set_letters.keys():
            set_letters_count += 1
            if letter in wild_letters.keys():
                wild_letters_count += 1
            if letter != set_letters[letter_pos]:
                return False
        elif letter in wild_letters.keys():
            for letter_pos_tmp in wild_letters[letter]:
                if letter_pos == letter_pos_tmp:
                    return False
            wild_letters_count += 1
        elif letter in bad_letters:
            return False
    if set_letters_count == len(set_letters) and wild_letters_count >= len(wild_letters):
        return True
    else:
        return False


def find_best_choice(letters_in_position, letter_count, words, set_letters, wild_letters, bad_letters):
    max_score_letter_count = 0
    max_word_letter_count = ""
    max_score_duplicate = 0
    max_word_duplicate = ''
    max_score = 0
    max_word = ''

    for word in words:
        if check_if_word_is_possable(word, set_letters, wild_letters, bad_letters):
            score = 0
            score_global_letter_count = 0
            duplicate_letters = {}
            for letter_pos in range(len(word)):
                letter = word[letter_pos]
                if letter in duplicate_letters:
                    duplicate_letters[letter] += 1
                else:
                    duplicate_letters[letter] = 1
                score += letters_in_position[letter_pos][letter]
                score_global_letter_count += letter_count[letter]
            if max(duplicate_letters.values()) > 1:
                if score > max_score_duplicate:
                    max_score_duplicate = score
                    max_word_duplicate = word
            else:
                if score > max_score:
                    max_score = score
                    max_word = word
                if score_global_letter_count > max_score_letter_count:
                    max_score_letter_count = score_global_letter_count
                    max_word_letter_count = word

    best_word = max_word_letter_count
    if len(set_letters) + len(wild_letters) >= 3:
        best_word = max_word_duplicate
    return max_word, max_word_duplicate, max_word_letter_count, best_word


def parse_results(green_user_input, yellow_user_input, gray_user_input, set_letters, wild_letters,  bad_letters):
    for letter_pos in range(len(green_user_input)):
        letter = green_user_input[letter_pos]
        if letter != "_":
            set_letters[letter_pos] = letter


    for letter_pos in range(len(yellow_user_input)):
        letter = yellow_user_input[letter_pos]
        if letter != "_":
            if letter in wild_letters and not letter_pos in wild_letters[letter]:
                wild_letters[letter].append(letter_pos)
            else:
                wild_letters[letter] = [letter_pos]

    for letter_pos in range(len(gray_user_input)):
        letter = gray_user_input[letter_pos]
        if letter != "_":
            bad_letters.append(letter)

    return set_letters, wild_letters, bad_letters


if __name__ == '__main__':
    # Read source.json
    with open('source.json') as json_file:
        data = json.load(json_file)

    words = data['words']

    letters_in_position = [{} for i in range(len(words[0]))]
    letter_count = {}
    # Find the most common letter in each of the 5 positions
    for word in words:
        for i in range(len(word)):
            if word[i] in letters_in_position[i]:
                letters_in_position[i][word[i]] += 1
            else:
                letters_in_position[i][word[i]] = 1
            if word[i] in letter_count:
                letter_count[word[i]] += 1
            else:
                letter_count[word[i]] = 1

    wild_letters = {}
    set_letters = {}
    bad_letters = []

    tried_word, tried_word_duplicate, tried_word_letter_count, best_word = find_best_choice(
        letters_in_position, letter_count, words, set_letters, wild_letters, bad_letters)
    print("Start word: " + tried_word)
    print("Start word duplicate: " + tried_word_duplicate)
    print("Start word global letter count: " + tried_word_letter_count)
    print("Best word: " + best_word)
    print("Use _ as spaces")
    for i in range(len(words[0])):
        # Get user input
        green_user_input = input('Enter Green letters: ')
        yellow_user_input = input('Enter Yellow letters: ')
        gray_user_input = input('Enter Gray letters: ')
        set_letters, wild_letters,  bad_letters = parse_results(
            green_user_input, yellow_user_input, gray_user_input, set_letters, wild_letters, bad_letters)
        tried_word, tried_word_duplicate, tried_word_letter_count, best_word = find_best_choice(
            letters_in_position, letter_count, words, set_letters, wild_letters, bad_letters)
        print("Next word: " + tried_word)
        print("Next word duplicate: " + tried_word_duplicate)
        print("Next word global letter count: " + tried_word_letter_count)
        print("Best word: " + best_word)
