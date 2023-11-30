import numpy as np

def func_w(a,n):
    b=1
    if n%2==0:
        while n>0:
            b=b*a;
            n-1           
            return b
            break
            
    else: print('хз')
    
print(func_w(3,2))