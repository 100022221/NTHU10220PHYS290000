# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:20:25 2014

"""

def prime(n):
    if n==2:
        print n,
    else:
        a=int(n**0.5)   
        b=range(a+2)
        k=0
        for i in b[2:]:
            if float(n)/i-int(n/i)==0:
                k=k+1             
        if k==0:
            print n,
b=int(raw_input('Put an integer:'))
a=range(b+1)
for i in a[2:]:
    prime(i)
