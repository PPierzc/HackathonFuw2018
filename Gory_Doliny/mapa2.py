#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:49:12 2018

@author: mateusz
"""
import numpy as np
import matplotlib.pyplot as plt
x,y,z=[],[],[]
file=open('data_DEM.xyz')
for i in file:
    row = i.split()
    x.append(float(row[0]))
    y.append(float(row[1]))
    z.append(float(row[2]))
x_set=set(x)
x_list=list(x_set)
x_list=sorted(x_list)

y_set=set(y)
y_list=list(y_set)
y_list=sorted(y_list)
x_count=[]
for i in x_list:
    x_count.append(x.count(i))
y_count=[]
for i in y_list:
    y_count.append(y.count(i)) 
zeros=np.zeros((len(y_count),len(x_count)))
k=0
p=0
q=0
d=0
for i in x_count:
    for j in range(p,i+q):
        zeros[d,k]=z[j]
        d=d+1
    d=0
    k=k+1
    p=i+q
    q=q+i
zeros[zeros==0]=min(z)
plt.figure(figsize=(20,10))
plt.imshow(zeros,interpolation='none',cmap='flag')
plt.colorbar()
plt.savefig('dupa.png')
plt.show()