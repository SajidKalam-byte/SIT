words={
    'A': "ANT",
    'K': "KING",
    'B': "BIG",
    'S': "SMALL",
    'B': "BUSY",
    'G':"GREAT"
}

print(words)
skeys=list(words.keys())
skeys.sort()

srt={i:words[i] for i in skeys}
print("Sorted dictionary ",srt)

item=input("Enter value to find :")
print(item)
for val in words.keys():
    if words[val]==item:
        print("Item found")
        print(words)
        item=input('Enter word to replace :')
        words[val]=item
        print(words)
    else:
        continue