#Program to plot  a hyperbola
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
#import subprocess
#import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
theta = np.linspace(-5,5,len)

#Given hyperbola parameters
#Eqn : x.T@V@x = F
V = np.array(([-1,0],[0,4]))
F = 1


V0 = np.array(([1,0],[0,4]))
F0 = 1


#Standard Eqn : y.T@D@y=1
#comparing these equations, get :  
#y = P.T@x/sqrt(F)
#P.T@V@P = D
#P.T@P = I

eigval,eigvec = LA.eig(V)
print(eigval)
print(eigvec)


eigval1,eigvec1 = LA.eig(V0)
print(eigval1)
print(eigvec1)


D = np.diag(eigval)
P = eigvec
print("D=\n",D)
print("P=\n",P)



D0 = np.diag(eigval1)
P0 = eigvec1
print("D=\n",D0)
print("P=\n",P0)


#Generating points on the hyperbola at origin
#y = np.zeros((2,len))
#y[0,:] = 1/eigval[0]*np.cosh(theta)
#y[1,:] = 1/eigval[1]*np.sinh(theta)

#Standard hyperbola : y.T@D@y=1
y1 = np.linspace(-1,1,len)
y2 = np.sqrt((1-D[0,0]*np.power(y1,2))/(D[1,1]))
y3 = -1*np.sqrt((1-D[0,0]*np.power(y1,2))/(D[1,1]))
y = np.hstack((np.vstack((y1,y2)),np.vstack((y1,y3))))



y10 = np.linspace(-1,1,len)
y20 = np.sqrt((1-D0[0,0]*np.power(y10,2))/(D0[1,1]))
y30 = -1*np.sqrt((1-D0[0,0]*np.power(y10,2))/(D0[1,1]))
y0 = np.hstack((np.vstack((y10,y20)),np.vstack((y10,y30))))


#Plotting standard hyperbola
plt.plot(y[0,:len],y[1,:len],color='b',label='Std hyperbola')
plt.plot(y[0,len+1:],y[1,len+1:],color='b')


#Plotting standard hyperbola
#plt.plot(y[0,:],y[1,:],label='Ellipse at origin')

#Affine Transformation
#Equation : y = P.T@(x-c)/(K**0.5)
x = (P @ (y)) * F**0.5

x0 = (P0 @ (y0)) * F0**0.5


#Plotting required hyperbola
plt.plot(x[0,:len],x[1,:len],color='r',label='Hyperbola H')
plt.plot(x[0,len+1:],x[1,len+1:],color='r')


plt.plot(x0[0,:len],x0[1,:len],color='g',label='Locus of Hyperbola H')
plt.plot(x0[0,len+1:],x0[1,len+1:],color='g')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

#if using termux
#plt.savefig('../figs/hyperloop.pdf')
#plt.savefig('../figs/hyperloop.eps')
#subprocess.run(shlex.split("termux-open ../figs/hyperloop.pdf"))
#else

plt.show()
