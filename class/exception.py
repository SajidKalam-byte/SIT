class test(Exception):
    pass
a=int(input("Enter a number: "))

try:
    print("This try block ")
    if a>0:
        raise test
    
except test:
    print("This except block")
    print("Test is raised")

finally:
    print("_______This is compulsory execution____")
    
print("End of Code")