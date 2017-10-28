# Author: Luka Maletin

from evaluator import evaluate
from postfix import infix_to_postfix
from validator import is_valid


def main():
    while True:
        expression = input('Enter an expression (q - quit): ')

        if expression == 'q':
            break

        valid, tokens = is_valid(expression)

        if valid:
            print(evaluate(infix_to_postfix(tokens)))
        else:
            print('Invalid expression, try again.')


if __name__ == '__main__':
    main()
