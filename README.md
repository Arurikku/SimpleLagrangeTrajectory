# Simple Lagrange Trajectory
Provides coordinates for a particle moving along a function curve (2D or 3D) using simple Lagrangian Mechanics
The principle of Lagrangian Mechanics is least action, which makes it incredibly easy to find a differential equation which describes accurately our system.

# 2D Version
The 2D version is a special case of the 3D one, so it is much easier to compute.
## Finding the Lagrangian
Let $f$ be a continuous differentiable function on our desired interval.\
Let $A$ be the point representing our particle, of coordinates $(x, y)$. We have therefore $A = (x, f(x))$\
Let us now construct the Lagrangian of our system.\
We have the potential energy: $E_p = mgy = mgf(x)$.\
And the kinetic energy: $E_k = \frac{1}{2}\cdot mv^2$.\
Since we are in cartesian coordinates, we have:\
$$v = \sqrt{\dot{x}^2+\dot{y}^2}$$
$$\iff v = \sqrt{\dot{x}^2+(\frac{d}{dt}f(x))^2}$$
$$\iff v = \sqrt{\dot{x}^2+\dot{x}^2\cdot f'(x)^2}$$
$$\iff v = \dot{x} \cdot \sqrt{1+ f'(x)^2}$$

Hence,  $$E_k = \frac{1}{2}\cdot m \dot{x}^2 (1+ f'(x)^2)$$

This leaves us with the Lagrangian:
$$L = E_k - E_p$$
$$\iff L = \frac{1}{2} \cdot m \dot{x}^2 (1+ f'(x)^2) - mgf(x)$$
## Using the principle of least action
The principle of least action tells us that:
$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = \frac{\partial L}{\partial x}$$
From the Lagrangian, we have:
$$\frac{\partial L}{\partial \dot{x}} = m \dot{x}(1+f'(x)^2)$$
$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = m (\ddot{x}(1+f'(x)^2)+2\dot{x}f'(x)f''(x))$$
$$\frac{\partial L}{\partial x} = mf'(x)(\dot{x}^2f''(x)-g)$$
From the principle of least action we have:
$$m (\ddot{x}(1+f'(x)^2)+2\dot{x}f'(x)f''(x)) = mf'(x)(\dot{x}^2f''(x)-g)$$
$$\iff \ddot{x} = \frac{mf'(x)(\dot{x}^2f''(x)-g) - 2\dot{x}f'(x)f''(x)}{1+f'(x)^2}$$
## Translating to python
While this seems to be an unsolvable, we can easily plot this using python.
First, let us lay the mathematical ground work:\
```math
U_i = \begin{pmatrix} x_i \\ \dot{x}_i \end{pmatrix}
```
```math
\dot{U}_i = \begin{pmatrix} \dot{x}_i \\ \ddot{x}_i \end{pmatrix}
```
We can simply write $\dot{U}_i$ as:
```math
\dot{U}_i = \frac{U_{i+1}-U_i}{dt}
```
giving us the recurrence relation that follows:
$$U_{i+1} = dt \cdot \dot{U}_i + U_i$$

Using the initial conditions $x_0$ and $\dot{x}_0$, we now have all values for $x$ and $\dot{x}$

