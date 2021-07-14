# Basic Matj

```python
# Addition
print(4 + 4)

# Subtraction
print(7 - 1)

# Multiplication
print(4 * 6)

# Division
print(7 / 3)

# Integer Division
print(7 // 3)

# Exponentiation
print(2 ** 3)

# Modulo
print( 9 % 3)
```
# Order of operations
```python
print(5 + 2 * -3)
print( (5 + 2) * -3 )
```
## Exercise 01

1. Subtract 5 to the 3rd power, which is 5^3, from 100 and divide the result by 5:

2. Add 6 to the remainder of 15 divided 4:
```python
print( (15 % 4)  + 6)
```
3. Add 2 to the 2nd power, which is 2^2, to the integer division of 24 and 4:

```
print( 2 ** 2 + 24 // 4)
```
# Number Types: Integers and Floats
Now you will address the difference between an integer and a float. Consider 8 and 8.0. You know that 8 and 8.0 are equivalent mathematically. They both represent the same
number, but they are different types. 8 is an integer, and 8.0 is a decimal or float. 
## Exercise 2: Integer and Float Types
1. Begin by explicitly determining the type of 6 using the following code:
```python
print(type(6))
```
2. Now, enter type(6.0) in the next cell of your notebook:
```python
print(type(6.0))
```
3. Now, add 5 to 3.14. Infer the type of their sum:
4. Now, convert 7.999999999 to an int:
```python
int(7.999999999)
```
5. Convert 6 to a float:
```python
float(6)
```

# Variable Assignment
## Exercise 3: Assigning Variables
1. Set x as equal to the number 2
2. Add 1 to the variable x
3. Change x to 3.0 and add 1 to x
# Changing Types
1. y starts as an integer:
2. y becomes a float:
3. Check the type of y:
# Reassigning Variables in Terms of Themselves
# Activity 1: Assigning Values to Variables
1. First, set 14 to the x variable.
2. Now, add 1 to x.
3. Finally, divide x by 5 and square it.
# Variable Names
To avoid confusion, it's recommended to use variable names that make sense to readers. Instead of using x, the variable may be income or age. 
```python
import keyword
print(keyword.kwlist)
```
# Exercise 4: Variable Names
1. Create a variable called ```1st_number``` and assign it a value of 1:
2. Now, let's try using letters to begin a variable:
3. Now, use special characters in a variable name, as in the following code:
```python
my_$ = 1000.00
```
4. Now, use letters again instead of special characters for the variable name:
```python
my_money = 1000.00
```
# Multiple Variables
Most programs contain multiple variables. The same rules apply as when working with single variables. You will practice working with multiple variables in the following
exercise
## Exercise 5: Multiple Variables in Python
1. Assign 5 to x and 2 to y:
2. Add x to x and subtract y to the second power:
3. Assign 8 to x and 5 to y in one line:
```python
x, y = 8, 5
```
4. Find the integer division of x and y:

# Comments
1. Write a comment that states This is a comment:
2. Set the pi variable as equal to 3.14. Add a comment above the line stating what you did
3. Now, try setting the pi variable as equal to 3.14 again, but add the comment stating what you did on the same line

# Docstrings
Docstrings, short for document strings, state what a given document, such as a program, a function, or a class, actually does
```python
"""
This document will explore why comments are particularly useful
when writing and reading code.
"""
```

# Activity 2: Finding a Solution Using the Pythagorean Theorem in Python
In this activity, you will determine the Pythagorean distance between three points. You will utilize a docstring and comments to clarify the process.

1. Write a docstring that describes what is going to happen.
2. Set x, y, and z as equal to 2, 3, and 4.
3. Determine the Pythagorean distance between x, y, and z.
4. Include comments to clarify each line of code.