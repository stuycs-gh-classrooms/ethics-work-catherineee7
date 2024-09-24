tictactoe = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]  
]

# column = input("P1: choose a column: ")
# row = input("P1: choose a row: ")
# XorO = input("P1: x or o: ")

# column1 = input("P2: choose a column: ")
# row1 = input("P2: choose a row: ")
# XorO_1 = input("P2: x or o: ")

def win(tictactoe):
	for row in range(0,3):
    	if tictactoe[row][0] == "x" and tictactoe[row][1] == "x" and tictactoe[row][2] == "x" or tictactoe[row][0] == "o" and tictactoe[row][1] == "o" and tictactoe[row][2] == "o":
        	return True
	for col in range(0,3):
    	if tictactoe[0][col] == "x" and tictactoe[1][col] == "x" and tictactoe[2][col] == "x" or tictactoe[0][col] == "o" and tictactoe[1][col] == "o" and tictactoe[2][col] == "o":
        	return True
	if tictactoe[0][0] == "x" and tictactoe[1][1] == "x" and tictactoe[2][2] == "x"  or tictactoe[0][0] == "o" and tictactoe[1][1] == "o" and tictactoe[2][2] == "o":
    	return True
	if tictactoe[0][2] == "x" and tictactoe[1][1] == "x" and tictactoe[2][0] == "x" or tictactoe[0][2] == "o" and tictactoe[1][1] == "o" and tictactoe[2][0] == "o":
    	return True
def tictactoeArray():
  for i in tictactoe:
	print(i)
def tictactoePlay():
  column = ""
  column1 = ""
  print("Some Info: The numbers are in index, so it starts at 0, if the game has been won, type end in columns to stop the prompts.")
  for i in range(4):
	if win(tictactoe) == True:
  	print("You win! :)")
  	break
	column = input("P1: choose a column: ")
	row = input("P1: choose a row: ")
	XorO = input("P1: x or o: ")
  if tictactoe[int(row)][int(column)] == "x" or tictactoe[int(row)][int(column)] == "o":
    print("Someone has already marked this square, try another)
  else:
	  tictactoe[int(row)][int(column)] = XorO_1
	tictactoeArray()
	column1 = input("P2: choose a column: ")
	row1 = input("P2: choose a row: ")
	XorO_1 = input("P2: x or o: ")
  if tictactoe[int(row1)][int(column1)] == "x" or tictactoe[int(row1)][int(column1)] == "o":
    print("Someone has already marked this square, try another)
  else:
	  tictactoe[int(row1)][int(column1)] = XorO_1
	tictactoeArray()
  column = input("P1: choose a column: ")
  row = input("P1: choose a row: ")
  XorO = input("P1: x or o: ")
  tictactoe[int(row)][int(column)] = XorO
  print(tictactoe)

tictactoePlay()
