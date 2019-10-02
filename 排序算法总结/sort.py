#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

####################冒泡排序###################
def bubbleSort(s):
    n = len(s)
    for j in range(n, 1, -1):
        for i in range(1, j):
            if s[i-1] > s[i]:
                big = s[i-1]
                s[i-1] = s[i]
                s[i] = big
    return s

####################选择排序###################
def selectSort(s):
    n = len(s)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if s[min_index] > s[j]:
                min_index = j
        d = s[i]
        s[i] = s[min_index]
        s[min_index] = d
    return s

####################插入排序###################
def insertSort(s):
    n = len(s)
    for i in range(1, n):
        key = s[i] 
        j = i-1
        while j >=0 and key < s[j] : 
            s[j+1] = s[j] 
            j -= 1
        s[j+1] = key 
    return s

####################归并排序###################
def merge(s1,s2,s):
    """将两个列表是s1，s2按顺序融合为一个列表s,s为原列表"""
    # j和i就相当于两个指向的位置，i指s1，j指s2
    i = j = 0
    print "s1:===========%s" %s1
    print "s2:===========%s" %s2
    print "s:===========%s" %s
    while i+j<len(s):
        # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1
    print "s:%s" %s
    return s

def merge_sort(s):
    """归并排序"""
    n = len(s)
    # 剩一个或没有直接返回，不用排序
    if n < 2:
        return
    # 拆分
    mid = n // 2
    s1 = s[0:mid]
    print "s1:%s" %s1
    s2 = s[mid:n]
    print "s2:%s" %s2
    # 子序列递归调用排序
    merge_sort(s1)
    merge_sort(s2)
    # 合并
    print "s:===-----%s" %s
    merge(s1,s2,s)
    print '----------------'
    return s

####################快速排序###################
def partition(s, low, high):
    i = low - 1
    key = s[high]
    for j in range(low, high):
        if s[j] <= key:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[i+1],s[high] = s[high], s[i+1]
    return i+1

def quick_sort(s, low, high):
    if low < high:
        k = partition(s, low, high)
        quick_sort(s, low, k-1)
        quick_sort(s, k+1, high)
    return s

def quickSort(s):
    n = len(s)
    low = 0
    high = n - 1
    s = quick_sort(s, low, high)
    print s

####################堆排序###################
def heapify(arr, n, i): 
    largest = i

    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 

    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换
        heapify(arr, n, largest)

  
def heapSort(arr): 
    n = len(arr) 
    
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i)
    # 一个个交换元素  
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        heapify(arr, i, 0) 

####################test排序###################
if __name__ == '__main__':
    s = [6,3,5,7,0,4,1,2]
    heapSort(s)

