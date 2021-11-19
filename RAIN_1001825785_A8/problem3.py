import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#create 3X1 matrix
def random3Dvectors():
    """
    Generates a random 3D unit vector (direction) with a uniform spherical distribution
    Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    :return:
    """
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return (x,y,z)

def _projections():
 V  = np.array(random3Dvectors())
 v1,v2,v3 = V
 U = np.array(random3Dvectors())
 u1,u2,u3 = U
 ax = plt.figure().add_subplot(projection='3d')
 #calculate projection of two 3D vectors
 projection = None
 #plot main original vectors
 ax.quiver(v1,v2,v3,u1,u2,u3, length=0.1, normalize=True)
 #projection of vector V
 # finding norm of the vector v
 v_norm = np.sqrt(sum(V**2))  
 proj_of_u_on_v = (np.dot(U, V)/v_norm**2)*V
 #projection of vector U
 # finding norm of the vector U
 u_norm = np.sqrt(sum(U**2)) 
 proj_of_v_on_u = (np.dot(V, U)/u_norm**2)*V 
 #plot the result, sho wth original value on plot too
 prov1,prov2,prov3 = proj_of_u_on_v
 prou1,prou2,prou3 = proj_of_v_on_u
 ax.quiver(prov1,prov2,prov3,prou1,prou2,prou3,colors= 'c', length=0.1, normalize=True)

 #different color: show original vector as well as projected vector with different color

 plt.show()

if __name__ == '__main__':
 _projections()