class Explorer:
    def __init__(self):
        self.current=-1
        self.items=[]
    def enter(self,item):
        if self.current+1<len(self.items):
            while len(self.items)>self.current+1:
                self.items.pop()
            self.items.append(item)
            self.current+=1
        else:
            self.items.append(item)
            self.current+=1
    def next(self):
        if self.current+1<len(self.items):
            self.current+=1
    def back(self):
        if self.isBottom():
            pass
        else:
            self.current=self.current-1
    def isBottom(self):
        if self.current==0:
            return True
        else:
            return False
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def getCur(self):
        if self.isEmpty():
            pass
        else:
            return self.items[self.current]
    def getLen(self):
        return len(self.items)
    def view(self):
        print '========================= top'
        if self.isEmpty():
            pass
        else:
            for i in range(1,len(self.items)-self.current):
                print '     ',self.items[-i]
            print '-->  ',self.items[self.current]
            for i in range(len(self.items)-self.current+1,len(self.items)+1):
                print '     ',self.items[-i]
        print '------------------------- bottom'

if __name__=='__main__':
    ie=Explorer()
    ie.view()
    ie.enter('sjtu')
    ie.enter('baidu')
    ie.enter('sina')
    ie.enter('youku')
    ie.back()
    ie.view()
    ie.enter('apple')
    ie.view()
    ie.back()
    ie.getCur()
    ie.back()
    ie.back()
    ie.back()
    ie.view()
    tmp=raw_input('press any key...')
