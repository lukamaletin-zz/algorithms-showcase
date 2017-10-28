# Author: Luka Maletin

from copy import deepcopy


def solvable(config):
    inversions = 0

    for i in range(len(config) - 1):
        if config[i] != 0:
            for j in range(i + 1, len(config)):
                if config[j] != 0:
                    if config[i] > config[j]:
                        inversions += 1

    blank = config.index(0) // 4  # blank tile row

    if inversions % 2 == 0:  # even number of inversions
        if blank == 1 or blank == 3:  # blank tile in 2nd or 4th row
            return True
        else:
            return False
    else:  # odd number of inversions
        if blank == 0 or blank == 2:  # blank tile in 1st or 3rd row
            return True
        else:
            return False


def coords(config, value):
    index = config.index(value)
    return index // 4, index % 4  # row and column of given tile


def actions(config):
    row, column = coords(config, 0)
    k = config.index(0)
    result = []

    if row > 0:  # blank tile not in first row
        down = deepcopy(config)
        down[k - 4], down[k] = down[k], down[k - 4]
        result.append(down)

    if row < 3:  # blank tile not in last row
        up = deepcopy(config)
        up[k], up[k + 4] = up[k + 4], up[k]
        result.append(up)

    if column > 0:  # blank tile not in first column
        right = deepcopy(config)
        right[k - 1], right[k] = right[k], right[k - 1]
        result.append(right)

    if column < 3:  # blank tile not in last column
        left = deepcopy(config)
        left[k], left[k + 1] = left[k + 1], left[k]
        result.append(left)

    return result


def h_score(config, final):
    # Calculates the sum of the Manhattan distance of each tile.
    distance = 0

    for i in range(len(config)):
        if config[i] != 0:
            row1, column1 = coords(config, config[i])
            row2, column2 = coords(final, config[i])
            distance += abs(row1 - row2) + abs(column1 - column2)

    return distance
