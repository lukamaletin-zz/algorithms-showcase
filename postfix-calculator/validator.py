# Author: Luka Maletin

import re

OPERATORS = '+-*/^'
REGEX = r'(?:\d*\.\d+)|(?:\d+)|(?:[()+\-\^/*])'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def tokenize(expression):
    return re.findall(REGEX, expression)


def is_valid(expression):
    expression = ''.join(expression.split())

    # All characters must be numbers or operators.
    for character in expression:
        if ((not is_number(character)) and (character not in OPERATORS) and
                (character not in '().')):
            return False, []

    tokens = tokenize(expression)
    paranthesis = 0
    i = 0

    while i < len(tokens):
        # There must not be more right than left parenthesis.
        if paranthesis < 0:
            return False, []

        elif i == 0 and tokens[0] in OPERATORS:
            if tokens[0] == '-':
                if len(tokens) == 0:
                    return False, []

                # Adding zero because subtraction is a binary operation.
                tokens.insert(0, '0')
            else:
                return False, []

        # Allowed after left parentheses: number, left parentheses.
        elif tokens[i] == '(':
            paranthesis += 1
            if i == len(tokens) - 1:
                return False, []
            elif tokens[i + 1] == '-':
                tokens.insert(i + 1, '0')
            elif (not is_number(tokens[i + 1])) and (tokens[i + 1] != '('):
                return False, []

        # Allowed after right parentheses, number: operator, right parentheses.
        elif tokens[i] == ')' or is_number(tokens[i]):
            if tokens[i] == ')':
                paranthesis -= 1
            if i == len(tokens) - 1:
                break
            elif (tokens[i + 1] not in OPERATORS) and (tokens[i + 1] != ')'):
                return False, []

        # Allowed after operator: number, left parentheses.
        elif tokens[i] in OPERATORS:
            if i == len(tokens) - 1:
                return False, []
            elif (not is_number(tokens[i + 1])) and (tokens[i + 1] != '('):
                return False, []

        i += 1

    # The number of left and right parenthesis must be the same.
    if paranthesis != 0:
        return False, []

    return True, tokens
