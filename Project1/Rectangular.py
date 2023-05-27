#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def rectangular(x,y):
    m = []
    n = []
    sign = 1
    
    #managing sign
    if x < 0:
        x = -1*x
        sign = -1*sign
    if y < 0:
        y = -1*y
        sign = -1*sign
    #converting numbers into matrices
    while x:
        m.append(x%10)
        x = x//10
    while y:
        n.append(y%10)
        y = y//10
    m.reverse()
    n.reverse()

    #initializing variables
    visit = 1
    i = len(m)-1
    j = len(n)-1
    is_running = True
    res = 0
    mult = 1
    carry = 0
    while is_running:
        t = len(m)-i
        k = i
        pdt = 0
        while (t > 0) and j >= 0:
            pdt += m[k]*n[j]
            if k == 0 and j == 0:
                is_running = False
            k += 1
            t -= 1
            j -= 1

        pdt = pdt + carry
        res = res + (pdt%10)*(mult)
        carry = pdt//10
        mult *= 10 
        if i == 0:
            i = i
            visit += 1
            j = len(n) - visit       
        else:
            i -= 1
            j = len(n) - 1
    res = (carry*mult+ res)*sign
    return res


# In[ ]:


def __main__():
    print("\nTestcase 1:")
    x1 = 7000
    y1 = 7294
    print("x = ",x1, 'y = ',y1)
    test1 = rectangular(x1,y1)
    print("x*y =  ", test1)

    print("\nTestcase 2:")
    x2 = 25
    y2 = 5038385
    print("x = ",x2, 'y = ',y2)
    test2 = rectangular(x2,y2)
    print("x*y =  ", test2)
    
    print("\nTestcase 2:")
    x3 = -59724
    y3 = 783
    print("x = ",x3, 'y = ',y3)
    test3 = rectangular(x3,y3)
    print("x*y =  ", test3)

    print("\nTestcase 4:")
    x4 = 8516
    y4 = -82147953548159344
    print("x = ",x4, 'y = ',y4)
    test4 = rectangular(x4,y4)
    print("x*y =  ", test4)
    
    print("\nTestcase 5:")
    x5 = 45952456856498465985
    y5 = 98654651986546519856
    print("x = ",x5, 'y = ',y5)
    test5 = rectangular(x5,y5)
    print("x*y =  ", test5)
    
    print("\nTestcase 6:")
    x6 = -45952456856498465985
    y6 = -98654651986546519856
    print("x = ",x6, 'y = ',y6)
    test6 = rectangular(x6,y6)
    print("x*y =  ", test6)

__main__()

