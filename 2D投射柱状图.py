import matplotlib.pyplot as plt
import numpy as np
from  mpl_toolkits.mplot3d import  Axes3D

fig=plt.figure()  # 生成类的实例 fig
ax = fig.add_subplot(1,1,1,projection='3d') # 投射3D模式自取，得到坐标卓实例ax
colors=['r','b','y']
ylayerlist=[2,1,0]  # 投射层次序号

for color,layer in zip(colors,ylayerlist):
    x=np.arange(10)
    y=np.random.rand(10)
    ax.bar(x,y,zs=layer,zdir='y',color=color,alpha=0.7) # zs 层级序号 zdir 用z轴表示y的矩阵高度

ax.set(xlabel='x',ylabel='y',zlabel='z',yticks=ylayerlist)

plt.show()
