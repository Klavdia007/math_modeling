import constant as cnst

def square(fig, a=1, b=1, h=1, r=1):
    if fig == 'rectangle':
        x = a*b
    elif fig =='triangle':
        x = a*h/2
    else:
        x = cnst.p *r**2
    return x

print(square('triangle', a=1, h=4)) 
