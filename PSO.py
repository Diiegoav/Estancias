from numpy import *
import matplotlib.pyplot as plt

men = -100
may = 100
W = 0.7
C1 = 1.4
C2 = 1.4
gmax = 10
nparts = 5
ndims = 30

def fun1(x):
	return ((x*x).sum(axis=1))

def fun2(x):
	return (abs(x).sum(axis=1) + prod(abs(x),axis=1))

def fun3(x):
	aux = 0
	aux2 = zeros(len(x))
	for i in range(len(x)):
		for j in range(len(x[i])):
			for h in range(j+1):
				aux += x[i][h]
			aux2[i] += aux*aux
	return aux2


x = random.random((nparts,ndims))
x = x * (may - men) + men
fx = fun3(x)
pbest = x.copy()
fx_pbest = fx.copy()
index = argmin(fx).copy()
gbest = x[index].copy()
fx_gbest = fx[index]


grafo = []
v = zeros((nparts,ndims))
i = 0

while i < gmax:
	v = W*v + C1*random.random((nparts,ndims))*(pbest-x) + C2*random.random((nparts,ndims))*(gbest-x)
	x = x + v
	ladme = x > men
	ladma = x < may
	pro = sum(x[ladme]) + sum(x[ladma]) / len(x[ladme]) + len(x[ladma])
	ladme = x < men
	ladma = x > may
	x[ladme] = pro
	x[ladma] = pro

	fx = fun3(x)
	index = fx < fx_pbest
	pbest[index] = x[index]
	fx_pbest[index] = fx[index]
	index = argmin(fx)

	if fx_pbest[index] < fx_gbest:
		gbest = x[index]
		fx_gbest = fx[index]
	grafo.append(fx_gbest)
	i += 1

print (fx_pbest," : ",gbest)
plt.plot(range(gmax),grafo)
plt.show()
