# Author: Luka Maletin

import time

from input_handler.validator import validate
from search_engine.browser import browse
from search_engine.reader import read


def main():
    path = 'C:\\Users'  # Change this to the path you want.

    start_time = time.time()
    print('Loading...')
    trie, graph = read(path)
    print('Loading time: %s seconds.' % (time.time() - start_time))

    while True:
        print("['q' - QUIT, '&' - AND, '|' - OR, '!' - AND NOT]")
        query = raw_input('Enter query: ').lower()

        if query == 'q':
            break

        valid, tokens = validate(query)

        if valid:
            start_time = time.time()
            browse(trie, graph, tokens)
            print('Results found in: %s seconds.' % (time.time() - start_time))
        else:
            print('Invalid query, try again.')


if __name__ == '__main__':
    main()
