# IST-Sem-5-Implementation-Of-Compiler-Phases-in-Python-Compiler-Construction-
In this assignment, we implemented Phases of compiler in python for our subject compiler construction.
The given code consists of two modules: a lexical analyzer and a syntax tree generator.

The lexical analyzer module has a tokenize function that takes a string of code as input and uses regular expressions to identify and extract tokens from the code. It stores the extracted tokens in a list called tokens, which consists of tuples with the token type and the token value.

The syntax tree generator module has a create_syntax_tree function that takes a string of code as input and uses the ast (Abstract Syntax Tree) module to generate a syntax tree for the code. The syntax tree is represented as a tree-like structure with nodes representing the different parts of the code. The function returns the syntax tree.

Both modules can be tested by calling the respective functions and passing in some sample code. The output of the tests show the extracted tokens in the case of the lexical analyzer and the syntax tree in the case of the syntax tree generator.
