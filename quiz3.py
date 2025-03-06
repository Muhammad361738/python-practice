"""
# Python Quiz: Strings, String Methods, Type Casting, and Conversions

## **Section A: True/False Questions (20 Marks)**
Each question carries 2 marks.

1. Strings in Python are immutable. (True/False) (true) 
2. The `strip()` method removes only leading whitespace from a string. (True/False)  (False)
3. Python automatically stores identical string literals in the same memory location. (True/False)  "False"
4. Type casting allows conversion of one data type to another. (True/False)  (True)
5. A tuple can be directly converted into a list using `list()` function. (True/False) (True) 
6. The `isalpha()` method returns `True` if a string contains only alphabetic characters. (True/False)  (True)
7. The `join()` method can only be used with lists of strings. (True/False)  (false)
8. Python allows implicit conversion between complex and integer data types. (True/False) (true) 
9. The `count()` method in strings is case-sensitive. (True/False)  (true)
10. A set allows duplicate values after conversion from a list. (True/False)  (true)

## **Section B: Multiple Choice Questions (40 Marks)**
Each question carries 4 marks.

1. Which of the following methods is used to convert a string to lowercase?
   a) upper()  
   b) lower()  
   c) capitalize()  
   d) title()  
(b)
2. What will `print('Python'.find('y'))` output?
   a) 0  
   b) 1  
   c) -1  
   d) None  
(b)
3. Which method is used to remove trailing characters from a string?
   a) strip()  
   b) rstrip()  
   c) lstrip()  
   d) replace()  
(a)
4. What is the result of `str(3.14)`?
   a) 3.14 (as float)  
   b) '3.14' (as string)  
   c) Error  
   d) None of the above  
(b)
5. Which data type cannot be directly converted to a set?
   a) List  
   b) Dictionary  
   c) Tuple  
   d) String  
(b)
6. What is the output of the following code?
   ```python
   s = "hello"
   print(s * 2)
   ```
   a) hellohello  
   b) Error  
   c) hheelllloo  
   d) None  
(a)
7. How do you check the length of a string `s`?
   a) len(s)  
   b) s.length()  
   c) length(s)  
   d) s.len()  
(a)
8. What will `tuple([1, 2, 3])` return?
   a) [1, 2, 3]  
   b) {1, 2, 3}  
   c) (1, 2, 3)  
   d) Error  
(a)
9. Which method is used to check if a string ends with a specific substring?
   a) startswith()  
   b) endswith()  
   c) find()  
   d) index()  
(a)
10. What is the result of `set('hello')`?
   a) {'hello'}  
   b) {'h', 'e', 'l', 'o'}  
   c) ['h', 'e', 'l', 'o']  
   d) Error  
(d)
## **Section C: Coding Questions (40 Marks)**
Each coding question carries 10 marks.

1. **String Methods:**
   Write a Python program that:
   - Takes a string input from the user.
   - Converts the string to uppercase.
   - Replaces all occurrences of the letter 'a' with '@'.
 "Ans"  
myString = input("Enter tha name : ")
myString.upper()
print(myString.replace("a","@"))


2. **Type Casting:**
   Write a Python script to:
   - Accept a floating-point number from the user.
   - Convert it to an integer.
   - Print both the float and integer values.
   Ans : 
myNum = float(input("Enter the float value "))

myInt = int(myNum)
print(myNum,"   ",myInt)

3. **String and List Conversion:**
   Write a Python function that:
   - Takes a comma-separated string as input.
   - Converts it into a list of integers.
   - Returns the list and its length.
   # myNumber = (input("Enter the number : ")).replace(" ",",")
# print(myNumber)
# # myList = int(myNumber)
# mySec=list(myNumber)
# print(mySec)
# print(len(mySec))

4. **List, Tuple, and Set Conversions:**
   Write a Python program to:
   - Convert a list of numbers into a tuple and a set.
   - Print all three collections (list, tuple, set) along with their types.
myList = [5,8,74,89,56,5,8,74]
myTup = tuple(myList)
mySet = set(myList)

print(myList,type(myList),"\n",myTup,type(myTup),"\n",mySet,type(mySet))
## **Total Marks: 100**
- Section A: 20 Marks
- Section B: 40 Marks
- Section C: 40 Marks


"""
