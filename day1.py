"""
Personal Message: Store a person’s name in a variable, and print a message to that person.
 Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

"""
personName = "Talha"
print(F'Hello {personName} would you like to learn some python today ')
"""
Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
"""
myPerson = "Muhammad Talha"
print(myPerson.upper())
print(myPerson.lower())
print(myPerson.title())

"""
Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed
. Then print the name after striping the white spaces.
"""
myName = "\t Muhammad     Talha        "
print(myName)
print(myName.strip())
print(myName.strip().replace(" ",""))