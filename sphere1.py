
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np



#creating x,y for 3D plotting
len = 10
xx, yy = np.meshgrid(range(len), range(len))
#print(xx)
#print(yy)

#setting up plot
fig = plt.figure()
#print(fig)
ax = fig.add_subplot(111,projection='3d',aspect='equal')
#print(ax)

A = np.array([2,1,-2])
B = np.array([1,1,0])
#C = np.array([0,0,2])

#finding cross product
D = np.cross(A,B)
print(D)

#E = np.cross(D,C)
#print(E)

#defining planes
n1 = np.array([2,1,-2]).reshape((3,1))
c1 = 2

#corresponding z for planes
z1 = 0.5*((c1-n1[0]*xx-n1[1]*yy)*1.0)/(n1[2])

r = 2
O = np.array([0,0,0])

len = 20

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
x_circ = np.zeros((3,len,len))
x_circ[0,:] = r*np.cos(u)*np.sin(v)
x_circ[1,:] = r*np.sin(u)*np.sin(v)
x_circ[2,:] = r*np.cos(v)
x_circ = (x_circ.T + O).T


#generating points in Line 
l1_p = line_dir_pt(A,O)
l2_p = line_dir_pt(B,O)
l3_p = line_dir_pt(D,O)

#plotting planes
ax.plot_surface(xx, yy, z1, color='y',alpha=0.2)

# draw a point
ax.scatter(O[0],O[1],O[2], color="g", s=10)
ax.scatter(0,0,2, color="b", s=10)

plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line $A$")
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line $B$")
plt.plot(l3_p[0,:],l3_p[1,:],l3_p[2,:],label="Line $D$")
ax.plot_wireframe(x_circ[0,:], x_circ[1,:], x_circ[2,:], label='$Sphere$', color="r")

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')
#fig = plt.figure()
#ax = fig.gca(projection='3d')
ax.set_aspect("equal")

#if using termux
#plt.savefig('../figs/incircle.pdf')
#plt.savefig('../figs/incircle.eps')
#subprocess.run(shlex.split("termux-open ../figs/incircle.pdf"))
#else
plt.show()
