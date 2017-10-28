# Author: Luka Maletin

import time

from puzzle import a_star_search, print_solution, search
from util import solvable

FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
# examples:
PUZZLE = [0, 5, 6, 12, 11, 4, 7, 8, 14, 1, 3, 2, 9, 13, 15, 10]
PUZZLE2 = [11, 6, 8, 0, 15, 4, 12, 7, 5, 9, 3, 2, 1, 14, 10, 13]
PUZZLE3 = [13, 6, 8, 7, 14, 4, 12, 2, 10, 1, 3, 11, 9, 15, 5, 0]
PUZZLE4 = [5, 1, 0, 7, 11, 3, 8, 2, 14, 10, 12, 13, 4, 15, 9, 6]
PUZZLE5 = [11, 1, 0, 8, 9, 6, 2, 7, 4, 3, 12, 13, 5, 10, 15, 14]
PUZZLE6 = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


def main():
    if solvable(PUZZLE):
        print('Solving...')
        final_node, cycles = search(PUZZLE, FINAL)
        steps = print_solution(final_node)
        print('Solution of %s steps found after %s cycles.' % (steps, cycles))
    else:
        print('No solution.')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Runtime: %s seconds.' % (time.time() - start_time))
