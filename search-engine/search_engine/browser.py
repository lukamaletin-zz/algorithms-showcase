# Author: Luka Maletin

from copy import deepcopy

from data_structures.heap import Heap
from input_handler.evaluator import evaluate
from input_handler.postfix import infix_to_postfix


def browse(trie, graph, tokens):
    criteria = [3, 2, 1]
    postfix = infix_to_postfix(tokens)

    # After converting the expression into postfix notation we replace every
    # word in the list with a dictionary of files in which the word is present,
    # or an empty dictionary if the word is not found in the trie.

    for i in range(len(postfix)):
        if postfix[i].isalpha():
            node_files = trie.find(postfix[i])
            if node_files:
                postfix[i] = deepcopy(node_files)
            else:
                postfix[i] = {}

    result = evaluate(postfix)  # returns a dictionary of resulting files

    # Iterating through resulting files to rank them:
    for key in result:
        v = graph.get_vertex(key)
        ranks = [0, 0, 0]

        # How many links are there from other files to the current file:
        ranks[1] = graph.incoming_degree(v)

        edges = graph.incoming_edges(v)
        for token in tokens:
            if token.isalpha():
                node_files = trie.find(token)
                if node_files:
                    if key in node_files:
                        # How many times do the words from the query appear
                        # in the current file:
                        ranks[0] += node_files[key][0]
                    for edge in edges:
                        source = edge.source().element()
                        if source in node_files:
                            # How many times do the words from the query appear
                            # in files that link to this one:
                            ranks[2] += node_files[source][0]

        ranks[0] *= criteria[0]
        ranks[1] *= criteria[1]
        ranks[2] *= criteria[2]
        result[key] = ranks

    print_sorted(result)


def print_sorted(result):
    heap = Heap()

    for key in result:
        heap.add(sum(result[key]), str(result[key]) + ' ' + key)

    sorted_result = heap.sort()

    i = 0
    for item in sorted_result:
        i += 1
        print(str(i) + '. ' + str(item[0]) + ' ' + item[1])
