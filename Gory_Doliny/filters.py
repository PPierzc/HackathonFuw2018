import numpy as np
import scipy.ndimage.filters as filters

def filter_map(data):
    kernel = np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 2, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ])
    kernel = kernel/np.sum(kernel)
    filtered_data = filters.convolve(data, kernel)
    return filtered_data
