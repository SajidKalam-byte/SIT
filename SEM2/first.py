class Hello:
    def __init__(self):
        pass
    
    def count(l):
        count=0
        for i in l:
            if i==0:
                count+=1
        print("The number of 0's in list is : ",count)


obj=Hello
l=[1,2,3,4,0,0]
obj.count(l)