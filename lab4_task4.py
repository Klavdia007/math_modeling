import numpy as np

def func(a, b, N):
    x = np.arange(a, b, N)
    y = x ** 2
    return y

print(func(1,9,1 ))