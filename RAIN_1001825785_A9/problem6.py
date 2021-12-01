"""
6. Using the dataset dataset2.txt, available through Canvas, find the least squares
solution using np.linalg.lstsq. You can load the data using np.loadtxt. After
finding the least squares solution, plot the data and the solution using matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
def main():
 #load data
 data  = np.loadtxt('dataset2.txt',encoding='bytes')
 x = data[:,0]
 y = data[:,1]
 #  y = mx + c
 a = np.array([x, np.ones(len(x))]).T  #x axis is 2d array
 values = np.linalg.lstsq(a,y,rcond = None)[0]
 plt.scatter(x,y)
 m = values[0] #slope
 c = values[1] # y intercept
 _y = x * m + c #equation of line
 plt.plot(x, _y, c='r')
 plt.xlabel("X")
 plt.ylabel("Y")
 plt.show()

if __name__ == '__main__':
 main()