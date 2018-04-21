import numpy as np

def __curvature(a, b):
    return 4 / (a**2 * b**2)

def correlate(data):
    a = data[:,0]
    b = data[:,1]
    h = data[:,2]
    curvature = np.array([__curvature(a[index], b[index]) for index in range(len(a))])
    correlation = np.corrcoef((curvature, h))[0,1]
    return correlation

if __name__ == '__main__':
    data = np.array([
        [1, 2, 3],
        [4, 1, 4],
        [6, 12, 1],
        [3, 1, 2],
    ])
    print(correlate(data))