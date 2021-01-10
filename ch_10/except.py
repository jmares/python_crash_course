try:
    a = 512/2
    print(a)
except ZeroDivisionError:
    print("You cannot divide by 0!")

try:
    b = 512/2
except ZeroDivisionError:
    print("You cannot divide by 0!")
else:
    print(b)

