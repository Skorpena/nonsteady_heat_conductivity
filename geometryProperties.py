import numpy as np
import constants as c

N = len(c.s)*c.n + 1 #amount of nodes in len(c.s) layers

def gridMap():
    '''devides sheet/plate into finite element grid'''
    x = [0]
    for i in range(N-1):
        j = 0 if i <= c.n-1 else 1
        x.append(x[i] + c.s[j]/c.n)
    x = np.round(np.array(x),3)
    return x

gM = gridMap()

if __name__ == '__main__':
    s = [10, 20]
    c.s = s
    x = gridMap()
    for i in range(N):
        print(i, x[i])
