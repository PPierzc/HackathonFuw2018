import numpy as np
from skimage.feature import peak_local_max
import matplotlib.pyplot as plt
from pprint import pprint
from scipy import ndimage as ndi


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

data = np.loadtxt('/Users/paulpierzchlewicz/Downloads/data.np')

# data = np.random.rand(1000,1000)
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


import time
#zero padding
zeros = np.zeros((data.shape[0]+4, data.shape[1]+4))
zeros[2:2+data.shape[0], 2:2+data.shape[1]] = data
data = zeros

start = time.time()
zeros = np.zeros(data.shape)

maximas = find_maximas(data)
print(len(maximas))
# for i in maximas:
#     validate_maxima(i, data)
#     # print("Górka") if validate_maxima(i, data) else None
#     # print("{}, {}".format(i, 'Górka' if validate_maxima(i, data) else 'Nie Górka'))
# print(time.time() - start)