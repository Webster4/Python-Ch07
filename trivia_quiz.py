# Quiz about rules in mafia
# In program I used reading and saving data in txt file

import sys

def open_file(file_name, mode):
	"""Open file"""
	try:
		the_file = open(file_name, mode)
	except IOError as e:
		print("File opening causes error, sorry\n", e)
		input("\nPlease press enter to exit program")
		sys.exit()
	else:
		return the_file

def next_line(the_file):
	"""Returns next formatted line from file"""
	line = the_file.readline()
	line = line.replace("/", "\n")
	return line
	
def next_block(the_file):
	"""Read next block of text from file and returns four strings and list"""
	category = next_line(the_file)
	
	question = next_line(the_file)
	
	answers = []
	for i in range(4):
		answers.append(next_line(the_file))
	
	# Conversion answer by cut '\n' which is read from txt file
	correct = next_line(the_file)
	correct = correct.strip('\n')
	
	explanation = next_line(the_file)
	
	return category, question, answers, correct, explanation 
	
def welcome(title):
	"""welcome player"""
	print("Welcome in Trivia Game\n")
	print(title)
	
	
	
def main():
	trivia_game = open_file("cant_refuse.txt", "r")
	title = next_line(trivia_game)
	welcome(title)
	score = 0
	
	category, question, answers, correct, explanation = next_block(trivia_game)
	
	while category:
		print(category)
		print(question)
		for i in range(4):
			print(i+1,"-",answers[i])
		
		answer = input("Please provide a number of your answer ")
		
		# Checking if answer is good
		if answer == correct:
			print("\nCorrect answer!!!", end=" ")
			score += 1
		else:
			print("\nSorry. Your answer is not correct")
			
		print(explanation)
		print("Your current score is: ",score,"\n\n")
		
		# getting next block of text
		category, question, answers, correct, explanation = next_block(trivia_game)
	
	# Closing of txt file
	trivia_game.close()
	
	print("\nYour final score is ",score)
	print("\nThank you for your time spared for this game. Good bye!")
	
main()
	
	
input("\n\nPlease press enter to exit program")
	