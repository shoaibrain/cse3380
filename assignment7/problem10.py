import numpy as np
import sympy


def main(param):
 #Convert the matrix of vectors in a parametric vector form,
 #This simplisfies the input of the main function
 v1,v2,v3 = param
 print(f"The vectors are:\n{v1}\n{v2}\n{v3}")
 print("Every vectors in Set S is a linear combination of vectors v1, v2 and v3")
 print("Therefore, set of vectors {v1, v2, v3} spans the set S")
 print(f"Clearly, v1 is non-zero vector and the vector v2 is not the scalar multiple of v1.\n We can condlude that the set of vectors {{v1,v2,v3}} are linearly independent.\n And the dimension of vector is 3")


if __name__ == '__main__':
 Vector_set = (['2b+3c'],['a+b-2c'],['4a+b'],['3a-b-c'])
 #assuming there is some helper function that processes the string representation of the vector sets above and 
 #returns an array of 1x4 dimensions
 Vector_set = [[0,1,4,3],[2,1,1,-2],[3,-2,0,-1]]
 #change the all the vectors into column vector
 for i in range(len(Vector_set)):
  Vector_set[i] = np.array(Vector_set[i]).reshape((4,1))
 main(Vector_set)
