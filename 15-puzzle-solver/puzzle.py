# Author: Luka Maletin

from heap_priority_queue import HeapPriorityQueue
from util import actions, h_score


def a_star_search(initial, final):  # f = g + h
    opened = HeapPriorityQueue()
    opened.add(0, initial, None, 0)
    closed = set()
    cycles = 0

    while not opened.is_empty():
        cycles += 1
        current_node = opened.remove_min()

        if current_node.value == final:
            return current_node, cycles

        if str(current_node.value) in closed:
            continue

        closed.add(str(current_node.value))

        for next_node in actions(current_node.value):
            g_score = current_node.g_score + 1
            f_score = h_score(next_node, final) + g_score
            opened.add(f_score, next_node, current_node, g_score)


def search(initial, final):  # f = h
    opened = HeapPriorityQueue()
    opened.add(0, initial, None, 0)
    closed = set()
    cycles = 0

    while not opened.is_empty():
        cycles += 1
        current_node = opened.remove_min()

        if current_node.value == final:
            return current_node, cycles

        if str(current_node.value) in closed:
            continue

        closed.add(str(current_node.value))

        for next_node in actions(current_node.value):
            opened.add(h_score(next_node, final), next_node, current_node, 0)


def print_solution(node):
    steps = []

    while node is not None:
        steps.append(node)
        node = node.came_from

    for i in range(len(steps) - 1, -1, -1):
        step = steps[i].value
        print(step[0:4])
        print(step[4:8])
        print(step[8:12])
        print(step[12:16])
        print('-' * 16)

    return len(steps) - 1
