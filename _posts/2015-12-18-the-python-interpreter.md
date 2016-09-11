---
layout: post
title: The Python Interpreter
subtitle: An introduction
meta: A brief description of the four pieces of the Python interpreter; The lexer, parser, compiler, and bytecode interpreter.
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

### Introduction:

The Python interpreter is a program distributed along with the Python standard library modules that is used to execute Python code. The Python interpreter works by converting human-readable Python source code into machine-understandable bytecode before executing the bytecode.

The Python interpreter, and thus the Python language, is vastly different than a strictly typed compiled language. The Python interpreter reads the source code top down and executes it until it hits an error or the end of the file.

There are four stages the Python interpreter uses to execute Python source code. The lexer reads in the source code and breaks it into pieces, which the parser then attempts to make sense of. The code is then handed off to the compiler, which converts it to machine readable bytecode, which is then executed by the bytecode interpreter.

When someone mentions "the Python interpreter", they mean all four pieces together, but when someone mentions the *"bytecode interpreter"*, they mean the final stage in the Python interpretation process.

If this interests you, Allison Kaptur has written a [series](https://akaptur.com/blog/2013/11/15/introduction-to-the-python-interpreter/) of blog posts explaining the CPython interpreter (the official Python interpreter written in C) in greater detail. She has also given several interesting PyCon [talks](https://www.youtube.com/watch?v=HVUTjQzESeo) about the Python interpreter as well. My intent here is only to give the broadest top level non-expert introduction, if you're looking for detail, you won't find it here.

### Lexer:

The lexer, or lexical analyzer, breaks the source code into tokens. If one were to write a lexer for the English language, it would break up a source text into the individual works and punctuation marks.

The lexer has two main parts, the scanner and the tokenizer. The scanner is language agnostic, and reads in the source file one character at a time. The scanner returns a character object, which contains the character, and the line number and column it is found at in the source file. Each time the scanner is called by the tokenizer it returns the next character in the source file.

The tokenizer is language specific. It groups the characters from the scanner into tokens based off the rules that define the Python language. This is where the the language syntax is defined. The tokenizer uses rules about whitespace, function names, class names, variable names, valid operators, comments, and all of the other rules necessary to define a language grammar in order to group the characters into meaningful tokens.

Given the following example source code,

```python
def foo( a ):
    x = 6
    return x + a
```

the tokenizer would break the code into the following tokens, with the first column being the line number the token is found on, the second column the character in the line the token begins on, and the third column being the token type, with the last column as the actual token value.

```
1  0 Symbol......: def
1  4 Identifier..: foo
1  7 Symbol......: (
1  9 Identifier..: a
1 11 Symbol......: )
1 12 Symbol......: :
2  4 Identifier..: x
2  6 Symbol......: =
2  8 Number......: 6
3  4 Symbol......: return
3 11 Identifier..: x
3 13 Symbol......: +
3 15 Identifier..: a
```

### Parser:

The parser takes all of the tokens from the source file, and creates what is called an Abstract Syntax Tree (AST) which represents the logical structure of the code. The AST is a tree-like structure with each node representing a language construct.

The following figure is the corresponding AST for the following code snippet, taken from the Wikipedia article on [ASTs](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

```python
while b != 0:
  if a > b:
    a = a - b
  else:
    b = b - a
return a
```

<img class="centered" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Abstract_syntax_tree_for_Euclidean_algorithm.svg/400px-Abstract_syntax_tree_for_Euclidean_algorithm.svg" alt="Abstract Syntac Tree">
<!-- ![AST](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Abstract_syntax_tree_for_Euclidean_algorithm.svg/400px-Abstract_syntax_tree_for_Euclidean_algorithm.svg) -->


### Compiler:

The compiler takes the AST and converts it into a code object. The code object is a feature unique to Python. The code object contains the bytecode, among other constructs such as a list of all variable names, all function names, any constants, variable values, etc.

The bytecode is just a series of bytes, with different codes corresponding to different commands. Here is the code object for the `foo` example given above.

```python
>>> dir(foo.func_code)
['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', 'co_argcount', 'co_cellvars',
'co_code', 'co_consts', 'co_filename', 'co_firstlineno',
'co_flags', 'co_freevars', 'co_lnotab', 'co_name', 'co_names',
'co_nlocals', 'co_stacksize', 'co_varnames']
```

There is a lot of things in there that are beyond the scope of this description. The things that interest us are the `co_varnames`, `co_consts`, and `co_code` fields.

```python
>>> foo.func_code.co_varnames
('a', 'x')
>>> foo.func_code.co_consts
(None, 6)
>>> foo.func_code.co_code
'd\x01\x00}\x01\x00|\x01\x00|\x00\x00\x17S'
```

The `co_varnames` field is an object that holds the variable names used in the function. The `co_consts` field is an object that holds all of the constants available inside the function scope. The last field, `co_code` is the actual bytecode.

### Interpreter:

The bytecode is simply a list of numbers. If we `ord` each byte, we can see what numbers the bytecode actually contains.

```python
>>> [ord(b) for b in foo.func_code.co_code]
[100, 1, 0, 125, 1, 0, 124, 1, 0, 124, 0, 0, 23, 83]
```

To understand the Python bytecode, one would simply look through the Python interpreter's C source code and see what `100` means, and then what `1` means. Or we can use the `dis` module to we can see what each bytecode segment means. What we will do is `dis`assemble our example function's bytecode.

```python
>>> import dis
>>> dis.dis(foo.func_code)
  2           0 LOAD_CONST               1 (6)
              3 STORE_FAST               1 (x)

  3           6 LOAD_FAST                1 (x)
              9 LOAD_FAST                0 (a)
             12 BINARY_ADD
             13 RETURN_VALUE
```

The left column is the line number in the source code, and the second column is the position in the line. The middle column is where the interesting things are; it is a list of the internal commands that the bytecode instructs the interpreter to execute. The fourth column is the arguments of the commands, and the fifth column are the names of the arguments that `dis` has looked up for us.

### Conclusion:

The Python interpreter goes through four stages in order to execute Python source code. It tokenizes source code with the lexer, and then attempts to make sense of the tokens by arranging them into an Abstract Syntax Tree. The compiler then takes the AST and turns it into a code object that the interpreter then executes.
