
# coding: utf-8

# In[73]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm






def ObliczDlugosc(choosen_point,points):
    dlugosc=[]
    for point in points:
        vector_from_choosen=choosen_point-point
        dlugosc.append(np.linalg.norm(vector_from_choosen))
        
    return dlugosc


def RadialDistribution(points,density=1):
    rho_list_all=[]
    for choosen_point in tqdm(points): 
        
        dlugosc=ObliczDlugosc(choosen_point,points)
        
            
        rho_list=[]
        r_list=[]
        r=delta_r

        while r<3.5:
            n=0
            for i in dlugosc:
                if i > r and i< r +delta_r:
                    n+=1
            rho_list.append((1/density)*n/(2*np.pi*r*delta_r))

            r_list.append(r)
            r+=delta_r
        rho_list_all.append([rho_list])
    rho_list_all=np.sum(rho_list_all,axis=0)/len(points)

    return rho_list_all[0],r_list



if __name__=="__main__":
	

	delta_r=0.03

	r=delta_r



	polozenia=np.array([[0,0],[1,0],[2,0],[3,0],[4,0]])
	print(polozenia)
	rho,r=RozkladRadialny(points=polozenia)




	plt.figure()
	plt.scatter(r,rho)
	plt.show()

