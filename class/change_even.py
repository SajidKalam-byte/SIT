'''input= 4247638
Add +1 to odd digits,
and +2 to even digits.'''


num = int(input("Enter a number: "))
rev = 0
copy=num
count=0

# Count the number of zeros
while copy % 10 == 0:
    count+=1
    copy //= 10

while num != 0:
    digit = num % 10
    if digit != 0:
        if digit % 2 == 0:
            digit += 2
        else:
            digit += 1
        digit %= 10
    rev = rev * 10 + digit
    num //= 10

# Reverse the digits to get the final number
x = rev
s = 0
while x != 0:
    a = x % 10
    s = s * 10 + a
    x //= 10

if count > 0:
    print("Changed number:", s*10**count)
else:
    print("Changed number:", s)