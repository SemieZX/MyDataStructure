<<<<<<< HEAD
import copy
import timeit
from random import randint
def mergeSort(alist):
    #print("Splitting",alist)
    if len(alist)>1:
        # there can import insertionSort when len(alist)<=16
        mid = len(alist)//2
        lefthalf = alist[:mid] #切片操作干扰算法性能
        righthalf = alist[mid:]

        if lefthalf[-1] < righthalf[0]: #优化一
            alist = lefthalf + righthalf
            return alist

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            j += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    #print("merging ", alist)

def mergeSortBu(alist):
    n = len(alist)
    size = 1
    while size < n:
        blist = alist[:]
        i = 0
        # confirm the left is avalible
        while i + size < n:
            if alist[i+size-1] < alist[i+size]: #优化一,左边第一个比右边第一个小时，先不处理
                i = i + 2*size
                continue
            # merge
            l , r , k = i , i + size, i
            while l < i + size and r < min(i+2*size,n):
                if blist[l] <= blist[r]:
                    alist[k] = blist[l]
                    l += 1
                else:
                    alist[k] = blist[r]
                    r +=1
                k += 1
            while l < i +size:
                alist[k] = blist[l]
                l += 1
                k += 1
            while r < min(i+2*size,n):
                alist[k] = blist[r]
                r += 1
                k += 1
            i += 2*size
        return alist





if __name__ == '__main__':
    # alist = [54,26,93,17,77,31,44,55,20]
    # mergeSortBu(alist)
    # print(alist)
    max = 10000
    list = [randint(-max, max) for x in range(max)]
    alist = copy.copy(list)
    blist = copy.copy(list)
    t2 = timeit.Timer('mergeSortBu(blist)', 'from __main__ import mergeSortBu,blist')
    t1 = timeit.Timer('mergeSort(alist)','from __main__ import mergeSort,alist')
    print(t1.timeit(number=1))
    print(t2.timeit(number=1))

=======
import copy
import timeit
from random import randint
def mergeSort(alist):
    #print("Splitting",alist)
    if len(alist)>1:
        # there can import insertionSort when len(alist)<=16
        mid = len(alist)//2
        lefthalf = alist[:mid] #切片操作干扰算法性能
        righthalf = alist[mid:]

        if lefthalf[-1] < righthalf[0]: #优化一
            alist = lefthalf + righthalf
            return alist

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            j += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    #print("merging ", alist)

def mergeSortBu(alist):
    n = len(alist)
    size = 1
    while size < n:
        blist = alist[:]
        i = 0
        # confirm the left is avalible
        while i + size < n:
            if alist[i+size-1] < alist[i+size]: #优化一,左边第一个比右边第一个小时，先不处理
                i = i + 2*size
                continue
            # merge
            l , r , k = i , i + size, i
            while l < i + size and r < min(i+2*size,n):
                if blist[l] <= blist[r]:
                    alist[k] = blist[l]
                    l += 1
                else:
                    alist[k] = blist[r]
                    r +=1
                k += 1
            while l < i +size:
                alist[k] = blist[l]
                l += 1
                k += 1
            while r < min(i+2*size,n):
                alist[k] = blist[r]
                r += 1
                k += 1
            i += 2*size
        return alist





if __name__ == '__main__':
    # alist = [54,26,93,17,77,31,44,55,20]
    # mergeSortBu(alist)
    # print(alist)
    max = 10000
    list = [randint(-max, max) for x in range(max)]
    alist = copy.copy(list)
    blist = copy.copy(list)
    t2 = timeit.Timer('mergeSortBu(blist)', 'from __main__ import mergeSortBu,blist')
    t1 = timeit.Timer('mergeSort(alist)','from __main__ import mergeSort,alist')
    print(t1.timeit(number=1))
    print(t2.timeit(number=1))

>>>>>>> 317c57ce73cfe876e9e4d1874de1a4c1e4051ffe
