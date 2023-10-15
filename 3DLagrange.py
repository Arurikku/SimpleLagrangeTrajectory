import numpy as np

def trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy): # any f(x,y) provided with partial F with x first and second, partial F with y first and second, and partial F with x and then y
    Kappa = 1 + (F_x**2)
    Lambda = F_x*F_y
    Mu = 1 + (F_y**2)
    Alpha = xdot**2*F_2x*F_x+(1/2)*ydot**2*F_xy+xdot*ydot*(F_y*F_2x+F_x*F_xy) - g*F_x - 2*xdot*F_x*(xdot*F_2x+ydot*F_xy) - ydot*F_xy*(ydot*F_y+xdot*F_x) - ydot*(xdot*F_y*F_2x+ydot*F_x*F_2y)
    Beta = ydot**2*F_2y*F_y+(1/2)*xdot**2*F_xy+ydot*xdot*(F_x*F_2y+F_y*F_xy) - g*F_y - 2*ydot*F_y*(ydot*F_2y+xdot*F_xy) - xdot*F_xy*(xdot*F_x+ydot*F_y) - xdot*(ydot*F_x*F_2y+xdot*F_y*F_2x)
    Y_dotdot = (Alpha*Lambda-Beta*Kappa)/(Lambda**2 - Kappa*Mu)
    X_dotdot = (Beta*Lambda-Alpha*Mu)/(Lambda**2 - Kappa*Mu)
    return (X_dotdot, Y_dotdot)

def trajectory_cone(x, xdot, y, ydot): # f(x,y) = sqrt(x² + y²)
    F_x = x / np.sqrt(x**2 + y**2)
    F_y = y / np.sqrt(x**2 + y**2)
    F_2x = (y**2) / ((x**2 + y**2) * np.sqrt(x**2 + y**2))
    F_2y = (x ** 2) / ((x ** 2 + y ** 2) * np.sqrt(x ** 2 + y ** 2))
    F_xy = -1 * (x * y) / ((x**2 + y**2) * np.sqrt(x ** 2 + y ** 2))
    return trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy)

def trajectory_parabola(x, xdot, y, ydot): # f(x,y) = x²+y²
    F_x = 2*x
    F_y = 2*y
    F_2x = 2
    F_2y = 2
    F_xy = 0
    return trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy)

def trajectory_bell(x, xdot, y, ydot): # f(x,y) = e^{-(x²+y²)}
    F_x = -2*x*np.exp(-1*(x**2+y**2))
    F_y = -2*y*np.exp(-1*(x**2+y**2))
    F_2x = 2*(2*(x**2)-1)*np.exp(-1*(x**2+y**2))
    F_2y = 2*(2*(y**2)-1)*np.exp(-1*(x**2+y**2))
    F_xy = 4*x*y*np.exp(-1*(x**2+y**2))
    return trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy)

def trajectory_sincos(x, xdot, y, ydot): # f(x,y) = sin(x) + cos(y)
    F_x = np.cos(x)
    F_y = -np.sin(y)
    F_2x = -np.sin(x)
    F_2y = -np.cos(y)
    F_xy = 0
    return trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy)

def trajectory_inclined_half_pipe(x, xdot, y, ydot): # f(x,y) = 0.01x² + 0.1y
    F_x = 0.02 * x
    F_y = 0.1
    F_2x = 0.02
    F_2y = 0
    F_xy = 0
    return trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy)

def trajectory_bumpy_half_pipe(x, xdot, y, ydot): # f(x,y) = 0.01cosh(x) + sin(y)
    F_x = 0.01*np.sinh(x)
    F_y = np.cos(y)
    F_2x = 0.01*np.cosh(x)
    F_2y = -np.sin(y)
    F_xy = 0
    return trajectory_general(xdot, ydot, F_x, F_y, F_2x, F_2y, F_xy)

def printForDesmos(tab): #Prints the coordinates in a way Desmos can understand
    for i in range(0, len(tab), stp):
        xPt = str(tab[i])
        if "e" in xPt:
            ind = xPt.index("e")
            print(xPt[:ind] + "*10^{" + xPt[ind + 1:] + "}", end=",")
            continue
        print(xPt, end=",")
    print()

x0,xdot_0, y0, ydot_0 = 5,-3,0,0
g=9.81

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
    prev_xdotdot,prev_ydotdot = trajectory_bumpy_half_pipe(prev_x, prev_xdot, prev_y, prev_ydot)
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