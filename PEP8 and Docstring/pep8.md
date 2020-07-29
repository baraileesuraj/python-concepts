# Pep 8 
 Pep 8 is a style guide for python code that  gives coding conventions for the Python code comprising the standard library in the main Python distribution.
 
 
# Code Layout Rules 

1. Use 4 space per indentation level
2. Continuation lines should align wrapped elements either vertically or using hanging indent
    ```python
    def myown_function_name(
            var_a, var_b, var_c,
            var_d):
        print(var_a)
    ```
3. Hanging indents should add a level
    ```python
    foo = my_function_name(
        var_a, var_b,
        var_c, var_d)
    ```
4. Spaces are thr preferred intentation method.And tabs should be used solely to remain constant with code that is already indented with tabs.
5. Maximum length of all lines should be 79 characters.
6. Line breaks should happen before a binary operator.
    ```python
    income=(income1
            + income2
            + income3
            - taxes
            )
    ```
7.  Surround top-level function and class definition with two blank lines.And method definition inside a class are surrounded by a single blank line.
8.  Always prefer UTF-8 format.
9.  Imports should ususally be on seperate lines and on top.
    ``` python
    #Nice
    import os
    import sys
    #Not Nice
    import os,sys
    #Nice
    from subprocess import Popen,PIPe
    ```
    
10. Wildcard imports like  __( from <module> import *)__ should be avoided.
11. Module level 'dunders' should be placed after module docstring but before any import statements.
12. Whitespaces correct uses
       ```python
       spam(ham[1], {eggs: 2})
       foo = (0,)
       if x == 4: print x, y; x, y = y, x
       myfunction(a)
       d['key'] = l[index]
       x = 1
       i = i + 1
       def munge() -> PosInt: ...
       def complex(real, imag=0.0):
       ```
13. Naming Conventions
    * Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.
    * Avoid using l,O or I as single character variable names.
    * Identifiers must be ASCII compatible
    * Modules should be all-lowercase.And Classname should be CapWords convention.
    * Function names should be lowercase, with words separated by underscore.
    * Always use self for the first argument to instance methods.
    * Always use cls for the first argument to class methods.
    * class_ is better than clss.
    * Constant are capital letters with underscores separating words.
    * Public attributes should have no leading underscores.
    * If public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name. 
    * If class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. 


14. Variable Annotations
    *  No space before the colon
    *  If an assignment has a right hand side, then the equality sign should have exactly one space on both sides:
