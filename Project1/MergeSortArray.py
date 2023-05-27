#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project 1
#Problem 1: Merge 2 subarrays using auxiliary array of min(m,n) size


# In[2]:


import numpy as np


# In[3]:


def mysort(a, n, m):

    if n == 0 or m == 0:
        return a
    else:
        l = min(n,m)    #length of smaller subarray
        h = max(n,m)    #length of larger subarray
        Aux = [0]*l     #Create auxiliary array of length min(n,m)

        #Initialize auxiliary array with the elements of smaller subarray
        for i in range(n+m-l, n+m, 1):
            Aux[i-n-m+l] = a[i]


       #Sort main array in asc order till the length of larger subarray
       #Shift larger elements into aux array and sort it in asc order
        for i in range(h):
            if a[i] > Aux[0]:
                temp = Aux[0]
                Aux[0] = a[i]
                a[i] = temp
                #sorting aux array in asc order
                if l>1 and Aux[0]>Aux[1]:
                    for k in range(1,l):
                        if Aux[k]<Aux[k-1]:
                            t = Aux[k-1]
                            Aux[k-1] = Aux[k]
                            Aux[k] = t

        #replace last l elements of the main array with aux array
        for i in range(h,n+m):
            a[i] = Aux[i-h]
        return a


# In[4]:


def concat(a1,a2):
    if len(a1) < len(a2):
        if len(a1)<1:
            a = a2
        else:
            a = np.concatenate([a2,a1])
    else:
        if len(a2) < 1:
            a = a1
        else:
            a = np.concatenate([a1,a2])
    return a


# In[5]:


def __main__():
    print("\nTestcase 1:")
    a11 = []
    a12 = [3,7,9]
    a1 = concat(a11,a12)
    print("Array ",a1)
    test1 = mysort(a1,len(a11), len(a12))
    print("Sorted array", test1)

    print("\nTestcase 2:")
    a21 = [2,7,9]
    a22 = [1]
    a2 = concat(a21,a22)
    print("Array ",a2)
    test2 = mysort(a2,len(a21), len(a22))
    print("Sorted array", test2)
    
    print("\nTestcase 3:")
    a31 = [1,7,10,15]
    a32 = [3,8,12,18]
    a3 = concat(a31,a32)
    print("Array ",a3)
    test3 = mysort(a3,len(a31), len(a32))
    print("Sorted array", test3)

    print("\nTestcase 4:")
    a41 = [1, 3, 5, 5, 15, 18, 21]
    a42 = [5, 5, 6, 8, 10, 12, 16, 17, 17, 20, 25, 28]
    a4 = concat(a41,a42)
    print("Array ",a4)
    test4 = mysort(a4,len(a41), len(a42))
    print("Sorted array", test4)

__main__()

