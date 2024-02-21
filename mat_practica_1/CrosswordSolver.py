import os
from time import sleep
from random import shuffle
from time import time

# Autores: Adrián González (1636620), 
# Descripción: Este programa soluciona un crucigrama mediante backtracking y forward checking
# Fecha: 30/9/2023

class CrosswordSolver:
	"""
		Class that solves a crossword puzzle using backtracking and forward checking.
	"""
	__board = []
	__board_x = 0
	__board_y = 0
	__words = []
	__words_len = 0
	__options = {}
	__attempt = 0
	__time = 0
	__total_time = 0
	__linesToResolve = []
	__linesResolved = []
	__wordsUsed = []
 
 
	def __init__(self, name, options):
		"""
			Constructor of the class.
   
			:param name: Name of the crossword ("A" or "CB_v3").
			:param options: Options of the program.
		"""
		self.__initOptions(options)
		self.loadBoard(name)
		self.loadWords(name)
  
  
	def __initOptions(self, options):
		"""
			Initializes the options and completes the missing ones.

			:param options: Options of the program.
		"""
		if (type(options) != dict):
			raise TypeError("The options must be a dictionary.")
		self.__options = options
		if ("delay" not in options):
			self.__options["delay"] = 0
		if ("board_prefix" not in options):
			self.__options["board_prefix"] = "crossword_"
		if ("words_prefix" not in options):
			self.__options["words_prefix"] = "diccionari_"
		if ("debug" not in options):
			self.__options["debug"] = False
		if ("frames" not in options):
			self.__options["frames"] = False
		if ("deletion_frames" not in options):
			self.__options["deletion_frames"] = False
		if ("engine" not in options):
			self.__options["engine"] = "forward_checking"
		if ("randomize" not in options):
			self.__options["randomize"] = False
		if (type(self.__options["delay"]) != int):
			raise TypeError("The delay must be an integer.")
		if (type(self.__options["board_prefix"]) != str):
			raise TypeError("The board prefix must be a string.")
		if (type(self.__options["words_prefix"]) != str):
			raise TypeError("The words prefix must be a string.")
		if (type(self.__options["debug"]) != bool):
			raise TypeError("The debug must be a boolean.")
		if (type(self.__options["frames"]) != bool):
			raise TypeError("The frames must be a boolean.")
		if (type(self.__options["deletion_frames"]) != bool):
			raise TypeError("The deletion frames must be a boolean.")
		if (type(self.__options["engine"]) != str):
			raise TypeError("The engine must be a string.")
		if (self.__options["engine"] != "forward_checking" and self.__options["engine"] != "backtracking"):
			raise ValueError("The engine must be 'forward_checking' or 'backtracking'.")
		if (type(self.__options["randomize"]) != bool):
			raise TypeError("The randomize must be a boolean.")
		return


	def __checkBoard(self, board):
		"""
			Checks if the board is valid.
		
			:param board: Board to check.
		"""
		# Check if the board is a matrix
		if type(board) != list:
			raise TypeError("The board must be a matrix.")
		# Check if the board is empty
		if not board:
			raise ValueError("The board cannot be empty.")
		# Loop through the board
		for row in board:
			# Check if the row is a list
			if type(row) != list:
				raise TypeError("The board must be a matrix.")
			# Check if the board has the same length in all rows
			if len(row) != len(board[0]):
				raise ValueError("The board must have the same length in all rows.")
		return

  
	def loadBoard(self, board):
		"""
			Loads the board from a file or a matrix.
		
			:param board: Name of the crossword file/difficulty or the matrix.
			:return: The board matrix.
		"""
		if self.__options["debug"]:
			print("Loading board...")
		# Read the board from a file
		if type(board) == str:
			file = board
			# Initialize the board
			board = []
			# Read the file
			filename = self.__options["board_prefix"] + file + ".txt"
			if self.__options["debug"]:
				print("Reading file \"" + filename + "\"...")
			with open(filename, "r") as f:
				# Loop through the file and append the lines to the board
				for line in f:
					line = line.split()
					line = [int(-1) if cell == '#' else int(0) for cell in line]
					board.append(line)
		# Check if the board is valid
		self.__checkBoard(board)
		# Set the board
		self.__board = board
		self.__board_x = len(board[0])
		self.__board_y = len(board)
		return board
  
  
	def loadWords(self, words):
		"""
			Loads the words from a file or a list.
		
			:param words: Name of the words file/difficulty or the list.
			:return: The words list.
		"""
		if self.__options["debug"]:
			print("Loading words...")
		# Read the words from a file
		if type(words) == str:
			file = words
			# Initialize the words
			words = []
			# Read the file
			filename = self.__options["words_prefix"] + file + ".txt"
			if self.__options["debug"]:
				print("Reading file \"" + filename + "\"...")
			with open(filename, "r") as f:
				# Loop through the file and append the lines to the words
				for line in f:
					# Get the word
					word = line.strip()
					# Check if the word is valid
					if not word:
						continue
					word = word.upper()
					# Append the word to the words
					words.append(word)
    # Randomize the words
		if self.__options["randomize"]:
			if self.__options["debug"]:
				print("Randomizing words...")
			shuffle(words)
		# Add the words to the list
		self.__words = words
		self.__words_len = len(words)
		return words
  
  
	def printCrossword(self, board):
		"""
			Prints the crossword.
			
			:param board: Board to print.
		"""
		# Check if the board is valid
		self.__checkBoard(board)
		print()
		# Loop through the board
		for row in board:
			# Loop through the row
			for cell in row:
				# Print the cell
				if cell == -1:
					print("#", end = " ")
				elif cell == 0:
					print("·", end = " ")
				else:
					print(cell, end = " ")
			print()
		print()
		return


	def printAttempt(self, board):
		"""
			Print the attempt with information.
			
			:param board: Board to print.
		"""
		# Check if frames is enabled
		if not self.__options["frames"]:
			return
		# Print the iteration
		#print("\n\n\n\n\n\n\n\n\n\n\n\n")
		os.system("cls" if os.name == "nt" else "clear")
		print("Time: ", round(time() - self.__time), "s")
		print("Attempt: ", self.__attempt)
		print()
		self.printCrossword(board)
		# Delay the execution
		if self.__options["delay"] > 0:
			sleep(self.__options["delay"] / 1000)
		return


	def getAttempts(self):
		"""
			Returns the number of attempts.
	 
			:return: The number of attempts.
		"""
		return self.__attempt


	def getTime(self):
		"""
			Returns the execution time.
	 
			:return: The execution time.
		"""
		return self.__total_time



	def __copyBoard(self, board):
		"""
			Copies the board.
   
			:param board: Board to copy.
			:return: The copied board.
		"""
		# Initialize the copied board
		copied_board = []
		# Loop through the board
		for row in board:
			# Append the row to the copied board
			copied_board.append(row.copy())
		return copied_board


	def solve(self):
		"""
			Solves the crossword puzzle.
			
			:return: The solved crossword puzzle.
		"""
		# Reduce the words to the ones that can be inserted in the board
		words = []
		length = max(self.__board_x, self.__board_y)
		if self.__options["debug"]:
			print("Reducing words by length...")
		words = self.__reduceWordsByMaxLength(self.__words, length)
		# Initialize information
		self.__attempt = 0
		# Set the current execution time
		self.__time = time()
  	# Copy the board
		board = self.__copyBoard(self.__board)
		# Solve the crossword with the specified engine
		if self.__options["engine"] == "backtracking":
			board = self.__solveWithBacktracking(board, words)
		else:
			board = self.__solveWithForwardChecking(board, words)
		# Save the execution time
		self.__total_time = time() - self.__time
		# Return the result
		return board


	def __reduceWords(self, words, length, format = None):
		"""
			Reduces the words to the ones that have the specified length.
			
			:param words: Words to reduce.
			:param length: Length of the words.
			:param format: Format to match, none by default for no format. (ex: "A??B????")
			:return: The reduced words list.
		"""

		reduced_words = []
		for word in words:
			if len(word) == length:
				if format:
					if not self.__checkFormat(word, format):
						continue
				reduced_words.append(word)
		return reduced_words


	def __checkFormat(self, word, format):
		"""
			Checks if the word matches the format.
   
			:param word: Word to check.
			:param format: Format to match.
			:return: True if the word matches the format, false otherwise.
		"""

		if len(word) != len(format):
			return False
		for i in range(len(word)):
			if format[i] == "?":
				continue
			if word[i] != format[i]:
				return False
		return True
			


	def __reduceWordsByMaxLength(self, words, length):
		"""
			Reduces the words to the ones that have the specified length.
			
			:param words: Words to reduce.
			:return: The reduced words list.
		"""

		reduced_words = []
		for word in words:
			if len(word) <= length:
				reduced_words.append(word)
		return reduced_words


	def __getLines(self, board):
		"""
			Get the initial possitions of the lines to fill, with the length and direction.
   
			:param board: Board to solve.
			:return: The lines to fill.
		"""

		lines = []
		length = 0
		for y in range(len(board)):
			initial_x = -1
			x = 0
			length = 0
			word = ""
			while x <= self.__board_x:
				if x == self.__board_x or board[y][x] == -1:
					if length > 1:
						lines.append({
							"initial_position": (initial_x, y),
							"length": length,
							"direction": "H",
							"word": word,
							"exclude": [],
							"attempts": 0,
						})
					length = 0
					initial_x = -1
					word = ""
				else:
					if initial_x == -1:
						initial_x = x
					length += 1
					word += board[y][x] if board[y][x] != 0 else "?"
				x += 1
		for x in range(len(board[0])):
			initial_y = -1
			y = 0
			length = 0
			word = ""
			while y <= self.__board_y:
				if y == self.__board_y or board[y][x] == -1:
					if length > 1:
						lines.append({
							"initial_position": (x, initial_y),
							"length": length,
							"direction": "V",
							"word": word,
							"exclude": [],
							"attempts": 0,
						})
					length = 0
					initial_y = -1
					word = ""
				else:
					if initial_y == -1:
						initial_y = y
					length += 1
					word += board[y][x] if board[y][x] != 0 else "?"
				y += 1
		return lines


	def __solveWithBacktracking(self, board, words):
		"""
			Solve the crossword with backtracking algorithm
   
			:param board: Board to solve.
			:param words: Words to use.
			:return: The solved crossword puzzle, or false if it cannot be solved.
		"""

		if self.__options["debug"]:
			print("Solving with backtracking...")
		self.__linesToResolve = self.__getLines(board)
		self.__linesResolved = []
		self.__wordsUsed = []
		board = self.__solveLinesWithBacktrackingRecursive(board, words)
		return board


	def __solveLinesWithBacktrackingRecursive(self, board, words):
		"""
			Resolve the lines with backtracking algorithm
   
			:param board: Board to solve.
			:param words: Words to use.
			:return: The solved crossword puzzle, or false if it cannot be solved.
  	"""
		# Check if there are words to use
		if not words:
			return False
		# Get the first line to resolve
		line = self.__linesToResolve[0]
		# Get the line format
		lineFormat = self.__getLineFormat(board, line)
		# Check if the line format is excluded
		if lineFormat in line["exclude"]:
			return False
		# Get the words that match the line format
		reducedWords = self.__reduceWords(words, line["length"], lineFormat)
		# Loop through the words
		for word in reducedWords:
			# Check if the word has been used
			if word in self.__wordsUsed:
				continue
			# Add the word to the words used
			self.__wordsUsed.append(word)
			# Move the line to the lines resolved
			self.__linesResolved.append(line)
			self.__linesToResolve.remove(line)
			# Insert the word in the board
			board = self.__insertWord(board, line, word)
			# Print the iteration
			self.__attempt += 1
			self.printAttempt(board)
			# Check if there are no more lines to resolve
			if not self.__linesToResolve:
				return board
			# Order the lines to resolve by intersection
			self.__linesToResolve = self.__orderLinesToResolveByIntersection(self.__linesToResolve, line)
			# Order the lines to resolve by top left
			#self.__linesToResolve = self.__orderLinesToResolveByTopLeft(self.__linesToResolve)
			# Resolve the lines
			result = self.__solveLinesWithBacktrackingRecursive(board, words)
			# Check if the result is false
			if not result:
				# Remove the word from the words used
				self.__wordsUsed.remove(word)
				# Remove the line from the lines resolved
				self.__linesResolved.remove(line)
				self.__linesToResolve.append(line)
				# Increment the attempts
				line["attempts"] += 1
				# Remove the word from the board
				self.__removeWord(board, line, lineFormat)
				# Print the iteration
				if self.__options["deletion_frames"]:
					self.printAttempt(board)
				# Continue with the next word
				continue
			# Return the result
			return result
		# Add the line format to the line exclude
		line["exclude"].append(lineFormat)
		# Return false
		return False


	def __orderLinesToResolveByIntersection(self, linesToResolve, line):
		"""
			Order the lines to resolve by intersection.
   
			:param linesToResolve: Lines to resolve.
			:param line: Line to check the intersection.
			:return: The ordered lines to resolve.
		"""
		start = []
		end = []
		if line["direction"] == "H":
			lineStart = line["initial_position"]
			lineEnd = (line["initial_position"][0] + line["length"] - 1, line["initial_position"][1])
			for l in linesToResolve:
				if l["direction"] == "V":
					lStart = l["initial_position"]
					lEnd = (l["initial_position"][0], l["initial_position"][1] + l["length"] - 1)
					if lStart[0] >= lineStart[0] and lStart[0] <= lineEnd[0] and lStart[1] <= lineStart[1] and lEnd[1] >= lineStart[1]:
						start.append(l)
						continue
				end.append(l)
		else:
			lineStart = line["initial_position"]
			lineEnd = (line["initial_position"][0], line["initial_position"][1] + line["length"] - 1)
			for l in linesToResolve:
				if l["direction"] == "H":
					lStart = l["initial_position"]
					lEnd = (l["initial_position"][0] + l["length"] - 1, l["initial_position"][1])
					if lStart[1] >= lineStart[1] and lStart[1] <= lineEnd[1] and lStart[0] <= lineStart[0] and lEnd[0] >= lineStart[0]:
						start.append(l)
						continue
				end.append(l)
		lines = start + end
		return lines
 

	def __getLineFormat(self, board, line):
		"""
			Get the format of the line.
	 
			:param board: Board to solve.
			:param line: Line to get the format.
			:return: The format of the line.
		"""
		# Initialize the format
		format = ""
		# Get the initial position
		x, y = line["initial_position"]
		# Check the direction of the line
		if line["direction"] == "H":
			# Loop through the line
			for i in range(line["length"]):
				# Append the character to the format (Add ? if the cell is empty)
				format += board[y][x + i] if board[y][x + i] != 0 else "?"
		else:
			# Loop through the line
			for i in range(line["length"]):
				# Append the character to the format (Add ? if the cell is empty)
				format += board[y + i][x] if board[y + i][x] != 0 else "?"
		return format


	def __insertWord(self, board, line, word):
		"""
			Inserts the word in the board.
	 
			:param board: Board to solve.
			:param line: Line to insert the word.
			:param word: Word to insert.
		"""
		# Get the initial position
		x, y = line["initial_position"]
		# Check the direction of the line
		if line["direction"] == "H":
			# Loop through the line
			for i in range(line["length"]):
				# Set the cell
				board[y][x + i] = word[i]
		else:
			# Loop through the line
			for i in range(line["length"]):
				# Set the cell
				board[y + i][x] = word[i]
		return board


	def __removeWord(self, board, line, format = None):
		"""
			Removes the word from the board.
	 
			:param board: Board to solve.
			:param line: Line to remove the word.
			:param format: Format to delete only certain characters (marked as ?)
		"""
		# Get the initial position
		x, y = line["initial_position"]
		# Check the direction of the line
		if line["direction"] == "H":
			# Loop through the line
			for i in range(line["length"]):
				# Check if the format is not none
				if format:
					# Check if the character is marked as ?
					if format[i] != "?":
						continue
				# Set the cell
				board[y][x + i] = 0
		else:
			# Loop through the line
			for i in range(line["length"]):
				# Check if the format is not none
				if format:
					# Check if the character is marked as ?
					if format[i] != "?":
						continue
				# Set the cell
				board[y + i][x] = 0
		return
		


	def __solveWithForwardChecking(self, board, words):
		"""
			Resolve the lines with backtracking + forward checking + MRV heuristic
   
			:param board: Board to solve.
			:param words: Words to use.
			:return: The solved crossword puzzle, or false if it cannot be solved.
  		"""

		if self.__options["debug"]:
			print("Solving with backtracking and forward checking...")

		self.__linesToResolve = self.__getLines(board)
		self.__linesResolved = []
		self.__wordsUsed = []

		return self.__solveWithForwardCheckingRecursive(board, words)

	def __solveWithForwardCheckingRecursive(self, board, words):
		"""
			Resolve the lines with backtracking + forward checking + MRV heuristic
   
			:param board: Board to solve.
			:param words: Words to use.
			:return: The solved crossword puzzle, or false if it cannot be solved.
  		"""

		if not words:
			return False

		line = self.__selectMRV(board, words)
		if not line:
			return board  
	
		lineFormat = self.__getLineFormat(board, line)
		if lineFormat in line["exclude"]:
			return False

		reducedWords = self.__reduceWords(words, line["length"], lineFormat)
		for word in reducedWords:
			if word in self.__wordsUsed:
				continue

			self.__wordsUsed.append(word)
			self.__linesResolved.append(line)
			self.__linesToResolve.remove(line)
			board = self.__insertWord(board, line, word)
			self.__attempt += 1
			self.printAttempt(board)

			if not self.__linesToResolve:
				return board


			self.__linesToResolve = self.__orderLinesToResolveByIntersection(self.__linesToResolve, line)
			result = self.__solveWithForwardCheckingRecursive(board, words)

			if not result:
				self.__wordsUsed.remove(word)
				self.__linesResolved.remove(line)
				self.__linesToResolve.append(line)
				line["attempts"] += 1
				self.__removeWord(board, line, lineFormat)
				if self.__options["deletion_frames"]:
					self.printAttempt(board)
				continue


			if not self.__propagateConstraints(board, line):

				self.__wordsUsed.remove(word)
				self.__linesResolved.remove(line)
				self.__linesToResolve.append(line)
				line["attempts"] += 1
				self.__removeWord(board, line, lineFormat)
				if self.__options["deletion_frames"]:
					self.printAttempt(board)
				continue

			return result

		line["exclude"].append(lineFormat)
		return False
	
	def __propagateConstraints(self, board, current_line):
		"""
		Propagates word constraints between crossword lines to ensure that words
        inserted are valid for all lines affected by the current insertion.

		:param board: Board to solve.
		:param words: Words to use.
        :return: True if all constraints are met; False if any line has no valid words.
		"""

		for line in self.__linesToResolve:
			if line == current_line:
				continue


			if line["direction"] == "H":
				intersect_x = current_line["initial_position"][0] - line["initial_position"][0]
				intersect_y = current_line["initial_position"][1] - line["initial_position"][1]
			else:
				intersect_x = current_line["initial_position"][0] - line["initial_position"][0]
				intersect_y = current_line["initial_position"][1] - line["initial_position"][1]


			words_to_remove = []
			for word in line["words"]:
				if word[intersect_x] != board[current_line["initial_position"][1] + intersect_y][current_line["initial_position"][0] + intersect_x]:
					words_to_remove.append(word)

			for word in words_to_remove:
				line["words"].remove(word)

			if not line["words"]:
				return False  

		return True
	
	def __selectMRV(self, board, words):
		"""
        Selects the line with the Minimum Remaining Values (MRV) to prioritize it for word insertion.

        :param board: Crossword board.
        :param words: List of available words.
        :return: The line with the minimum MRV.
		"""

		mrv_line = None
		min_word_count = float('inf')
		for line in self.__linesToResolve:
			lineFormat = self.__getLineFormat(board, line)
			possible_words = self.__reduceWords(words, line["length"], lineFormat)
			if len(possible_words) < min_word_count:
				mrv_line = line
				min_word_count = len(possible_words)
		return mrv_line	
