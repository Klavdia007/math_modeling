
import constant as cnst

def energy(m,h,v):
    E = (m*v**2/2)+m*cnst.g*h
    return E
print(energy(m=10,h=5,v=2))
