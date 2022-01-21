from copy import copy
import json
import os
import copy

def check_if_word_is_possable(word, set_letters, wild_letters, bad_letters):
	# Get the number of unique letters in wild_letters dict
	unknown_letters = len(word) - len(set(wild_letters.values())) - len(set_letters)
	wild_letters = copy.deepcopy(wild_letters)
	set_letters = copy.deepcopy(set_letters)

	# Check if the word is possable
	for letter_pos in range(len(word)):
		letter = word[letter_pos]
		if letter in bad_letters:
			return False
		if letter_pos in set_letters.values() or letter in wild_letters.values():
			if letter_pos in set_letters and letter != set_letters[letter_pos]:
				return False
		
			if letter_pos in wild_letters:
				if wild_letters[letter_pos] == letter:
					return False
			else:
				# Get key of the letter
				for key in wild_letters.keys():
					if wild_letters[key] == letter:
						wild_letters[key] == "*"
		else:
			unknown_letters -= 1
			if unknown_letters < 0:
				return False
	return True
		

def find_best_choice(letters_in_position, words, set_letters, wild_letters, bad_letters):
	max_score = 0 
	max_word = ''

	for word in words:
		if check_if_word_is_possable(word, set_letters, wild_letters, bad_letters):
			score = 0
			for letter_pos in range(len(word)):
				letter = word[letter_pos]
				score += letters_in_position[letter_pos][letter]
			if score > max_score:
				max_score = score
				max_word = word
	return max_word

def parse_results(green_user_input, yellow_user_input, gray_user_input, set_letters, wild_letters,  bad_letters):
	for letter_pos in range(len(green_user_input)):
		letter = green_user_input[letter_pos]
		if letter is not "_":
			set_letters[letter_pos] = letter

	for letter_pos in range(len(yellow_user_input)):
		letter = yellow_user_input[letter_pos]
		if letter is not "_":
			if wild_letters[letter] is None:
				wild_letters[letter] = [letter_pos]
			else:
				wild_letters[letter].append(letter_pos)
	
	for letter_pos in range(len(gray_user_input)):
		letter = gray_user_input[letter_pos]
		if letter is not "_":
			bad_letters.append(letter)

	return set_letters, wild_letters, bad_letters
	

	


if __name__ == '__main__':
	# Read source.json
	with open('source.json') as json_file:
		data = json.load(json_file)

	words = data['words']

	letters_in_position = [{} for i in range(len(words[0]))]
	# Find the most common letter in each of the 5 positions
	for word in words:
		for i in range(len(word)):
			if word[i] in letters_in_position[i]:
				letters_in_position[i][word[i]] += 1
			else:
				letters_in_position[i][word[i]] = 1

	wild_letters = {}
	set_letters = {}
	bad_letters = []

	tried_word = find_best_choice(letters_in_position, words, set_letters, wild_letters, bad_letters)
	print(tried_word)
	print("Use _ as spaces")
	for i in range(len(words[0]) + 1): 
		# Get user input
		green_user_input = input('Enter Green letters: ')
		yellow_user_input = input('Enter Yellow letters: ')
		gray_user_input = input('Enter Gray letters: ')
		set_letters, wild_letters,  bad_letters = parse_results(green_user_input, yellow_user_input, gray_user_input, set_letters, wild_letters, bad_letters)
		tried_word = find_best_choice(letters_in_position, words, set_letters, wild_letters, bad_letters)
		print(tried_word)
		
		
	