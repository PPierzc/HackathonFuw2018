import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import skimage.filters as skimage
import scipy.ndimage.filters as filters
import time

def filter_map(data):
    kernel = np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 2, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ])
    kernel = kernel/14
    filtered_data = filters.convolve(data, kernel)
    return filtered_data

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

data = np.loadtxt('/Users/paulpierzchlewicz/Downloads/data.np')

peak1 = data[330:355, 400:440]
mount = data[660:700, 640:730]
plain = data[660:700, 450:520]
freq_0 = np.fft.rfftfreq(data.shape[0])
freq_1 = np.fft.rfftfreq(data.shape[1])

kernel = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 2, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
])

print()
kernel = kernel/14
filtered_peak = filters.convolve(peak1, kernel)
filtered_peak = filters.convolve(filtered_peak, kernel)
filtered_peak = filters.convolve(filtered_peak, kernel)
filtered_peak = filters.convolve(filtered_peak, kernel)
filtered_mount = filters.convolve(mount, kernel)

# filtered_data = filters.convolve(data, kernel)
s = time.time()
filtered_data = skimage.gaussian(data)
print(time.time() - s)
# show_fit(plain)
# show_fit(peak1)
# peak1 = filtered_data[330:355, 400:440]
# mount = filtered_data[660:700, 640:730]
# plain = filtered_data[660:700, 450:520]
# # show_fit(peak1)
# # show_fit(filtered_peak)
# # show_fit(mount)
# show_fit(plain)
# show_fit(filtered_mount)

peaks = np.load('./Gory_Doliny/peaks.npy')

print(peaks)

