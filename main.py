import json
import os

def check_if_word_is_possable(word_tried, word):

	# Create data structure to store the possable letters
	unknown_letters = 0
	wild_letters = []
	set_letters = {}
	for i in range(len(word_tried)):
		if word_tried[i] == '_':
			unknown_letters += 1
		if word_tried[i].islower():
			wild_letters.append(word_tried[i])
		if word_tried[i].isupper():
			set_letters[i] = word_tried[i]

	
	# Check if the word is possable
	for letter in word:
		if letter in set_letters:
			if letter != set_letters[letter]:
				return False
		elif letter in wild_letters:
			wild_letters.remove(letter)
		else:
			unknown_letters -= 1
			if unknown_letters < 0:
				return False
	return True
		

def find_next_word(words_tried, position_index):
	possable_words = {}

	# This gives us the possable word with the letters in the set position aka the upper case letters
	for word_tried in words_tried:
		possable_words_given_single_word  = {}
		for i in range(len(word_tried)):
			# if the letter is capitalized
			if word_tried[i].isupper():
				# Get possible words from position_index
				for word in position_index[i][word_tried[i]]:
					if check_if_word_is_possable(word_tried, word):
						# Add to possable_words_given_single_word
						if word not in possable_words_given_single_word:
							possable_words_given_single_word[word] = 1
						else:
							possable_words_given_single_word[word] += 1
			if word_tried[i].islower():
				for i in len(word_tried):
					if word in position_index[i][word_tried[i]]:
						if word not in possable_words_given_single_word:
							possable_words_given_single_word[word] = 1
						else:
							possable_words_given_single_word[word] += 1
			
			for word in possable_words_given_single_word:
				if word >= len(word_tried):
					if word not in possable_words:
						possable_words[word] = possable_words_given_single_word[word]
					else:
						possable_words[word] += possable_words_given_single_word[word]

		return possable_words
				

def sort_most_common_letters(letters_in_position):
	# Sort the letters in position
	return_list = [[] for i in range(len(letters_in_position[]))]
	for letter in letters_in_position:
		


if __name__ == '__main__':
	# Read source.json
	with open('source.json') as json_file:
		data = json.load(json_file)

	words = data['words']

	letters_in_position = [{} for i in range(len(words[0]))]
	position_index = [{} for i in range(len(words[0]))]
	# Find the most common letter in each of the 5 positions
	for word in words:
		for i in range(len(word)):
			if word[i] in letters_in_position[i]:
				letters_in_position[i][word[i]] += 1
				position_index[i][word[i]].append(word)
			else:
				letters_in_position[i][word[i]] = 1
				position_index[i][word[i]] = [word]

	# Print the most common letter in each of the 5 positions

	startword = ''
	for i in range(len(letters_in_position)):
		most_common_letter = max(letters_in_position[i], key=letters_in_position[i].get)
		startword += most_common_letter

	print(f'The most common letters are: {startword}')

	# Find word closest to the startword
	possable_words = {}
	for i in range(len(startword)):
		possable_words_tmp = position_index[i][startword[i]]
		for word in possable_words_tmp:
			if word in possable_words:
				possable_words[word] += 1
			else:
				possable_words[word] = 1

	max_matching_word = max(possable_words, key=possable_words.get)
	print(f'The word closest to the startword is: {max_matching_word}')

	print("Enter letters that are in the correct position in capital letters, letters that are in the wrong position in lowercase letters, and incorrect with a '_'")
	words_tried = []
	for i in range(len(startword) + 1):
		# Get input from user
		while True:
			try:
				user_input = input()
				if user_input == "_____":
					# Find the second most common letter in each of the 5 positions
					for i in range(len(startword)):
						# Get the second most common letter in each of the 5 positions

						most_common_letter = max(letters_in_position[i], key=letters_in_position[i].get)
						startword = startword[:i] + most_common_letter + startword[i+1:]
				if len(user_input) == len(startword):
					break
			except:
				print("Invalid input")
				continue
		
		words_tried.append(user_input)
		# Find the next word
		next_word = find_next_word(words_tried, position_index)
		print(f'The next word is: {next_word}')