import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pprint
from matplotlib import cm
data =  np.loadtxt('data.np')



scale = 50
for i in range(min(data.shape)//scale-1):
    for j in range(min(data.shape)//scale-1):
        
        
        
        Z  = data[i*scale:(i+1)*scale,j*scale:(j+1)*scale]
        #xs, ys = np.meshgrid(np.arange(points.shape[1]), np.arange(points.shape[0]))
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_zlim(np.min(data),np.max(data))
        X, Y = np.meshgrid(np.arange(Z.shape[1]), np.arange(Z.shape[0]))
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=3, cstride=3,cmap='hot')
        #cset = ax.surface(X, Y, Z, zdir='z', offset=-50, cmap=cm.hot)
        #cset = ax.contourf(X, Y, Z, zdir='x', offset=0, cmap=cm.coolwarm)
        #cset = ax.contourf(X, Y, Z, zdir='y', offset=50, cmap=cm.coolwarm)
        # ax.set_title('dupa')
        ax.set_title('x %s-%s,y %s-%s'%(i*scale,(i+1)*scale,j*scale,(j+1)*scale))
        ax.set_xlabel('X')
        ax.set_xlim(0,50)
        ax.set_ylabel('Y')
        ax.set_ylim(0,50)
        ax.set_zlabel('Z')
        ax.set_zlim(np.min(Z),np.max(Z))


        #plt.savefig('całość png')
        plt.show()