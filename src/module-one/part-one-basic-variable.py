import sys

print("sample python now started with date 15 June 204")

print(sys.version)

print(sys.version_info)

"""
Python Indentation
Indentation refers to the spaces at the beginning of a code line.

as you line 15 we used if statement but line 16 we require min one space and same line number 19 we did same
so space more import in python and this is only for clean code in terms of code read.


"""
if 5 > 2:
    print("five is greater then two")

# if we have more than one line also we need to put proper place in each statement
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")
    print("Five is greater than two!")

# as you see below code we did not define any data type in
# x and y variable and base on our value it takes and print it


x = 5
y = "hello world"

print(x)
print(y)

# he value of z is overwrite
z = 4  # x is of type int
z = "Sally"  # x is now of type str
print(z)

"""
Casting
If you want to specify the data type of a variable, this can be done with casting.
"""
p = str(3)  # p will be '3'
q = int(3)  # q will be 3
r = float(3)  # r will be 3.0

print(p)
print(q)
print(r)

"""
Get the Type
You can get the data type of a variable with the type() function.
"""

a = 5
b = "goldy"
print(type(a))
print(type(b))

"""
Single or Double Quotes?
String variables can be declared either by using single or double quotes:
"""

s = "dhruvi"
# is the same as
f = 'hemang'

print(s)
print(f)

"""
Case-Sensitive
Variable names are case-sensitive.
"""

y = 4
Y = "yellow"
# Y will not overwrite a

print(y)
print(Y)

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myvar = "goldy"
my_var = "goldy"
_my_var = "goldy"
myVar = "goldy"
MYVAR = "goldy"
myvar2 = "goldy"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

"""
2myvar = "error-varible-type"
my-var = "error-varible-type"
my var = "error-varible-type"

#This example will produce an error in the result
"""

"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
"""

myVariableName = "camel"

"""
Pascal Case
Each word starts with a capital letter:
"""

MyVariableName = "pascal case"

"""
Snake Case
Each word is separated by an underscore character:
"""

my_variable_name = "snake"

"""
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""

u, i, o = "Pat", "Cat", "Bat"
print(u)
print(i)
print(o)

"""
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
"""

x = y = z = "element"
print(x)
print(y)
print(z)

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc.
Python allows you to extract the values into variables.
 This is called unpacking.
"""

cars = ["maruti", "tata", "ford"]
x, y, z = cars
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python"
y = "is"
z = "awesom"
print(x + y + z)

# for numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# in the print() function, when you try to combine a string and a number with the +
# operator, Python will give you an error:
"""
x = 5
y = "John"
print(x + y)
"""

# The best way to output multiple variables in the print() function is to separate them with commas,
# which even support different data types:

x = 5
y = "John"
print(x, y)

"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Create a variable inside a function, with the same name as the global variable

y = "awesome"


def sample():
    y = "fantastic"
    print("Java is " + y)


sample()

print("Python is " + y)

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""


def third():
    global p
    p = "fantastic"


third()

print("Python is " + p)

# Also, use the global keyword if you want to change a global variable inside a function.

s = "awesome"


def five():
    global s
    s = "fantastic"


five()

print("Python is " + s)
