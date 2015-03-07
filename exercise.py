
# define a function that returns True if the year that is passed to it is a leap year and False otherwise
# a leap year is:
# - a year divisible by 4
# - a year that is divisible by 100 and 400
def is_leap_year(year):
	if (year) % 4 == 0:
		return True
	elif (year) % 100 == 0 and (year) % 400 == 0:
		return True	
	else: 
		return False

# define a function that returns True if the string parameter passed is a palindrome and False otherwise
# the definition of a palindrome is a word is when is the same when you switch the order ie. madam is a palindrome
def is_palindrome(some_string):
	for char in some_string:
		if some_string[0] == some_string[some_string.length - 1] and some_string[1] == some_string[some_string.length - 2]:
			return True
		else:
			return False


#Answer
def is_palindrome(some_string):
	left_index = 0 #defining variables; establish your parameters to work with; be bold in creating what you need to move forward and create logic!
	right_index = len(some_string) - 1 #len is a built in function
	while left_index < right_index:
		if some_string[left_index] != some_string[right_index]:
			return False
		left_index += 1
		right_index -= 1
	return True

# define a function that takes a list of integers and returns the largest of all the values
def mode(values):
	pass

# define a function that takes a list of integers and return the median of the values
# - the median is the middle element when the integers are in sorted order
# - if there is an even number of integers, it is the sum of the 2 middle numbers divided by 2
def median(values):
	pass

#Answer
def bubble_sort(values):
	i = 0
	while i < len(values):
		j = 0
		while j < len(values):
			if values[j] > values[i]:
				temp = values[i]
				values[i] = values[j]
				values[j] = temp
			j += 1
		i += 1

def median(values):
	bubble_sort(values)
	if len(values) % 2 = 0:
		return float(values[len(values) / 2 - 1] + values[len(values) / 2]) / 2
	else:
		return values[(len(values) / 2)]













# Steps
# 1. Same steps in the ComputerPlayer and the HumanPlayer
# 2. How to implement start to use the computer player the same as the human player
# 3. Defining the winning combinations for the game


# Rock, scissor, paper game
class ComputerPlayer:
	pass
	# 1a. Implement the method for which the player returns a combination
		# - store the available combinations
		# - generate a random combination, generate a number and using the value as index to a list


class HumanPlayer:
	pass
	# 2a. Implement the method for which the player returns a combination
		# - store the available combinations
		# - get the input and see if its in the available combinations, if it is valid, return the value, if it is not, ask for another input

class Game:
	def __init__(self, player1, player2): #Doesn't matter if these are human or computer players; if you are a human player, the implementation is typing your answer; if the player is a computer, the implementation is generating an answer
		self.player1 = player1
		self.player2 = player2
	def start(self): #start method
		# 1. Get the combination of player1
		# 2. Get the combination of player2
		# 3. Determine whether a player's combination beats another player

if __name__ == '__main__':
	player = HumanPlayer()
	computer = ComputerPlayer()
	game = Game(player, computer)
	# game = Game(player1, computer2)
	# game = Game(player1, player2)
	game.start()











