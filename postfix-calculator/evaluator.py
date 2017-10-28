# Author: Luka Maletin

from array_stack import ArrayStack

OPERATORS = '+-*/^'


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return b - a
    elif operator == '*':
        return a * b
    elif operator == '/':
        return b / a
    else:
        return b ** a


def evaluate(expression):
    operands = ArrayStack()

    for token in expression:
        if token in OPERATORS:
            b = operands.pop()  # second operand
            a = operands.pop()  # first operand

            if token == '/' and b == 0:
                return 'Cannot divide by zero, try again.'
            elif token == '^' and b < 1 and a < 0:
                return 'Cannot root negative number, try again.'
            else:
                operands.push(calculate(b, a, token))

        else:
            operands.push(float(token))

    return operands.pop()
