# Author: Luka Maletin

import os

from data_structures.graph import Graph
from data_structures.trie import Trie
from search_engine.html_parser import Parser


def read(path):
    trie = Trie()
    parser = Parser()
    graph = Graph()

    # Adding words into the trie and links into the graph:
    for root, dirs, files in os.walk(path):
        for path in files:
            if path.endswith(".html") or path.endswith(".htm"):
                current = os.path.join(root, path)
                u = graph.insert_vertex(current)
                links, words = parser.parse(current)
                for link in links:
                    v = graph.insert_vertex(link)
                    graph.insert_edge(u, v)
                for word in words:
                    trie.add(word.lower(), current)
    return trie, graph
