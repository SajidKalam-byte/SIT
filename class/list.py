'''1. Count a number of character, numbers, special characters present in a list.
	IO- 4, '5', 0, '@', '!', 'B'
    OP- 3, 3, 2'''
list=['4', '5', '0', '@', '!', 'B']
count=0
count1=0
count2=0
for i in list:
    if i.isalpha():
        count+=1
    elif i.isdigit():
        count1+=1
    else:
        count2+=1
print(count, count1, count2)