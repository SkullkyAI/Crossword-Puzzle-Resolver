import os
from CrosswordSolver import CrosswordSolver

# Ask the user for the crossword name
os.system("clear" if os.name == "posix" else "cls")
print("Welcome to the crossword solver!")
print("")
print("There are two crosswords available:")
print(" 1. \"CB_v3\": Simple crossword of 6x7")
print(" 2. \"A\": Complex crossword of 12x12")
print("\n")
num = input("Enter the number of the crossword: ")
# Check if the crossword number is empty
while num == "":
	num = input("No crossword number entered. Please enter the number of the crossword: ")
# Check if the crossword number is valid
while num != "1" and num != "2":
	num = input("Invalid crossword number entered. Please enter the number of the crossword: ")
# Set the crossword name
if num == "1":
	crosswordName = "CB_v3"
else:
	crosswordName = "A"
 
os.system("clear" if os.name == "posix" else "cls")
print("Crossword \"" + crosswordName + "\" selected.")
print("")
print("There are two algorithms available:")
print(" 1. Backtracking")
print(" 2. Forward checking")
print("\n")
# Ask the user for the algorithm
num = input("Enter the number of the algorithm: ")
while num == "":
	num = input("No algorithm number entered. Please enter the number of the algorithm: ")
while num != "1" and num != "2":
	num = input("Invalid algorithm number entered. Please enter the number of the algorithm: ")
# Set the algorithm
if num == "1":
	algorithm = "backtracking"
else:
	algorithm = "forward_checking"
print("")
print("Algorithm \"" + algorithm + "\" selected.")
print("\n\n")

# Initialize the crossword solver
cs = CrosswordSolver(crosswordName, {
  "engine": algorithm,
  "randomize": True,
  "delay": 0,
  "debug": True,
  "frames": True,
  "deletion_frames": True,
})
# Solve the crossword
res = cs.solve()

# Print the result
time = round(cs.getTime(), 4)
attempts = cs.getAttempts()
os.system("clear" if os.name == "posix" else "cls")
if res == False:
	print("The crossword could not be solved.")
else:
	print("The crossword has been solved!")
print("")
print("Time: " + str(time) + " seconds")
print("Attempts: " + str(attempts))
if res != False:
	cs.printCrossword(res)	