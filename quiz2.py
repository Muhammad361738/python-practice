# Section A: True/False Questions (20 Marks)
# Each question carries 2 marks. Choose whether the statement is true or false.

# True/False: The == operator in Python is used to assign a value to a variable. (False)
# True/False: The logical operator or returns True only if both operands are True. (False)
# True/False: The != operator compares if two values are equal. (false)
# True/False: The in operator checks if a value exists within an iterable, like a list or string.  (true)
# True/False: The not logical operator in Python inverts the Boolean value of its operand. (false)
# True/False: x = 5 is an example of an assignment operator. (true)
# True/False: The is operator checks if two variables point to the same object in memory. (true)
# True/False: The not operator can be used with only Boolean values in Python. (false)
# True/False: The and operator returns True if either of its operands is True. (true)
# True/False: Python allows assigning a variable multiple values in one line like x, y = 5, 10. (true)
# Section B: Multiple Choice Questions (40 Marks)
# Each question carries 4 marks.

# Which of the following is not a valid comparison operator in Python?
# a) >=
# b) ==
# c) ===
# d) !=
# Ans : (C)
# What will be the output of the following code?

# python
# Copy
# Edit
# a = 10
# b = 20
# c = 15
# print(a < b and c > a)
# a) True
# b) False
# c) Error
# d) None
# (a)
# Which of the following logical operators is used to reverse the Boolean value?
# a) and
# b) or
# c) not
# d) xor
#  (d)
# What is the correct output of the following code snippet?

# python
# Copy
# Edit
# a = 10
# b = 5
# a += b
# print(a)
# a) 10
# b) 15
# c) 5
# d) None
# (b)
# Which Python keyword is used to declare a function?
# a) def
# b) func
# c) function
# d) declare
# (a)
# Which of the following statements is incorrect regarding variable assignment in Python?
# a) Variables are assigned values using the = operator.
# b) Python allows assigning multiple variables in a single line.
# c) Python does not allow reassigning values to variables.
# d) A variable can store a value of any data type.
# (c)
# What does the is operator do in Python?
# a) Compares if two values are equal
# b) Compares memory addresses of two variables
# c) Compares the data types of two variables
# d) Checks if a value exists in a list
# (b)
# Which of the following is the correct way to delete a variable in Python?
# a) delete var
# b) var = None
# c) del var
# d) remove var
# (C)

# Section C: Coding Questions (40 Marks)
# Each coding question carries 10 marks. Write the Python code for the following problems.

# Assignment & Comparison Operators:
# Write a Python program that takes two numbers as input from the user. Use the comparison operators to check if the first number is greater than, less than, or equal to the second number. Print the appropriate message based on the comparison.

# user1 = int(input("Enter a first number : "))
# user2 = int(input("Enter a first number : "))
# if(user1> user2 ):
#     print("user1 is greater then user2")
# elif(user1< user2 ):
#     print("user1 is less then user2")
# elif(user1 == user2 ):
#     print("user1 is equal to user2")

# Logical Operators:
# Write a Python function that accepts two Boolean variables and returns the result of the and, or, and not logical operations on these variables.
# def myBol (a,b):
#     user = input("enter operator : ")
#     if (user == "and"):
#         return print(a and b)
#     elif (user == "or"):
#         return print(a or b)
#     elif (user == "not"):
#         return print(not a)
# print(myBol(False,False))
# Variable Assignment & Keywords:
# Create a Python program that assigns values to three variables (a string, an integer, and a float) in a single line and prints each value and its data type.
# a,b,c = "Talha",20,67.9
# print(a,type(a),"\n" , b,type(b),"\n",c,type(c))
# Deleting Variables:
# Write a Python script that assigns a value to a variable and then deletes the variable. Ensure the script throws an error when trying to access the variable after deletion.
myName = "Talha"
print(myName)
del myName
print(myName)
# Evaluation Criteria:
# True/False Questions: Marks are awarded for correctly identifying whether the statement is true or false.
# MCQs: Correct answers will earn full marks, and incorrect ones will get zero.
myName = "Talha"
user = input("Enter the the m Name")
if (myName == user):
    print(True)
else:
    print(False)
# Total Marks Breakdown:
# True/False Questions: 20 marks
# MCQs: 40 marks
# Coding Questions: 40 marks
