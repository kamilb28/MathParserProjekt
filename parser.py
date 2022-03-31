import re

# analiza leksykalna/ czytanie tokenów
def lex_analyisis(string):
    symbols = ['+', '-', '*', '/']
    brackets = ['(', ')']

    tokens = list()
    for index, char in enumerate(string):
        # if it's symbol 
        if char in symbols:
            tokens.append([char, "symbol"])
            
        # or bracket
        elif char in brackets:
            tokens.append([char, "bracket"])

        # https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        # if it's number
        elif re.match(r'\d', char):
            tokens.append([char, "number"])

        # ignore spaces
        elif char == ' ':
            pass

        # isn't number or symbol
        else:
            raise Exception('Invalid token')
    return tokens

