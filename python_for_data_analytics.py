# .....
print(" print statements in python")


print("hello woorld")
print("this is my first program")
print("i hope you all like it "
"my name is ganesh"
"ghumade")
# hello woorld
# this is my first program
# i hope you all like it my name is ganeshghumade

# multiple line use
print("""hello world
this is my first program
 i hope you all like it""")
# hello world
# this is my first program
#  i hope you all like it

# using \n for new line
print("hello world \nthis is my first program \ni hope you all like it")
# hello world 
# this is my first program 
# i hope you all like it


# using single quote inside double quote
print('it\'s going to rain today')
# it's going to rain today

# .....

print("comments in python")
# .....

# 1.single line comments

# hello my name is Ganesh 
# hello my name is Yash

# 2.multiple line comments

"""""in this program we are going to learn about
data analytics and many more things 
using python programming language"""


# 3. multiple line comments(in single inverted commas)

'''in this program we are going to learn about
data analytics and many more things 
using python programming language'''

# .....

print("creating varibles in python")

"""variables are placeholders, in which we can store a value """

a="hello"
print(a)
# hello

a="hello"
print("a")
# a

# rules fow writting variables in python
# 1. in starting of variable any name is given then in print statement same this letter is compulsory other wise it through error

Name="Ganesh"
print(Name)
# Ganesh

# 2.make sure to not use space while creating a variable
# if want to create space then use underscore symbol(_)

one_number="Ganesh Yash"
print(one_number)
# Ganesh Yash

# 3. a variable name should never start with a number or special symbol

# .....

print("data type and user-input")

# Datatypes:

"""text-type: string(str)
numeric type: integer(int),floting point(flot),complex
sequence type: list,tuple and range
mapping type: dictionaries(dict)
set type: set, frozenset
boolean type: bool
binary types: bytes, bytearry, memoryview"""

"""user input""" # in string type

name=input("enter your name here: ")
print(name)
# enter your name here: Ganesh
# Ganesh


"""user input""" # in integer type (int)

age=int(input("enter your age here: "))
print(age)
# enter your age here: 20
# 20

"""user input""" # in floating point type (float)

length=float(input("enter thee length of the rectangle: "))
print(length)
# enter thee length of the rectangle: 42.2
# 42.2

 
"""user input""" # in evaluating the expression (eval)

exp1=eval(input("enter any equation here: "))
print(exp1)
# enter any equation here: 56+44
# 100

# .....

print("typecasting and subtypes")

"""conversion of one datatype to another is caleed as type-casting
there are two type of type-casting:
1. implicit typw conversion
2. exxplicit type conversion"""

name="Ganesh"
print(type(name))
# <class 'str'>

age=20
print(type(age))
# <class 'int'>

""" implicit type conversion """
a=123
b=1.23
print (type(a))
print(type(b))

c=a+b
print(c)
print(type(c))

# <class 'int'>
# <class 'float'>
# 124.23
# <class 'float'>

"""" explicit type conversion"""

a="123" # Here a is in the form of string. We cannot add string and flooat together.That's why firstly convert string as an integer 
a=int(a)  # after conversion <class 'int'>
b=1.23  # <class 'float'> 
  
print(type(a))
print(type(b))
c=a+b      # 124.23
print(c)

print(type(c))  # <class 'float'>



a="123" # Here a is in the form of string. We cannot add string and flooat together.That's why firstly convert string as an float 
a=float(a)  # after conversion <class 'float'>
b=1.23  # <class 'float'> 
  
print(type(a))
print(type(b))
c=a+b      # 124.23
print(c)

print(type(c))  # <class 'float'>

# .....
