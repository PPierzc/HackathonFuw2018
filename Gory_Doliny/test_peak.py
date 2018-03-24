import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as filters
from skimage.feature import peak_local_max

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

def find_maximas(data):
    coordinates = peak_local_max(data, min_distance=1)
    return coordinates

def validate_maxima(coordinate, data):
    grad = np.gradient(data)
    i = 0
    run = True
    while run:
        i += 1
        try:
            gradII = sum(abs(np.array(grad)))[coordinate[0]-i:coordinate[0]+i+1,coordinate[1]-i:coordinate[1]+i+1]
            condition = sum(gradII[0, :] + gradII[gradII.shape[0] - 1, :] + gradII[:, 0] + gradII[:, gradII.shape[0] - 1])
        except:
            run = False
        if not condition:
            return True
            run = False
    return False

def show_maximas(coordinates, data):
    zeros = np.zeros(data.shape)
    print(zeros.shape)
    print(data.shape)
    for coordinate in coordinates:
        zeros[coordinate[0], coordinate[1]] = 10
    plt.imshow(zeros)
    plt.show()

if __name__ == '__main__':
    data = np.loadtxt('/Users/paulpierzchlewicz/Downloads/data.np')
    peak = data[330:355, 400:440]

    fig,ax = plt.subplots(1)
    ax.imshow(peak, cmap='rainbow')
    # rect = patches.Rectangle((275,335),50,50,linewidth=1,edgecolor='r',facecolor='none')
    # ax.add_patch(rect)
    plt.show()



    maximas = find_maximas(peak)
    show_maximas(maximas, peak)

