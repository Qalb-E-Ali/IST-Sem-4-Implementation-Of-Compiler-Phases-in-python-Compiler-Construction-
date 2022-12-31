# Module 01 lexical analyzer 
import re

# List of tokens
tokens = []

# Regular expression patterns for each token
token_patterns = [
    (r'\d+', 'INTEGER'),
    (r'\+', 'OPERATOR'),
    (r'-', 'OPERATOR'),
    (r'\*', 'OPERATOR'),
    (r'/', 'OPERATOR'),
    (r'\(', 'PUNCTUATOR'),
    (r'\)', 'PUNCTUATOR'),
]

# Tokenize the input code
def tokenize(code):
    # Split the code into a list of lines
    lines = code.split('\n')

    # Iterate over each line
    for line in lines:
        # Match the line against the token patterns
        for pattern, token_type in token_patterns:
            # Find all occurrences of the pattern in the line
            for match in re.finditer(pattern, line):
                # Extract the matched string and add it to the list of tokens
                tokens.append((token_type, match.group()))

# Test the tokenize function with some sample code
code = "1 + 2 * (3 + 4 )"
tokenize(code)
print(tokens)

# Module 02 Syntax tree

import ast

def create_syntax_tree(code):
    tree = ast.parse(code)
    return tree

# Test the function with some sample code
code = "x = 1 + 2"
tree = create_syntax_tree(code)
print(ast.dump(tree))
