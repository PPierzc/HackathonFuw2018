import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt

# data = np.load('/Users/paulpierzchlewicz/Downloads/macierz_china.npy')
# ostaniec = data[390:490, 260:360]
# gora = data[470:570, 810:910]
# data = np.hstack((ostaniec, gora))
# data /= 11

data = pd.read_csv('/Users/paulpierzchlewicz/Downloads/skupaj.xyz', sep=';', names=['x', 'y', 'z'])

# data = data[::100]
# data = data.iloc[::100, :]
Unique_x = set(data['x'].values.tolist())
Unique_y = set(data['y'].values.tolist())

uX = len(Unique_x)
uY = len(Unique_y)

#ziped = list(zip(data['x'],data['y'],data['z']))

# i = 0
# print('matrix')
# for xindex, x in enumerate(Unique_x):
#     for k in range(len(Unique_x)):
#         if x==ziped[k][0]:
#             z[k, i] = ziped[k][2]
#             i+=0
#         elif i>=len(Unique_y):
#             i=0
#             break

print(uX)
print(uY)
magic = 10
z = np.zeros((uY//magic, uX//magic))




print(z.shape)
for i in range(0,uX,magic):

    print(i/uX*100)
    for j in range(0,uY,magic):
        #print(i,j)
        #print(j)
        # if j % 100 ==0:
        #print(data['z'][i*uX+j])
            #print([i*uY+j])
        #print(data['z'][i*magic+j*magic])
        z[i//magic,j//magic] = data['z'][i/magic+j]

# for i in range(0,uX):
#
#     print(i/uX*100)
#     for j in range(0,uY):
#         #print(j)
#         if j % 100 ==0 and i%100==0:
#         #print(data['z'][i*uX+j])
#             #print([i*uY+j])
#             z[i//100,j//100] = data['z'][i*uY+j]

np.savetxt('dolki.np',z)
plt.imshow(z)
plt.show()

# # surface = go.Surface(z=data, colorscale='Earth')
# surface = go.Surface(x=data['x'].values.tolist(), y=data['y'].values.tolist(), z=data['z'].values.tolist(), colorscale='Earth')
# layout = go.Layout(
# scene = dict(
# aspectmode = "manual",
# # aspectratio = dict( x = 11, y = 11, z = 1),
# aspectratio = dict( x = 1, y = 1, z = 1),
# ))
# fig = go.Figure(data=[surface], layout=layout)
# plot(fig, filename='test_11')
