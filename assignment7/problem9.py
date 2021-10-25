import numpy as np
import sympy

def getvectorX(B,xB):
  """
  returns col vector determined by coordinate vector xB and basis B
  only works on 3x3 basis and 1x3 coordinate vector
  """
  b1,b2,b3 = None,None,None
  for index,b in enumerate(B):
    #change each row vector to column vector 
    if index == 0: b1 = np.array(b).reshape((3,1))
    elif index == 1: b2 = np.array(b).reshape((3,1))
    elif index == 2: b3 = np.array(b).reshape((3,1))
  #multiply numpy.ndarray with scalar in xB
  for index,xb in enumerate(xB):
    if index == 0: b1 = np.multiply(b1,xb)
    elif index == 1: b2 = np.multiply(b2,xb)
    elif index == 2: b3 = np.multiply(b3,xb)
  #add all vectors
  temp =  np.add(b1,b2) #add first two vector, np.add takes 2 param
  return np.add(temp,b3) #add third vector









if __name__ == "__main__":
  setB = ([0,-1,-1],[-4,0,0],[6,6,3])
  xB = [-2,6,1]
  print(f"Vector X determied by setB and xB is:\n{getvectorX(setB,xB)}")
