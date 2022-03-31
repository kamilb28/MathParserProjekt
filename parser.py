import re

def lex_analyisis(string):
    symbols = ['+', '-', '*', '/']
    brackets = ['(', ')']

    tokens = list()
    for index, char in enumerate(string):
        if char in symbols:
            tokens.append([char, "symbol"])
        elif char in brackets:
            tokens.append([char, "bracket"])

        # https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        # if its o number
        elif re.match(r'\d', char):
            tokens.append([char, "number"])

        # ignore spaces
        elif char == ' ':
            pass

        # isnt number or symbol
        else:
            raise Exception('Invalid token')
    return tokens

