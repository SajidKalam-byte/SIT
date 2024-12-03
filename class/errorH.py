
try:
    a=int(input("ENter input "))
    b=int(input("ENter input "))
except ValueError:
    print("Invalid input")

try:
    
    div=a/b
    print(div)    
except IndexError:
    print("Error for dividing by zero")
except ZeroDivisionError:
    print("division by zero")
except NameError:
    print("Name error")
