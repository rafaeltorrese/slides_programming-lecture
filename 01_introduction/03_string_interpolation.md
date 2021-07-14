# String Interpolation
When writing strings, you may want to include variables in the output. String interpolation includes the variable names as placeholders within the string. There
are two standard methods for achieving string interpolation: comma separators and format.
# Comma Separators
```python
italian_greeting = 'Ciao'
print('Should we greet people with', italian_greeting, 'in North Beach?')
```
## Format
```python
owner = 'Lawrence Ferlinghetti'
age = 100
print('The founder of City Lights Bookstore, {}, is now {} years old.'.format(owner, age))
print(f'The founder of City Lights Bookstore, {owner}, is now {age} years old.')
```
# The len() Function

```python
arabic_greeting = 'Ahlan wa sahlan.'
len(arabic_greeting)
```

# String Methods
All Python types, including strings, have their own methods. These methods generally provide shortcuts for implementing useful tasks. Methods in Python, as in many other
languages, are accessed via dot notation
## Exercise 10: String
1. Set a new variable, called **name**, to any name that you like:
2. Now, convert the name into lowercase letters using the **lower()** function:
3. Now, capitalize the name using the **capitalize()** function:
4. Convert the name into uppercase letters using **upper()**
5. Finally, count the number of "o" instances in the word 'Corey'
```python
name.count('o')
```

# Casting
It's common for numbers to be expressed as strings when dealing with input and output. Note that '5' and 5 are different types.
## Exercise 11: Types and Casting
1. Open a new file
2. Determine the type of '5':
type('5')
3. Now, add '5' and '7':
```python
'5' + '7'
 ```
 4. Convert the '5' string to an int
 5. Add '5' and '7' by converting them to int first:
 int('5') + int('7')

 # The input() Function
 