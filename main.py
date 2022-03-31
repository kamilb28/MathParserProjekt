import parser
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        string = sys.argv[1]
    else:
        string = "(2 + 2 ) * 3"

    tokens = parser.lex_analyisis(string)

    print(tokens)
