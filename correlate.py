"""
Calculates the correlation of a set of paraboloids
"""

import numpy as np

def __curvature(_a, _b):
    '''
    :param _a: parameter a of the paraboloid function
    :param _b: parameter b of the paraboloid function
    :return: the curvature at the point 0,0 of the paraboloid
    '''
    return 4 / (_a ** 2 * _b ** 2)

def correlate(data):
    '''
    :param data: a 2D array which has the parameters of each paraboloid
    :return: the correlation coefficient of the set
    '''
    _a = data[:, 0]
    _b = data[:, 1]
    _h = data[:, 2]
    curvature = np.array([__curvature(_a[index], _b[index]) for index in range(len(_a))])
    correlation = np.corrcoef((curvature, _h))[0, 1]
    return correlation

if __name__ == '__main__':
    DATA = np.array([
        [1, 2, 3],
        [4, 1, 4],
        [6, 12, 1],
        [3, 1, 2],
    ])
    print(correlate(DATA))
