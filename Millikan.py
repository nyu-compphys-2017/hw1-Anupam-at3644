
# coding: utf-8

# In[6]:

import numpy as np
import matplotlib.pyplot as plt

#N->no. of points
#a->left limit
#b->right limit

file="millikan.txt"

data=np.genfromtxt(file)
#print (x)
class millikan(object):
    def __init__(self,N,a,b):
        self.N=N
        self.a=a
        self.b=b
        self.width=(b-a)/N
        self.x_array=np.arange(self.a,self.b,self.width)
    
    def seed_m(self):     #using 1st and last data point
        seed_m=(data[-1,1]-data[0,1])/(data[-1,0]-data[0,0])
        return seed_m
    def seed_c(self):
        seed_c=data[-1,1]-(self.seed_m()*data[-1,0])
        return seed_c
    
    def y_array(self):
        seed_m=self.seed_m()
        seed_c=self.seed_c()
        y_array=[]
        for i in self.x_array:
            y_array.append((seed_m*i)+seed_c)
        return np.array(y_array)
    
    def E_x(self):
        sigma_x=np.sum(self.x_array)
        return sigma_x/self.N
    def E_y(self):
        sigma_y=np.sum(self.y_array())
        return sigma_y/self.N
    def E_xx(self):
        sigma_xx=np.sum(self.x_array**2)
        return sigma_xx/self.N
    def E_xy(self):
        sigma_xy=np.sum(self.x_array*self.y_array())
        return sigma_xy/self.N
    
    def slope(self):
        return ((self.E_xy()-(self.E_x()*self.E_y()))/(self.E_xx()-(self.E_x()**2)))
    def const(self):
        return (((self.E_xx()*self.E_y())-(self.E_x()*self.E_xy()))/(self.E_xx()-(self.E_x()**2)))
        

        
plt.scatter(data[:,0],data[:,1],c='red',label="Measurements")

m=millikan(100,4e14,13e14)
slope=m.slope()
const=m.const()
x_array=m.x_array
y_array=m.y_array()
plt.plot(x_array,y_array,'-',label="Fitted Line")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Potential(V)")
h=(slope*1.602e-19)
h_real=6.62607004e-34
error=(h_real-h)*100/h_real
print ("Planck Constant (Actual)=",h_real)
print("Calculated value(slope*q_e)=",h)
print("Error=",error,"%")
plt.legend()
plt.plot()
plt.savefig("Millikan.png")
plt.show()






# In[16]:

#a=np.array([[1,2],[3,4],[5,6]])
a=np.array([1,2,3])
print (np.dot(a,a))



# In[ ]:



