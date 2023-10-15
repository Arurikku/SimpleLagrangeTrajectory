import numpy as np

def trajectory_general(x, xdot, fdot, fdotdot): # valid for any f(x), but needs f'(x) and f''(x)
    return (-(xdot ** 2) * fdotdot(x) * fdot(x) - g * fdot(x)) / (1 + fdot(x) ** 2)

def trajectory_cosh(x, xdot): # f(x) = cosh(x)
    return trajectory_general(x, xdot, lambda x: np.sinh(x), lambda x: np.cosh(x))

def trajectory_square(x, xdot): # f(x) = x²
    return trajectory_general(x, xdot, lambda x: 2*x, lambda x: 2)

def trajectory_sine_step(x, xdot): # f(x) = x - sin(x)
    return trajectory_general(x, xdot, lambda x: 1 - np.cos(x), lambda x: np.sin(x))

def trajectory_bell(x, xdot): # f(x) = e^{-x²}
    return trajectory_general(x, xdot, lambda x: -2*x*np.exp(-1*(x**2)), lambda x: 2*(2*(x**2)-1)*np.exp(-1*(x**2)))

def printForDesmos(tab): #Prints the coordinates in a way Desmos can understand
    for i in range(0, len(tab), stp):
        xPt = str(tab[i])
        if "e" in xPt:
            ind = xPt.index("e")
            print(xPt[:ind] + "*10^{" + xPt[ind + 1:] + "}", end=",")
            continue
        print(xPt, end=",")
    print()

x0,xdot_0 = 3,5
g=9.81

dt = 0.0001
t_start = 0
t_end = 5
fric = 0.5
nPoints = 500

U = [[x0,xdot_0]]

curr_time = t_start
ctr = 0


while curr_time <= t_end:
    prev_x = U[ctr][0]
    prev_xdot = U[ctr][1] * (1-(fric*dt))
    prev_xdotdot = trajectory_cosh(prev_x, prev_xdot)
    U_next= [dt * prev_xdot + prev_x, dt * prev_xdotdot + prev_xdot]
    U.append(U_next)
    curr_time+=dt
    ctr += 1

x_points = np.array([el[0] for el in U])

print(len(x_points), "points")

stp = int((t_end - t_start)/(dt*nPoints))
print("Step value:",stp)
print("dt:", dt)
print("Friction:",fric)

print("Horizontal Position:")
printForDesmos(x_points)
print()
