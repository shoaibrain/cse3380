from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt

# (a) Create a Python script that generates a plot of the L1 distance versus L2
# distance. That is, the y-axis represents the output of each function and the
# x-axis is the vector u−v. To keep visualization simple, generate a range of
# values from -1 to 1 as your x values.
def _plot(l1,l2):
 x_range = np.linspace(-1,1,num=2,endpoint=True)
 y_axis = [l1,l2]
 # Define plot space
 plt.scatter(x_range,y_axis)
 plt.xlabel("vector u-v")
 plt.ylabel("L1 and L2")
 plt.show()

# (b) Create a function in Python that, given two vectors, computes the L1 and L2
# loss. The loss should be printed out.
def _loss(vectors):
 v1,v2 = vectors
 #calculate L1 loss from v1
 L1 = round(distance.cityblock(v1,v2),2) #round to two decimal places
 #calculate L2 loss from v2
 L2 = round(distance.euclidean(v1,v2),2) #rounded to two decimal places
 # the loss should be printed out
 # print(f'L1 loss is: {L1}')
 # print(f'L2 loss is: {L2}')
 return (L1,L2)

# (c) To test the above function, randomly generate two sets of scalars and pass
# them as input to your function.
def _random_scalar():
 scalar1 =  np.random.randint(0, high=5, size=(1,3), dtype='l') #1x3 row vector
 scalar12 =  np.random.randint(0, high=5, size=(1,3), dtype='l')#1x3 row vector
 #pass these scalar into function to calculate loss L1 and L2
 losses = _loss((scalar1,scalar12))
 print(losses)
 return losses


if __name__ == '__main__':
 l1,l2 = _random_scalar()
 _plot(l1,l2)
 
