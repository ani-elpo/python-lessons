from pprint import pprint

EMPTY = "_"
SHIP = "#"
HIT = "X"
MISS = "O"


def makeGrid(rows, cols):
    grid = []
    for x in range(0, rows):
        row = []
        grid.append(row)
        for y in range(0, cols):
            row.append(EMPTY)
    return grid


def shoot(grid, row, col):
    grid[row][col] = HIT


def position(grid, row, col, length):
    grid[row][col] = SHIP
    # length = int(input())
    # ship = grid[row][col] + length
    # ship = SHIP


def grid_print(grid):
    # grid = [[EMPTY for row in range(10)] for col in range(10)]
    for row in grid:
        print("   ".join(row))







grid2 = makeGrid(10, 10)
position(grid2, 5, 2, 3)
shoot(grid2, 3, 0)
grid_print(grid2)





#create a function that prints grids neatly
# complete the ship position function