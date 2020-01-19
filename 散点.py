import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.gca(projection='3d') #得到3D模式下实例ax

xs=np.random.rand(50)*10
ys=np.random.rand(50)*10+20
zs1=np.random.rand(50)*10
zs2=np.sqrt(xs**2+ys**2)

ax.scatter(xs,ys,zs=zs1,zdir='z',c='cornflowerblue',marker='o',s=40)
ax.scatter(xs,ys,zs=zs2,zdir='z',c='purple',marker='^',s=40)

ax.set(xlabel="x",ylabel='Y',zlabel='Z')

plt.show()
