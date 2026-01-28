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

print("problem soling") 

1.
"""write a program to display a person's name, age and 
# address in three different lines."""

name="yash"
age=23
address="654 lake street"

print(name)
print(age)
print(address)

# yash
# 23
# 654 lake street

2.
"""write  a program to convert a float into integer"""

x=12.4
print(type(x))
# <class 'float'>

x=int(x)
print(type(x))
# <class 'int'>
print (x)
# 12


3.
""""write a program to take details from a student for id-card and then print in different lines"""

name=input("enter the name of the student: ")
grade=input("enter the grade of the stident: ")
age=int(input("enter the age of the student: "))
email=input("enter the email of the student: ")
phone_number=input("enter the phone number of the students: ")
print("student identity card")

print("name:", name)
print("grade:", grade)
print("age:", age)
print("email:", email)
print("phone_number:", phone_number)

output="""enter the name of the student: Yash
# enter the grade of the stident: 5th
# enter the age of the student: 10
# enter the email of the student: yash@gmail.com
# enter the phone number of the students: 8888888888
# student identity card
# name: Yash
# grade: 5th
# age: 10
# email: yash@gmail.com
# phone_number: 8888888888"""

4.
""""write a program to take an user input as integer then convert it as float"""

a=int(input("enter a number here: "))
print(a)
print(type(a))
# enter a number here: 12
# 12
# <class 'int'>

a=float(a)
print("after conversion", a)   # after conversion 12.0
print(type(a))
# <class 'float'>

# .....


print("Swap two variables")

# method 1 (use temporary variables(temp))

x=12
y=13

temp=x
print(temp)  # 12 value of temp
x=y
print(x)
# 13 (value of x)
"""here the value of x is now 13 """

y=temp
print(y) 
# 12 (value of y)
""""and here the value of y is 12"""

# method 2

a=30
b=40

a,b=b,a
print(a)  # value of a is 40
print(b)  # value of b is 30

# .....

print("operators and operands")

"""operators indicates what operatio is to be performed while operand 
indicates on what the action or the operation should be performed.

x+y=0 
in the given experation, x,y, and 0 are thr operands. """

# types of operators:

""" operators can be further divided into 6 categories
1.Arithmetic operation
2.Comparison operation
3.Logical operation
4.Assignment operation
5.Identity operation
6.Membership operation
7.Bitwise operation """

# .....

print("Arithmetic Operators")

"""
1.Addition (+)
2.Substraction (-)
3.Multiplaction (*)
4.Floor division (//)
5.Exponentiation (**)
6.Division (/)
7.Modulus (%)
"""
# 1.Addition (+)
"""10+2=12"""

#2.Substraction (-)
"""15-5=10"""

# 3.Multiplaction (*)
"""5*5=25"""

# 4.Floor divisiion (//)
"""If we divide 8 by 3 then quotient is 2.6666.. and reminder is 2
in above example floor division of the 8 by 3 is 2"""

print(8//3)
# 2

print(12//3)
# 4

print(13//3)
# 4

# 5.Exponentiation (**)

"""in general to wrtie 2 the powerr 10
here 2**10"""

print(2**10)
# 1024

print(2**2)
# 4

print(10**10)
# 10000000000

# 6.Division (/)

"""5/5=1
10/5=2"""

# 7.Modulus (%)

"""we use modulus in the pyrhon for to find remender 
here we divide 8 by 3 then the remender is 2"""

print(8%3)
# 2

print(10%5)
# 0

print(20%3)
# 2

print(13%6)
# 1

# .....

print("comparisional operators")

"""
python comparison operators

1.Greater than '>'
2.Less than '<'
3.Equal to '=='
4.Not equal to '!='
5.Greater than or equal to '>='
6.Less than or erual to '<='
"""

# 1. Greater than '>'

print(9>6) 
# True

print(10>9)
# True

print(45>30)
# True

print(55>58)
# False

print(89>90)
# False


# 2.Less than '<' 

print(9<6) 
# False

print(10<9)
# False

print(45<30)
# False

print(55<58)
# True

print(89<90)
# True

# 3. Equal to '=='

print(3==3)
# True

print(8==8)
# True

print(10==10)
# True

print(6==5)
# False

print(3==8)
# False

# 4. Not equal to '!='

print(3!=10)
# True

print(6!=15)
# True

print(9!=10)
# True

print(10!=10)
# False

print(6!=6)
# False

# 5. Greater than or equal to '>='

print(3>=3)
# True

print(5>=1)
# True

print(10>=5)
# True

print(10>=20)
# False

print(15>=20)
# False

# 6.Less than or erual to '<='

print(10<=20)
# True

print(5<=6)
# True

print(10<=10)
# True

print(5<=4)
# False

print(12<=10)
# False

# .....

print("logical operators")

"""1.operator:(and)
meaning: true if both the operanda are true 
example: x and y

2.operator:(or)
meaning: true if either of the operanda is true 
example: x or y 

3.operator:(not)
meaning: true if operand is false (complements the operand)
exaple: not x
"""

# 1.operator: (and)

print(3>4 and 3<4)
# False
print(6>10 and 6<10)
# False
print(9<10 and 12>10)
# True
print(7>5 and 4<2)
# False
print(3<4 and 6>4)
# True

# 2.operator:(or)

print(3>4 or 3<4)
# False
print(6>10 or 6<10)
# False
print(9<10 or 12>10)
# True
print(3>5 or 9<2)
# False
print(3<4 or 6>4)
# True

# 3.operator:(not)
# opposite 

print(not(3>4 or 3<4))
# False
print(not(6>10 or 6<10))
# False
print(not(9<10 or 12>10))
# False
print(not(3>5 and 9<2))
# True
print(not(3<4 and 6>4))
# False

# .....

print ("assignment operators")

"""assignment operators are used in python to assign to variables.
a=6 is a simple assignment operator that assigns the value 6 on the right 
to the variable o on the left..

1.operator:=
example:x=6
equivalent to: x=6

2.operator:+=
example:x+=6
eqivalent to: x=x+6


3.operator: -=
example: x-=6
eqivalent to: x=x-6


4.operator: *=
example: x*=6
eqivalent to: x=x*6
"""

# .....

print("identity operators")

"""identity operators are uused to compare items to see if they are 
the same object with the same memory address"""

# types 
"""
1.Is
2.Is not 
"""

# 1.Is

1.
a=1234
b="1234"
print (a is b)
# False 

2.
a=1234
b=1234

print(a is b)
# True

# 2.Is not 

a=1234
b="1234"
print (a is not b)
# True

2.
a=1234
b=1234

print(a is not b)
# False 

# .....

print("Bitwise operators")

"""
these operators are used to comapre the binary numbers
Types
1.AND (&) Operator
2.OR (|) Operator 
3.XOR (^) operator
4.<<zero fill left shift
5.>>zero fill right shift

operation         result

0&0                0
1&0                0 
0&1                0
1&1                1
"""

print(bin(10))
# 0b1010

print(bin(15))
# 0b1111

print(bin(20))
# 0b10100



# 1.AND (&) Operator

# implementation of And operation on Binary digits 

1.
a=10
b=8

print(a&b)
# 8

2.
c=56
b=5

print(c&b)
# 0


# 2.OR (|) Operator 

"""
OR operator 

Bitwise Or operations 

operation       result

0|0               0
1|0               1
0|1               1
1|1               1

"""

1.
a=10
b=8

print(a|b)
# 10

2.
c=56
b=5

print(c|b)
# 61

# 3.XOR (^) operator

"""XOR operators:

Bitwise Xor operations 

operation     result 
0^0             0
1^0             1
0^1             1
1^1             0

"""
1.
a=10
b=8

print(a^b)
# 2

2.
c=56
b=5

print(c^b)
# 61

# 4.<<zero fill left shift

1.
print(10>>1)
# 5

2.
print(5>>6)
# 0

# 5.>>zero fill right shift

1.
print(10<<1)
# 20

2.
print(5<<6)
# 320

# .....

print("Membership operators")

"""
Membership operators are used to check the presence of a
sequence in an object.
types 
1.In
2.Not in
 """

# 1.In


1.
a="hello"
print("h" in a)
# True

2.
p="Ganesh"
print("p" in p)
# False

3.
p="Ganesh"
print("f" in p)
# False

4.
o="Orange"
print("r" in o)
# True


# 2.Not in

1.
a="hello"
print("h" not in a)
# False

2.
p="Ganesh"
print("p" not in p)
# True

3.
p="Ganesh"
print("f" not in p)
# True

4.
o="Orange"
print("r" not in o)
# False

# .....

print("Conditional Statements")

"""
Conditional statements :

conditional statements allows computer to execute a certain 
condition only if it is true 

types of conditional statements:

1.If statements
2.If-else statements
3.If-elif-statements
4.Nested statements
5.Short Hand if statements
6.SHORT HAND IF-ELSE STATEMENTS
 """
# .....

print("IF STATEMENTS")

"""
if statements

The if statement is the most fundamental decision-making statement
The if statement in python has the subsequent syntax:
if expression
statement
"""

1.
marks=56

if marks>=50:
    print("You will get a mobile phone")
print("Thank you")

# You will get a mobile phone
# Thank you

2.
apple=10

if apple<5:
    print("Good luck")
print("Sorry")  

# Sorry

3.
apple=4

if apple<5:
    print("Bad luck")
print("Sorry")

# Bad luck
# Sorry

4.
orange=50

if orange>10:
    print("You are good")
print("It is ok")    
# You are good
# It is ok

5.
a=20
if a >30:
    print("Yes i am present")
print("ok") 

# ok

# .....
