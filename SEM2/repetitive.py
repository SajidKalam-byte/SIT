class Hello:
    def __init__(self):
        pass
    
    def count(self, l):
        print(l[0], end="")
        for i in range(1, len(l)):
            if l[i] == l[i - 1]:
                if l[i - 1] != "*":
                    print("*", end="")
            else:
                print(l[i], end="")

obj = Hello()
l = "hello worldd"
obj.count(l)
