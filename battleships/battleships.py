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


class ShipTooLongError(Exception):
    pass


def position(grid, row, col, length, direction = "vertical"):

    # error messages
    if row + length > 9:
        raise ShipTooLongError("your ship is too long row ="+str(row)+" length ="+str(length))
    if col + length > 9:
        raise ShipTooLongError("your ship is too long column ="+str(col)+" length ="+str(length))

    # positioning ships
    if direction == "vertical":
        for i in range(length):
            grid[row][col] = SHIP
            row = row + 1
    if direction == "horizontal":
        for i in range(length):
            grid[row][col] = SHIP
            col = col + 1



def grid_print(grid):
    # grid = [[EMPTY for row in range(10)] for col in range(10)]
    for row in grid:
        print("   ".join(row))







grid2 = makeGrid(10, 10)
position(grid2, 5, 2, 3)
position(grid2, 2, 8, 4, direction="horizontal")
shoot(grid2, 3, 0)
grid_print(grid2)





# complete the ship position function so it makes hor + ver ships
# check if it's valid (fits) if it's not, raise the error