try:
    user = float(input("Enter a Marks : "))
    if user >= 80:
       print("You'r Grade is A+")

    elif user >= 70 :
       print("You'r Grade is B")

    elif user >= 60:
       print("You'r Grade is C")
    
    elif user >= 50 :
       print("You'r Grade is D")

    else:
       print("You are Failed")

except ValueError as e :
    print(e)
    
