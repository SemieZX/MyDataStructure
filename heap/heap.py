import  timeit
from random import randint
import test
import sys
sys.path.append('J:\mydspycharm\heap')
from semie import hello

class MaxHeap:

    def __init__(self,max = 100000):
        self.heapList = [0]
        self.currentSize = 0
        self.maximum = max

    def shiftUp(self,i):
        currentvalue = self.heapList[i]
        while i//2 > 0:
            if self.heapList[i//2] < currentvalue :#父亲小
                self.heapList[i] = self.heapList[i//2]
                i = i//2
            else: #父节点比它大
                break
            self.heapList[i] = currentvalue

    def maxChild(self, i):  # return the index of maxChild
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def shiftDown(self,i):
        currentvalue = self.heapList[i]
        while i*2 <= self.currentSize:
            mc = self.maxChild(i)
            if currentvalue < self.heapList[mc]:#比最大孩子小
                self.heapList[i] = self.heapList[mc]
                i = mc
            else:#比孩子都大，不再下沉
                break
            self.heapList[i] = currentvalue

    def delFirst(self):
        delval = self.heapList[1]
        if self.currentSize == 1:
            self.currentSize -= 1
            self.heapList.pop()
            return delval
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.shiftDown(1)
        return delval

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.shiftUp(self.currentSize)
        if self.currentSize > self.maximum:
            self.delFirst()

    def buildHeap(self,alist): #heapify
        self.heapList = [0] + alist[:]
        self.currentSize=len(alist)
        i = self.currentSize // 2
        while i > 0:
            self.shiftDown[i]
            i -= 1
        overflow = self.currentSize - self.maximum
        for i in range(overflow):
            self.delFirst()

    def HeapSort(self,alist):
        self.buildHeap(alist)
        sortedList = [self.delFirst() for x in range(self.currentSize)]
        sortedList.reverse()
        return sortedList

    def HeapSortInPlace(self,alist):
        self.buildHeap(alist)
        while self.currentSize > 1: #每次把最大的放到最后，然后调整堆，再把剩余最大的放最后
            self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize] , self.heapList[1]
            self.currentSize -= 1
            self.shiftDown(1)
        return self.heapList[1:]

class MinHeap(MaxHeap): #最小堆，继承自MaxHeap，覆盖父类的上浮和下沉操作

    def __init__(self):
        super(MaxHeap,self).__init__()

    def shiftUp(self,i):
        currentvalue = self.heapList[i]
        while i//2 > 0:
            if self.heapList[i//2] > currentvalue:
                self.heapList[i] = self.heapList[i//2]
                i = i//2
            else:
                break
        self.heapList[i] = currentvalue

    def minChild(self,i):
        if 2*i + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2-1]:
                return 2*i
            else:
                return i*2 + 1

    def shiftDown(self,i):
        currentvalue = self.heapList[i]
        while 2*i <= self.currentSize:
            mc = self.minChild(i)
            if currentvalue > self.heapList[mc]:
                self.heapList[i] = self.heapList[mc]
                i = mc
            else:
                break
        self.heapList[i] = currentvalue


def main():
    test.hi()

if __name__ == '__main__':
    main()



