class Hello:
    def __init__(self):
        pass
    
    def dict(l):
        d = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        for i in l:
            if i in d:
                d[i] += 1
        print(d)

obj = Hello()
l = "helloworldd"
obj.dict(l)
