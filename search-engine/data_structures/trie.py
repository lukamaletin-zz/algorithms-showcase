# Author: Luka Maletin


class Trie(object):
    class Node(object):
        def __init__(self, element=''):
            self._element = element

            # (K, V) = (file path (string), criteria (list)):
            self._files = {}

        def add_file_count(self, path):
            if path in self._files:
                self._files[path][0] += 1
            else:
                self._files[path] = [1, 0, 0]

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    def __init__(self):
        self._root = self.Node()

        # (K, V) = (Node, children (dictionary)):
        self._references = {}  # top-level dictionary

        # (K, V) = (letter (string), Node):
        self._references[self._root] = {}  # children

    def add(self, word, path):
        current_node = self._root
        for i in range(len(word)):
            if word[i] not in self._references[current_node]:
                new_node = self.Node(word[i])
                self._references[new_node] = {}  # children
                self._references[current_node][word[i]] = new_node
                current_node = new_node
            else:
                current_node = self._references[current_node][word[i]]

            if i == len(word) - 1:
                current_node.add_file_count(path)

    def find(self, word):
        current_node = self._root
        for i in range(len(word)):
            if word[i] in self._references[current_node]:
                current_node = self._references[current_node][word[i]]
                if i == len(word) - 1:
                    return current_node._files
            else:
                return None
