import numpy as np

def printForDesmos(tab): #Prints the coordinates in a way Desmos can understand
    for i in range(0, len(tab), stp):
        xPt = str(tab[i])
        if "e" in xPt:
            ind = xPt.index("e")
            print(xPt[:ind] + "*10^{" + xPt[ind + 1:] + "}", end=",")
            continue
        print(xPt, end=",")
    print()

#Returns the mixed partial F_aj_ak assuming a correct ordering
def getMixedPartial(n, j, k, mixed_partials):
    return mixed_partials[k + n*j]

# coordsDot is the list of the time derivatives of coords (xdot and ydot for 3D)
# First order partials should be in order: F_a0, F_a1, ... , F_an
# Mixed partials should in order be: F_a0_a0, F_a0_a1, F_a0_a2, ... , F_a0_an, F_a1_a0, F_a1_a1, ... , F_an_an
# Note that second order partials are in the mixed partials
def trajectory_general(coordsDot, first_order_partials, mixed_partials):
    n = len(coordsDot)

    C_w = []
    Right_Matrix = []
    for w in range(n):

        # Building C_w, splitting the big sum into its terms to be able to read
        F_aw_aw = getMixedPartial(n, w, w, mixed_partials)
        F_aw = first_order_partials[w]
        aw_dot = coordsDot[w]
        chunk1 = aw_dot*F_aw_aw*sum([coordsDot[k]*first_order_partials[k] for k in range(n)])
        chunk2 = -g*F_aw
        chunk3 = -1 * sum([sum([coordsDot[k]*coordsDot[j]*first_order_partials[j]*getMixedPartial(n,k,w,mixed_partials) for j in range(n)]) for k in range(n)])
        chunk4 = -1* F_aw * sum([sum([coordsDot[k]*coordsDot[j]*first_order_partials[j]*getMixedPartial(n,k,w, mixed_partials) for j in range(n) if not j == w]) for k in range(n)])
        chunk5 = -F_aw*sum([sum([coordsDot[k]*coordsDot[j]*getMixedPartial(n,j,k, mixed_partials) for j in range(n)]) for k in range(n)])
        C_w.append(chunk1 + chunk2 + chunk3 + chunk4 + chunk5)

        # Building the matrix
        Matrix_Row = []
        k = 0
        while k < n:
            if k == w:
                Matrix_Row.append(1 + F_aw ** 2)  # Lambda_w
                k+=1
                continue
            Matrix_Row.append(F_aw * first_order_partials[k]) # H_k
            k+=1
        Right_Matrix.append(Matrix_Row)
    Matrix_Inv = np.linalg.inv(Right_Matrix)
    output_accels = Matrix_Inv.dot(C_w)
    return output_accels

def trajectory_bell3D(x, xdot, y, ydot): # f(x,y) = e^{-(x²+y²)}
    F_x = -2*x*np.exp(-1*(x**2+y**2))
    F_y = -2*y*np.exp(-1*(x**2+y**2))
    F_2x = 2*(2*(x**2)-1)*np.exp(-1*(x**2+y**2))
    F_2y = 2*(2*(y**2)-1)*np.exp(-1*(x**2+y**2))
    F_xy = 4*x*y*np.exp(-1*(x**2+y**2))
    return trajectory_general((xdot, ydot), (F_x, F_y), (F_2x, F_xy, F_xy, F_2y))

x0,xdot_0, y0, ydot_0 = 5,-3,0.5,0
g = 9.81

dt = 0.001
t_start = 0
t_end = 20
nPoints = 400
stp = int((t_end - t_start)/(dt*nPoints))

U = [[x0,xdot_0,y0,ydot_0]]

curr_time = t_start
ctr = 0

fricX, fricY = 0.1,0.1

while curr_time <= t_end:
    prev_x = U[ctr][0]
    prev_xdot = U[ctr][1] * (1-(fricX*dt))
    prev_y = U[ctr][2]
    prev_ydot = U[ctr][3] * (1-(fricY*dt))
    prev_xdotdot,prev_ydotdot = trajectory_bell3D(prev_x, prev_xdot, prev_y, prev_ydot)
    U_next= [dt * prev_xdot + prev_x, dt * prev_xdotdot + prev_xdot, dt * prev_ydot + prev_y, dt * prev_ydotdot + prev_ydot]
    U.append(U_next)
    curr_time+=dt
    ctr += 1


x_points = np.array([el[0] for el in U])
y_points = np.array([el[2] for el in U])

print("X Position:")
printForDesmos(x_points)
print()
print("Y Position:")
printForDesmos(y_points)