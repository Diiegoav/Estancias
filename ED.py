from numpy import *
import matplotlib.pyplot as plt

def fun1(p):
    return ((p*p).sum(axis=1))

may = 5
men = -5
nparts = 2
ndims = 5
gmax = 10
CR = .5
F = 1.4
p = random.random((nparts,ndims))
p = p *(may - men) + men
u = zeros((nparts,ndims))
fx = fun1(p)
g = 0
while g < gmax
    i = 0
    for i in range(len(p)):
        vec = []
        s = 0
        for s in range(len(p)):
            vec.append(s)
        random.shuffle(vec)
        r1 = vec[0]
        r2 = vec[1]
        r3 = vec[2]

        jrand = random.randint(p[r2])
        j = 0
        for j in range(ndims):
            if random.random((nparts,ndims)) < CR or j == jrand:
                u[i][j] = p[r3][j] + F * (p[r1][j] - p[r2][j])
            else:
                u[i][j] = p[i][j]

        if fun1(u[i])<= fun1(x[i]):
            p[i] = u[i]
        else:
            p[i] = p[i]
    g += 1
