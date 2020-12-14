class Fibonacci(object):
    def __init__(self):
        self.flist = [0,1]
        self.main()
        
    def main(self):
        listLen = input('please enter the length of fibonacci: ')
        self.checkLen(listLen)
        while len(self.flist) < int(listLen):
            self.flist.append(self.flist[-1] + self.flist[-2])
        print('we get:\n %s' %self.flist)
        
    def checkLen(self,lenth):
        lenList = map(str,range(3,51))
        if lenth in lenList:
            print('you can continue：')
        else:
            print('length only in 3 to 51')
            exit()
if __name__ == '__main__':           
    f = Fibonacci()
        
