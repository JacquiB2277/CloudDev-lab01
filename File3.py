Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print "Hello World"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> Print "Hello World"
SyntaxError: invalid syntax
>>> Print {"Hello World")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> Print ("Hello World")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Print ("Hello World")
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print("Hello world")
Hello world
