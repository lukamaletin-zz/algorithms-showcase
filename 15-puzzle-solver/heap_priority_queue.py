# Author: Luka Maletin


class PriorityQueueError(Exception):
    pass


class PriorityQueueItem(object):
    def __init__(self, key, value, came_from, g_score):
        self._key = key
        self.value = value
        self.came_from = came_from
        self.g_score = g_score

    def __lt__(self, other):
        return self._key < other._key

    def __le__(self, other):
        return self._key <= other._key


class HeapPriorityQueue(object):
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

    def add(self, key, value, came_from, g_score):
        self._data.append(PriorityQueueItem(key, value, came_from, g_score))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise PriorityQueueError('Priority queue is empty.')

        item = self._data[0]
        return item._key, item.value, item.came_from, item.g_score

    def remove_min(self):
        if self.is_empty():
            raise PriorityQueueError('Priority queue is empty.')

        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item
