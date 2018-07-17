from random import randint
import timeit
import copy

# 3路快排适合有大量重复元素的排序，但是对普通序列其性能并不是最好
# 对于排序算法，在小序列时可以用插入排序进行优化，其次对于初始元素随机化也很有必要，这是为了结局序列有序时分的两部分极大不平问题的好办法

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    rand = randint(first,last) #解决近乎有序的列表
    alist[first],alist[rand] = alist[rand], alist[first]
    pointvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done: #双路快拍，解决有大量相同值的元素
        #判断用等号，保证两棵树平衡
        while leftmark <= rightmark and alist[leftmark] < pointvalue:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] > pointvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
            leftmark += 1
            rightmark -= 1

    alist[first] , alist[rightmark] = alist[rightmark], alist[first]

    return rightmark



def quickSort3ways(alist):
    quickSort3waysHelper(alist,0,len(alist)-1)

def quickSort3waysHelper(alist,first,last):
    if first < last:
        leftEnd , rightStart = partition3ways(alist,first,last)
        quickSort3waysHelper(alist,first,leftEnd)
        quickSort3waysHelper(alist,rightStart,last)

def partition3ways(alist,first,last):
    rand = randint(first,last)
    alist[first],alist[rand] = alist[rand],alist[first]
    pivotvalue = alist[first]
    #[first+1..lf]  < [rt..last] > [lf+1..i) =
    # remind the initial value
    leftmark , i , rightmark = first, first+1, last+1
    done = False
    while not done:
        if alist[i] < pivotvalue:
            alist[leftmark+1],alist[i] = alist[i],alist[leftmark+1]
            i += 1
            leftmark += 1
        elif alist[i] == pivotvalue:
            i += 1
        else:
            alist[rightmark-1],alist[i] = alist[rightmark-1],alist[i]
            rightmark -= 1
        if i >= rightmark:
            done =True

    alist[first],alist[leftmark] = alist[leftmark], alist[first]
    leftmark -= 1
    return  leftmark, rightmark



if __name__ == '__main__':

    #alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #quickSort(alist)
    #print(alist)
    max = 5000
    list = [randint(0,10)for _ in range(max)]
    alist = copy.copy(list)
    blist = copy.copy(list)
    t1 = timeit.Timer('quickSort(alist)', 'from __main__ import quickSort,alist')
    t2 = timeit.Timer('quickSort3ways(blist)','from __main__ import quickSort3ways,blist')
    print('快速排序: %s s' % t1.timeit(number=1))
    print('3ways快速排序: %s s' % t2.timeit(number=1))




