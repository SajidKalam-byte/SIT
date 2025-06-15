class pro:
    def __init__(self):
        pass
    
    def read():
        with open("sample.txt", "r") as file:
            content = file.read()
            sum=0
            for i in content.split(','):
                sum= sum + int(i)
            print(sum)

    def write():
        with open("sample.txt", "w") as file:
            file.write("Hello\n")
            

    def list():
        with open("sample.txt", 'r') as file:
            content = file.read()
            l=[]
            c=0
            for i in content.split(","):
                l[c] = int(i)
                c+=c
            print(l)


obj = pro
obj.read()
#obj.list()