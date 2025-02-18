class Stack:
    def __init__(self):
        self.mylist=[]
    def push(self,item):
        self.mylist.append(item)
    def pop(self):
        return self.mylist.pop()
    def getLen(self):
        return len(self.mylist)
    def isEmpty(self):
        return (self.mylist==[])
    def item(self,num):
        return self.mylist[num]
    
        
