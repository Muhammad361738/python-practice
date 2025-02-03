"""
Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the 
number 8. Be sure to enclose your operations in print statements to see the results.
"""
print(4+4)
print(12-4)
print(4*2)
print(16/2)

"""
Names: Store the names of a few of your friends in a array called names.
 Print each person’s name by accessing each element in the list, one at a time
"""
myFriends = ["Waqar", "Salman","Zain","Talha"]
print(myFriends[0])
print(myFriends[1])
print(myFriends[2])
print(myFriends[3])

"""
Greetings: Start with the array you used in Exercise 11, but instead of just printing each 
person’s name, print a message to them. The text of each message should be the same,
 but each message should be personalized with the person’s name.
"""
print(f'Hello {myFriends[0]}')
print(f'Hello {myFriends[1]}')
print(f'Hello {myFriends[2]}')
print(f'Hello {myFriends[3]}')

"""
Your Own Array: Think of your favorite mode of transportation, such as a motorcycle or a car, 
and make a list that stores several examples. Use your list to print a series of statements about 
these items, such as “I would like to own a Honda motorcycle.”
"""

transportation = ["Honda motorcycle", "Tesla car", "Yamaha bike", "BMW car", "Ducati bike"]

for i in transportation :
    print(f'I would like to own {i}')
