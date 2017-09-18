
# coding: utf-8

# In[1]:

import numpy as np
from cmath import sqrt
import matplotlib.pyplot as plt
        
#N->no. of points
#a->left limit
#b->right limit

class Point_Set(object):
    def __init__(self,N=2000,a=-2.0,b=2.0):
        self.N=N
        self.a=a
        self.b=b
        self.width=(b-a)/N

        self.x_cood=np.arange(a,b,self.width)
        self.y_cood=np.arange(a,b,self.width)

    
    def Mandelbrot(self, c):
        self.z_seed=complex(0,0)        
        for i in range(0,self.N):
            self.z_seed =(self.z_seed*self.z_seed)+c
            
            if abs(self.z_seed) > 2.0:
                return 0
  
        return 1
    
    def plot(self):
        trues = []
        falses = []
        ans = []
        for i in self.x_cood:
            for j in self.y_cood:
                c=complex(i,j)
                ans.append(self.Mandelbrot(c))
                if self.Mandelbrot(c) is 1:
                    trues.append([i, j])
                else:
                    falses.append([i, j])
#        print(ans.count(1))
#        print(ans.count(0))
        trues = np.array(trues)
        falses = np.array(falses)
#        print(len(false))
#        print (len(trues))
        plt.scatter(trues[:,0], trues[:,1], c="black", label="True")
        plt.scatter(falses[:,0], falses[:,1], c="white", label="False")
        plt.legend()
        plt.savefig("Mandelbrot.png")
        plt.show()
        

        
point_set = Point_Set()
point_set.plot()        


# In[ ]:



