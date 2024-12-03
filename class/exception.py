class test(Exception):
    pass
try:
    print("This try block ")
    raise test
except test:
    print("This except block")
    print("Test is raised")

print("End of Code")