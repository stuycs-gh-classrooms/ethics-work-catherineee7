tictactoe = [
[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]  
]

column = input("P1: choose a column: ")
row = input("P1: choose a row: ")
XorO = input("P1: x or o: ")

column1 = input("P2: choose a column: ")
row1 = input("P2: choose a row: ")
XorO_1 = input("P2: x or o: ")

def tictactoeArray():
  for i in tictactoe:
    print(i)
def tictactoePlay():
  print("Some Info: The numbers are in index, so it starts at 0, if the game has been won, type end in columns to stop the prompts.")
  for i in range(4):
    if column == "end" or column1 == "end":
      break
    column = input("P1: choose a column: ")
    row = input("P1: choose a row: ")
    XorO = input("P1: x or o: ")
    tictactoe[int(row)][int(column)] = XorO
    tictactoeArray()
    column1 = input("P2: choose a column: ")
    row1 = input("P2: choose a row: ")
    XorO_1 = input("P2: x or o: ")
    tictactoe[int(row1)][int(column1)] = XorO_1
    tictactoeArray()
  column = input("P1: choose a column: ")
  row = input("P1: choose a row: ")
  XorO = input("P1: x or o: ")
  tictactoe[int(row)][int(column)] = XorO
  print(tictactoe)

tictactoePlay()
