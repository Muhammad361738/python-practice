"""
Python is a statically typed language. (True/False) (Faslse)

The bool data type in Python can only have two values: True and False. (True/False) (True)

In Python, the complex data type is used to store numbers with both real and imaginary parts. (True/False) (true)

Python automatically converts smaller data types to larger ones in arithmetic operations. (True/False) (true)

Tuples in Python are mutable. (True/False) (False)

A list can contain multiple data types in Python. (True/False) (True)

The type() function can be used to determine the data type of any variable. (True/False) (True)

Python does not support type casting. (True/False) (False)

Sets in Python allow duplicate values. (True/False) (false)

Strings in Python are immutable. (True/False) (False)




🧑‍💻 Syntax-Based Multiple Choice Questions (MCQs) (20 Marks)

Which function is used to check the data type of a variable in Python?
a) isinstance()b) type()c) checktype()d) datatype()

(b)

What will print(type(5.0)) output?
a) <class 'int'>b) <class 'float'>c) <class 'double'>d) <class 'decimal'>

(b)


Which of the following is an immutable data type?
a) Listb) Dictionaryc) Setd) Tuple

(d)

What is the correct syntax to define a set in Python?
a) set = {1, 2, 3}b) set(1, 2, 3)c) {1, 2, 3}d) set([1, 2, 3])

(a)

Which of the following is not a valid Python data type?
a) listb) arrayc) tupled) dict

(b)

What will print(type(True)) output?
a) <class 'bool'>b) <class 'int'>c) <class 'str'>d) <class 'float'>

(a)

How do you create a complex number in Python?
a) 5 + 3ib) complex(5, 3)c) 5 + 3jd) 5i + 3

(d)

Which Python collection is ordered, changeable, and allows duplicate members?
a) Listb) Tuplec) Setd) Dictionary

(a)

What is the output of print(type(None))?
a) <class 'None'>b) <class 'NoneType'>c) <class 'null'>d) <class 'void'>

(c)

Which of the following methods is used to convert a string to an integer in Python?
a) str()b) float()c) int()d) cast()

(c)


Coding-Based Questions (20 Marks)

Identify the Data Type:
Write a Python program that takes user input and prints the data type of the input.

Example Output:
Enter a value: 45
Data Type: <class 'int'>


Ans: my_num= int(input("Enter a number :"))
print(type(my_num))


Data Type Conversion:
Write a Python program to convert the following:

Integer to Float

Float to String

String to List

ANS:my_num=6
print(float(my_num))

my_num=3.2
print(str(my_num))

my_str="Zain"
print(list(my_str))

Working with Collections:

Create a list containing integers and strings.

Add a new element to the list.

Remove an element from the list.

Ans:my_list=[1,2,3,"zain",5]
print(my_list.append(6))
print(my_list.pop())

Immutable vs Mutable:
Immutable we can no update once we create 
list dic set

mutable we can upadate once we create 
string tuples int float 




Create a tuple and attempt to modify one of its elements.

my_tuples=(1,2,3,4,5)
print(my_tuples.append(5))

Explain why the modification does or does not work.
beacuse tuples are mutable 

Set Operations:
Write a Python program that:

Creates two sets of numbers.

Finds their union and intersection.

my_setone={1,2,5,7,9}
my_settwo={3,10,4,8}
print(my_setone u my_settwo)
print(my_setone - my_settwo)


""" 