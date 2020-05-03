import numpy as np
import random

def possible(x: int, y:int, n:int, grid):

  row = grid[x,:]
  column = grid[:,y]

  if grid[x,y] != 0 or n > 9:
    return False

  if n in row:
    return False
  
  if n in column:
    return False


  x0_square = (x//3)*3
  y0_square = (y//3)*3

  square = grid[x0_square : x0_square+3, y0_square : y0_square+3,]

  if n in square:
    return False

  return True


def verify(grid):

  grid = np.asarray(grid)
  for x in grid:
    if np.sum(x) == 45:
      u, index = np.unique(x, return_inverse =True)
      if u[np.bincount(index) > 1].size > 0:
        return False
    else:
      return False
  #print('Pass Rows')

  for y in grid.transpose():
    pass
    if np.sum(y) == 45:
      u, index = np.unique(y, return_inverse =True)
      if u[np.bincount(index) > 1].size > 0:
        return False
    else :
      return False
  #print('Pass Columns')
  
  for x in range(0,9,3):
    for y in range(0,9,3):
      square = grid[x : x+3, y : y+3]
      if np.sum(square) == 45:
        u, index = np.unique(x, return_inverse =True)
        if u[np.bincount(index) > 1].size > 0:
          return False
      else:
        return False
  #print('Pass Squares')
  return True


def solve(grid):

  x,y = np.where(grid == 0)
  coordinates = list(zip(x,y))

  for i in coordinates:
    rand_array = [1,2,3,4,5,6,7,8,9]
    random.shuffle(rand_array) #usefulll for the generation of sudoku
    for n in rand_array:
      if possible(i[0], i[1], n, grid):
        grid[i[0], i[1]] = n
        solve(grid)
        if not verify(grid):
          grid[i[0], i[1]] = 0
        else:
          return grid
    return 
  return grid


def generate(level=1):

  if level == 1:
    remove = 45
  elif level == 2:
    remove = 50
  elif level == 3:
    remove = 60
  else:
    remove = 70

  new_grid = np.matrix(np.zeros(81, dtype=int).reshape(9,9))

  new_grid = solve(new_grid)
  remove_indexes = random.sample(range(0,81), remove)
  
  new_grid = new_grid.reshape(1,81)
  #print(new_grid)
  for index in remove_indexes:
    new_grid[0, index] = 0

  return np.matrix(new_grid.reshape(9,9))
