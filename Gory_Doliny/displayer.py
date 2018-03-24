import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches

data = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 1, 0, 0],
    [0, 0, 2, 5, 3, 0, 0],
    [0, 0, 1, 2, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
])

patch_coordinates_x = 270
patch_coordinates_y = 315

data = np.loadtxt('/Users/paulpierzchlewicz/Downloads/data.np')

# fig,ax = plt.subplots(1)
# ax.imshow(data, cmap='rainbow')
# rect = patches.Rectangle((275,335),50,50,linewidth=1,edgecolor='r',facecolor='none')
# ax.add_patch(rect)
# plt.show()

print()

def show_fit(data):
    xs, ys = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
    # z = calculate_R(xs, ys)
    zs = xs ** 2 + ys ** 2

    fig = plt.figure()
    ax2 = Axes3D(fig)
    ax2.plot_surface(xs, ys, data, rstride=1, cstride=1, cmap='hot')
    plt.show()


peak1 = data[330:355, 400:440]
freq_0 = np.fft.rfftfreq(data.shape[0])
freq_1 = np.fft.rfftfreq(data.shape[1])

show_fit(data[330:355, 400:440])