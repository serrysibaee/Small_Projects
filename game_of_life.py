# game of life with command (code for github)
# clean the output problem semi-solved maybe we need to use local computer
# inspired by tsoding implementation in Ada https://github.com/tsoding/ada-gol
# after some debugging in python we need to put more effort for the count_ngbrs() with mod
# and in the next() unlike the video where it is handled by the language it self
# also thanks to https://github.com/mwharrisjr/Game-of-Life/blob/master/script/main.py (for python help)
# source from wiki https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

from numpy.core.multiarray import ndarray
import time
import numpy as np
import sys
import os

rows:int = 50
cols:int = 50
ALIVE = "O"
DEAD = "."
# make the sybmol as option
# make the code as function to be more fun and useable
def render_board(board:ndarray):
  for row in range(rows):
    for col in range(cols):
      cell_val = board[row][col]
      if cell_val == 1:
        print(ALIVE, end=" ")
      if cell_val == 0:
        print(DEAD, end=" ")
    print()

def count_ngbrs(board, row_n, col_n)-> int:
  n_ng = 0
  # range for neighbours: -1,0,1 --> [-1,1] in N
  for i in range(-1,2):
    for j in range(-1,2):
      if not (i == 0 and j == 0):
        n_ng += board[(row_n + i) % rows][(col_n + j) % cols]
        # print(i,j)

  return n_ng

# this will return next state of the board
def next(board) -> ndarray:
  result = np.zeros((rows,cols))
  for row in range(rows):
    for col in range(cols):
      n = count_ngbrs(board, row, col)
      # if current cell is alive
      if board[row][col] == 1:
        result[row][col] = 1 if 2 <= n <= 3 else 0
      # if current cell is dead
      elif board[row][col] == 0:
        result[row][col] = 1 if n == 3 else 0
      # change in cells
  return result



# the board
# we could start with random state
board = np.random.randint(0,2,(rows,cols))

# OR we could start with pre known state (that goes to infinity)
#board = np.zeros((rows,cols))
#board[0][1] = 1;board[1][2] = 1;board[2][0] = 1;board[2][1] = 1;board[2][2] = 1;
# render_board(board)

# render_board(board)
for i in range(1000):
  render_board(board)
  board = next(board)
  time.sleep(0.05)
  #output.clear() # should be replaces with the system clearning command
  os.system("cls")

# count_ngbrs(board, 4, 4)