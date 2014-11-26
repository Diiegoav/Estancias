from numpy import *
import matplotlib.pyplot as plt

def fun1(x):
    return ((x*x).sum(axis=1))

may = 10
men = -10
nparts = 5
ndims = 3
gmax = 50
CR = .5
F = 1.8
x = random.random((nparts,ndims))
x = x *(may - men) + men
u = zeros((nparts,ndims))
fx = fun1(x)
fu = fun1(u)
g = 0
while g < gmax:
    for i in range(len(x)):
        vec = []
        for s in range(len(x)):
            vec.append(s)
        random.shuffle(vec)
        r1 = vec[0]
        r2 = vec[1]
        r3 = vec[2]
        jrand = random.randint(ndims)
        for j in range(ndims):
            if random.random() < CR or j == jrand:
                u[i][j] = x[r3][j] + F * (x[r1][j] - x[r2][j])
            else:
                u[i][j] = x[i][j]
            fx = fun1(x)
            fu = fun1(u)
        print(fx)
        if fu[i] <= fx[i]:
            x[i] = u[i]
        else:
            x[i] = x[i]
    g += 1
