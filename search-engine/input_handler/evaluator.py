# Author: Luka Maletin

from data_structures.stack import Stack

OPERATORS = '&|!'


def calculate(d1, d2, operator):
    if operator == '&':
        return intersection(d1, d2)

    elif operator == '|':
        return union(d1, d2)

    elif operator == '!':
        return difference(d1, d2)


def evaluate(expression):
    operands = Stack()

    for token in expression:
        if isinstance(token, str):
            if token in OPERATORS:
                b = operands.pop()  # second operand
                a = operands.pop()  # first operand
                operands.push(calculate(a, b, token))

        else:
            operands.push(token)

    return operands.pop()


def intersection(d1, d2):
    result = {}

    for key in d1.keys():
        if key in d2:
            result[key] = d1[key]

    return result


def union(d1, d2):
    result = {}

    for key in d1.keys():
        result[key] = d1[key]

    for key in d2.keys():
        if key not in result:
            result[key] = d2[key]

    return result


def difference(d1, d2):
    result = {}

    for key in d1.keys():
        if key not in d2:
            result[key] = d1[key]

    return result
