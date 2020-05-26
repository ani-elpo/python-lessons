from pprint import pprint


def makeGrid(rows, cols):
    grid = []
    for x in range(0, rows):
        row = []
        grid.append(row)
        for y in range(0, cols):
            row.append(0)

    return grid


def shoot(row, col):
    for y in range(row, col):
        row.append(1)




grid2 = makeGrid(10, 10)
pprint(grid2)





#make grid with 10 cols + 10 rows - DONE
#each cell has 0 - DONE
#shoot func --> accepts col + row index and replaces 0 with 1

#create a function that prints grids neatly