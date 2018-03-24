import numpy as np

def curvature(a, b):
    return a*b

def correlate(data):
    a = data[:,0]
    b = data[:,1]
    h = data[:,2]
    circ = np.array([curvature(a[index],b[index]) for index in range(len(a))])
    correlation = np.corrcoef((circ, h))[0,1]
    return correlation

if __name__ == '__main__':
    data = np.array([
        [1, 2, 3],
        [4, 1, 4],
        [6, 12, 1],
        [3, 1, 2],
    ])
    print(correlate(data))