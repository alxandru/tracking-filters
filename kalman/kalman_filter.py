from matrix.matrix import *


def filter(measurements, x, P):
    I =  matrix([[]])
    I.identity(P.dimx)
    for n in range(len(measurements)):
        # measurement update
        #Z = matrix([[measurements[n]]])
        #y = Z - (H * x)
        Z = matrix([measurements[n]])
        y = Z.transpose() - (H * x)
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
        x = x + (K * y)

        P = (I - (K * H)) * P

        # prediction
        x = (F * x) + u
        P = F * P * F.transpose()

        print('x= ')
        x.show()
        print('P= ')
        P.show()

## 2-D
#measurements = [1, 2, 3]
#x = matrix([[0.], [0.]]) # initial state (location and velocity)
#P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
#u = matrix([[0.], [0.]]) # external motion
#F = matrix([[1., 1], [0, 1.]]) # next state function
#H = matrix([[1., 0]]) # measurement functions
#R = matrix([[1.]]) # measurement unceartainty
#filter(measurements, x, P)

## 4-D
measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
initial_xy = [4., 12.]
x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)
u = matrix([[0.], [0.], [0.], [0.]]) # external motion
P =  matrix([[0.,0.,0.,0.],[0.,0.,0.,0.],[0.,0.,1000.,0.],[0.,0.,0.,1000.]])
# initial uncertainty: 0 for positions x and y, 1000 for the two velocities
F =  matrix([[1.,0.,.1,0.],[0.,1.,0.,.1],[0.,0.,1.,0.],[0.,0.,0.,1.]])
# next state function: generalize the 2d version to 4d
H =  matrix([[1.,0.,0.,0.],[0.,1.,0.,0.]])
# measurement function: reflect the fact that we observe x and y but not the two velocities
R =  matrix([[.1,0],[0,.1]])
# measurement uncertainty: use 2x2 matrix with 0.1 as main diagonal
filter(measurements, x, P)
