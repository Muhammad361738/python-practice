

try:
    n = 2/5
    print(n)
except ZeroDivisionError:
    print("Cannot Divide with zero")
finally:
    print("In Finally")