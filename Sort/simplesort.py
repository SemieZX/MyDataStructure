# -*- coding: utf-8 -*-
from random import randint
import timeit

def bubbleSort(alist):
    exchange = False
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1],alist[j]
                exchange=True
        if not exchange:
            break
    return


def selectionSort(alist):
    for i in range(len(alist)):
        minposition = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[minposition]:
                minposition = j
        alist[i],alist[minposition] = alist[minposition],alist[i]
    return 


def insertionSort(alist):
    for i in range(1,len(alist)):
        currentvalue = alist[i] #save current
        position = i
        while alist[position-1] > currentvalue and position > 0:
            alist[position] = alist[position-1]
            position = position -1
        alist[position] = currentvalue
    return 


def shellSort(alist):
    gap = len(alist)//2
    while gap > 0:
        for startpos in range(gap):
            gapInsertionSort(alist,startpos,gap)
        gap = gap//2
    return 


def gapInsertionSort(alist,startpos,gap):
    # accessory function
    for i in range(startpos,len(alist),gap):
        position = i
        currentvalue = alist[i]
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue



# test the speed
max = 5000
list=[randint(-max,max) for x in range(max)]

alist = list[:]
blist = list[:]
clist = list[:]
dlist = list[:]

t1=timeit.Timer('bubbleSort(alist)','from __main__ import bubbleSort,alist')
print('短路冒泡排序: %s s' %t1.timeit(number=1))

t2=timeit.Timer('selectionSort(blist)','from __main__ import selectionSort,blist')
print('选择排序: %s s' %t2.timeit(number=1))

t3=timeit.Timer('insertionSort(clist)','from __main__ import insertionSort,clist')
print('插入排序: %s s' %t3.timeit(number=1))

t4=timeit.Timer('shellSort(dlist)','from __main__ import shellSort,dlist')
print('希尔排序: %s s' %t4.timeit(number=1))
