# Author: Luka Maletin

import re

OPERATORS = '&|!'
REGEX = r'(?:[a-zA-Z]+)|(?:[()&|!])'


def tokenize(expression):
    return re.findall(REGEX, expression)


def validate(expression):
    # All characters must be letters, operators or parenthesis.
    for character in expression:
        if (not character.isalpha()) and (character not in (OPERATORS + '() ')):
            return False, []

    tokens = tokenize(expression)
    paranthesis = 0
    i = 0

    while i < len(tokens):
        # There must not be more right than left parenthesis.
        if paranthesis < 0:
            return False, []

        elif i == 0 and tokens[0] in OPERATORS:
            return False, []

        # Allowed after left parentheses: left parentheses, word.
        elif tokens[i] == '(':
            paranthesis += 1
            if i == len(tokens) - 1:
                return False, []
            elif (tokens[i + 1] != '(') and (not tokens[i + 1].isalpha()):
                return False, []

        # Allowed after right parentheses: right parentheses, operator, word.
        elif tokens[i] == ')':
            paranthesis -= 1
            if i == len(tokens) - 1:
                break
            elif (tokens[i + 1] != ')') and (tokens[i + 1] not in OPERATORS) and (not tokens[i + 1].isalpha()):
                return False, []
            elif tokens[i + 1].isalpha():
                tokens.insert(i + 1, '&')

        # Allowed after word: parentheses, operator, word.
        elif tokens[i].isalpha():
            if i == len(tokens) - 1:
                break
            elif (tokens[i + 1] not in (OPERATORS + '()')) and (not tokens[i + 1].isalpha()):
                return False, []
            elif tokens[i + 1].isalpha() or tokens[i + 1] == '(':
                tokens.insert(i + 1, '&')

        # Allowed after operator: left parentheses, word.
        elif tokens[i] in OPERATORS:
            if i == len(tokens) - 1:
                return False, []
            elif (tokens[i + 1] != '(') and (not tokens[i + 1].isalpha()):
                return False, []

        i += 1

    # The number of left and right parenthesis must be the same.
    if paranthesis != 0:
        return False, []

    return True, tokens
