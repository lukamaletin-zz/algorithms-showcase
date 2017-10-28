# Author: Luka Maletin

from data_structures.stack import Stack

OPERATORS = '&|!'


def infix_to_postfix(expression):
    postfix = []
    priority = {'(': 1, '&': 2, '|': 2, '!': 2}
    operators = Stack()

    for token in expression:
        if token in OPERATORS:
            # Operators are added to the stack, but first the ones with a
            # higher priority are added to the result:
            while not operators.is_empty() and priority[token] <= priority[operators.top()]:
                postfix.append(operators.pop())

            operators.push(token)

        # Left parenthesis are added to the stack:
        elif token == '(':
            operators.push(token)

        # Operators between parenthesis are added from the stack to the result:
        elif token == ')':
            while operators.top() != '(':
                postfix.append(operators.pop())

            operators.pop()  # Pop the left parentheses from the stack.

        # Operands are added to the result:
        else:
            postfix.append(token)

    while not operators.is_empty():
        # The remaining operators are added from the stack to the result:
        postfix.append(operators.pop())

    return postfix
