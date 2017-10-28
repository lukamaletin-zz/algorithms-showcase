# Author: Luka Maletin


class HeapError(Exception):
    pass


class Heap(object):
    class Item(object):
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __le__(self, other):
            return self._key <= other._key

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _has_left(self, i):
        return self._left(i) < len(self._data)

    def _has_right(self, i):
        return self._right(i) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        parent = self._parent(i)
        if i > 0 and self._data[i] < self._data[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def _downheap(self, i):
        if self._has_left(i):
            left = self._left(i)
            smaller_child = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[right] < self._data[left]:
                    smaller_child = right
            if self._data[smaller_child] < self._data[i]:
                self._swap(i, smaller_child)
                self._downheap(smaller_child)

    def add(self, key, value):
        self._data.append(self.Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise HeapError('Priority queue is empty.')

        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise HeapError('Priority queue is empty.')

        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value

    def sort(self):
        result = []
        while not self.is_empty():
            result.append(self.remove_min())
        return reversed(result)
