from copy import copy
import json
import os
import copy

def check_if_word_is_possable(word, wild_letters, set_letters, bad_letters):
	unknown_letters = len(word) - len(wild_letters) - len(set_letters)
	wild_letters = copy.deepcopy(wild_letters)
	set_letters = copy.deepcopy(set_letters)

	# Check if the word is possable
	for letter_pos in range(len(word)):
		letter = word[letter_pos]
		if letter in bad_letters:
			return False
		if letter_pos in set_letters:
			if letter != set_letters[letter_pos]:
				return False
		elif letter in wild_letters.values():
			if letter_pos in wild_letters:
				if wild_letters[letter_pos] == letter:
					return False
				else:
					wild_letters.pop(letter_pos)
		else:
			unknown_letters -= 1
			if unknown_letters < 0:
				return False
	return True
		

def find_best_choice(letters_in_position, words, wild_letters, set_letters, bad_letters):
	max_score = 0 
	max_word = ''

	for word in words:
		if check_if_word_is_possable(word, wild_letters, set_letters, bad_letters):
			score = 0
			for letter_pos in range(len(word)):
				letter = word[letter_pos]
				score += letters_in_position[letter_pos][letter]
			if score > max_score:
				max_score = score
				max_word = word
	return max_word

def parse_results(user_input, tried_word, wild_letters, set_letters, bad_letters):
	for letter_index in range(len(user_input)):
		letter = user_input[letter_index]
		if letter == "_":
			bad_letters.append(tried_word[letter_index])
		elif letter.isupper():
			set_letters[letter_index] = letter
		elif letter.islower():
			wild_letters[letter_index] = letter
		else:
			raise ValueError("Invalid input")
	return wild_letters, set_letters, bad_letters
		
	


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

	tried_word = find_best_choice(letters_in_position, words, wild_letters, set_letters, bad_letters)
	print(tried_word)
	print("Enter letters that are in the correct position in capital letters, letters that are in the wrong position in lowercase letters, and incorrect with a '_'")
	for i in range(len(words[0]) + 1): 
		# Get user input
		user_input = input('Enter results: ')
		print(user_input)
		wild_letters, set_letters, bad_letters = parse_results(user_input, tried_word, wild_letters, set_letters, bad_letters)
		tried_word = find_best_choice(letters_in_position, words, wild_letters, set_letters, bad_letters)
		print(tried_word)
		
		
	