#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def alaCarte(x,y):
    sign = 1
#getting absolute value of x and y
    if x < 0:
        x *= -1
        sign *= -1
    if y < 0:
        y *= -1
        sign *= -1
#identifying small and large number        
    if x > y:
        s = y
        l = x
    else:
        s = x
        l = y
    
#initializing result variable  
    if s%2 != 0:
        result = l
    else:
        result = 0
    while s > 0:
        s = s//2
        l = l*2
        if s%2 != 0:
            result += l 

#assigning sign to the result
    if sign < 0:
        result = -1*result
    return result


# In[ ]:


def __main__():
    print("\nTestcase 1:")
    x1 = 7000
    y1 = 7294
    print("x = ",x1, 'y = ',y1)
    test1 = alaCarte(x1,y1)
    print("x*y =  ", test1)

    print("\nTestcase 2:")
    x2 = 25
    y2 = 5038385
    print("x = ",x2, 'y = ',y2)
    test2 = alaCarte(x2,y2)
    print("x*y =  ", test2)
    
    print("\nTestcase 3:")
    x3 = -59724
    y3 = 783
    print("x = ",x3, 'y = ',y3)
    test3 = alaCarte(x3,y3)
    print("x*y =  ", test3)

    print("\nTestcase 4:")
    x4 = 8516
    y4 = -82147953548159344
    print("x = ",x4, 'y = ',y4)
    test4 = alaCarte(x4,y4)
    print("x*y =  ", test4)
    
    print("\nTestcase 5:")
    x5 = 45952456856498465985
    y5 = 98654651986546519856
    print("x = ",x5, 'y = ',y5)
    test5 = alaCarte(x5,y5)
    print("x*y =  ", test5)
    
    print("\nTestcase 6:")
    x6 = -45952456856498465985
    y6 = -98654651986546519856
    print("x = ",x6, 'y = ',y6)
    test6 = alaCarte(x6,y6)
    print("x*y =  ", test6)

__main__()

