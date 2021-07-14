# Strings: Concatenation, Methods, and input()
 In Python, anything that goes between 'single' or "double" quotes is considered a string. Strings are commonly used to express words, but they have many other uses, including displaying information to the user and retrieving information from a user 
 
 ## Exercise 7: String Error Syntax
1. Open a new file.
2. Enter a valid string:
```python
bookstore = 'City Lights'
```

3. Now enter an invalid string:
```python
bookstore = 'City Lights"
```
4. Now you need to enter a valid string format again, as in the following code snippet
```python
bookstore = "Moe's"
```
5. Now add the invalid string again:
```python
bookstore = 'Moe's'
```

## Escape Sequences with Quotes
Python uses the backslash character, \, called an escape sequence in strings, to allow for the insertion of any type of quote inside of strings

```python
bookstore = 'Moe\'s'
```
## Multi-Line Strings
```python
vacation_note = '''
During our vacation to San Francisco, we waited in a long line by
Powell St. Station to take the cable car. Tap dancers performed on
wooden boards. By the time our cable car arrived, we started looking
online for a good place to eat. We're heading to North Beach.
'''
```
# The print() Function
## Exercise 8: Displaying Strings
1. Open a new file.
2. Define a greeting variable with the value 'Hello'. Display the greeting using the print() function:
```python
greeting = 'Hello'
```
3. Display the value of greeting without using the print() function:
4. Consider the following sequence of code
```python
spanish_greeting = 'Hola.'
spanish_greeting
arabic_greeting = 'Ahlan wa sahlan.'
```
5. Display the Spanish greeting
6. Now, display the Arabic greeting message, as mentioned in the following code snippet:

# String Operations and Concatenation
The multiplication and addition operators work with strings as well. In particular, the + operator combines two strings into one and is referred to as string concatenation.
The * operator, for multiplication, repeats a string. In the following exercise, you will be looking at string concatenation in our string samples
## Exercise 9: String Concatenation
1. Open a new file.
2. Combine the **spanish_greeting** we used in Exercise 8, Displaying Strings, with **'Senor.'** using the + operator and display the results:
```python
spanish_greeting = 'Hola'
print(spanish_greeting + 'Senor.')
>>> HolaSenor.
```
3. Now, combine **spanish_greeting** with 'Senor.' using the + operator, but this time, include a **space**:
```python
spanish_greeting = 'Hola '
print(spanish_greeting + 'Senor.')
```
4. Display the greeting 5 times using the *  multiplication operator:
```python
greeting = 'Hello'
print(greeting * 5)
```