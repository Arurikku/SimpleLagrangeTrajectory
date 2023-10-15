# Simple Lagrange Trajectory
Provides coordinates for a particle moving along a function curve (2D or 3D) using simple Lagrangian Mechanics.\
The principle of Lagrangian Mechanics is least action, which makes it incredibly easy to find a differential equation which describes accurately our system.\
The coordinates can be used very easily in [Desmos Graph](https://www.desmos.com/calculator).

# 2D Version
The 2D version is a special case of the 3D one, so it is much easier to compute.
## Building the 2D Lagrangian
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


# 3D Version
While jumping to a whole new dimension seems difficult, one only needs to know basic partial derivatives to do this.\
## Building the 3D Lagrangian
Let $f$ be a continuous differentiable function on our desired interval.\
Let $A$ be the point representing our particle, of coordinates $(x, y, z)$. We have therefore $A = (x, y, f(x,y))$\
Let us now construct the Lagrangian of our system.\
We have the potential energy: $E_p = mgz = mgf(x,y)$.\
And the kinetic energy: $E_k = \frac{1}{2}\cdot mv^2$.\
Since we are yet again in cartesian coordinates, we have:\
$$v = \sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2}$$
$$\iff v = \sqrt{\dot{x}^2 + \dot{y}^2 +(\frac{d}{dt}f(x,y))^2}$$
$$\iff v = \sqrt{\dot{x}^2 + \dot{y}^2 +(\dot{x}\frac{\partial f}{\partial x}+\dot{y}\frac{\partial f}{\partial y})^2}$$
$$\iff v = \sqrt{\dot{x}^2(1+(\frac{\partial f}{\partial x})^2)+\dot{y}^2(1+(\frac{\partial f}{\partial y})^2) + 2\dot{x}\dot{y}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y}}$$
Hence,
$$E_k = \frac{1}{2}\cdot m(\dot{x}^2(1+(\frac{\partial f}{\partial x})^2)+\dot{y}^2(1+(\frac{\partial f}{\partial y})^2) + 2\dot{x}\dot{y}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y})$$
We now have the Lagrangian: 
$$L = \frac{1}{2}\cdot m(\dot{x}^2(1+(\frac{\partial f}{\partial x})^2)+\dot{y}^2(1+(\frac{\partial f}{\partial y})^2) + 2\dot{x}\dot{y}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y} - 2gf(x,y))$$
## Using the principle of least action
We have:
$$\frac{\partial L}{\partial \dot{x}} = m (\dot{x}(1+(\frac{\partial f}{\partial x})^2)+\dot{y}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y})$$
$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} = m(\ddot{x}(1+(\frac{\partial f}{\partial x})^2)+2\dot{x}\frac{\partial f}{\partial x}(\dot{x}\frac{\partial^2 f}{\partial x^2}+\dot{y}\frac{\partial^2 f}{\partial x \partial y})+\ddot{y}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y}+\dot{y}\frac{\partial^2 f}{\partial x \partial y}(\dot{y}\frac{\partial f}{\partial y}\dot{x}\frac{\partial f}{\partial x})+\dot{y}(\dot{x}\frac{\partial f}{\partial y}\frac{\partial^2 f}{\partial x^2}+\dot{y}\frac{\partial f}{\partial x}\frac{\partial^2 f}{\partial y^2}))$$
$$\frac{\partial L}{\partial x} = m(\dot{x}^2\frac{\partial^2 f}{\partial x^2}\frac{\partial f}{\partial x}+\frac{1}{2}\dot{y}^2\frac{\partial^2 f}{\partial x \partial y}+\dot{x}\dot{y}(\frac{\partial^2 f}{\partial x^2}\frac{\partial f}{\partial y}+\frac{\partial f}{\partial^2 x \partial y}\frac{\partial f}{\partial x})-g\frac{\partial f}{\partial x})$$

Applying the principle of least action gives in the end:
$$\ddot{x}(1+(\frac{\partial f}{\partial x})^2)+\ddot{y}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y} = \dot{x}^2\frac{\partial^2 f}{\partial x^2}\frac{\partial f}{\partial x}+\frac{1}{2}\dot{y}^2\frac{\partial^2 f}{\partial x \partial y}+\dot{x}\dot{y}(\frac{\partial^2 f}{\partial x^2}\frac{\partial f}{\partial y}+\frac{\partial f}{\partial^2 x \partial y}\frac{\partial f}{\partial x})-g\frac{\partial f}{\partial x} -2\dot{x}\frac{\partial f}{\partial x}(\dot{x}\frac{\partial^2 f}{\partial x^2}+\dot{y}\frac{\partial^2 f}{\partial x \partial y}) - \dot{y}\frac{\partial^2 f}{\partial x \partial y}(\dot{y}\frac{\partial f}{\partial y}\dot{x}\frac{\partial f}{\partial x})-\dot{y}(\dot{x}\frac{\partial f}{\partial y}\frac{\partial^2 f}{\partial x^2}+\dot{y}\frac{\partial f}{\partial x}\frac{\partial^2 f}{\partial y^2})$$

However, we want $\ddot{x}$ independant of $\ddot{y}$, so we apply the principle of least action again, but with respect to $y$ and $\dot{y}$.\
There is no need to go through the same calculations, as the equations are very clearly symmetrical, so we have in the end:
$$\ddot{y}(1+(\frac{\partial f}{\partial y})^2)+\ddot{x}\frac{\partial f}{\partial x}\frac{\partial f}{\partial y} = \dot{y}^2\frac{\partial^2 f}{\partial y^2}\frac{\partial f}{\partial y}+\frac{1}{2}\dot{x}^2\frac{\partial^2 f}{\partial x \partial y}+\dot{x}\dot{y}(\frac{\partial^2 f}{\partial y^2}\frac{\partial f}{\partial x}+\frac{\partial f}{\partial^2 x \partial y}\frac{\partial f}{\partial y})-g\frac{\partial f}{\partial y} -2\dot{y}\frac{\partial f}{\partial y}(\dot{y}\frac{\partial^2 f}{\partial y^2}+\dot{x}\frac{\partial^2 f}{\partial x \partial y}) - \dot{x}\frac{\partial^2 f}{\partial x \partial y}(\dot{x}\frac{\partial f}{\partial x}\dot{y}\frac{\partial f}{\partial y})-\dot{x}(\dot{y}\frac{\partial f}{\partial x}\frac{\partial^2 f}{\partial y^2}+\dot{x}\frac{\partial f}{\partial y}\frac{\partial^2 f}{\partial x^2})$$

We now have a system of the form:
```math
\begin{cases}
\kappa\ddot{x} + \lambda\ddot{y} = \alpha\\
\mu\ddot{y} + \lambda\ddot{x} = \beta
\end{cases}
```
yielding the solutions:
$$\ddot{x} = \frac{\alpha\lambda-\beta\kappa}{\lambda^2-\kappa\mu}$$
$$\ddot{y} = \frac{\beta\lambda-\alpha\mu}{\lambda^2-\kappa\mu}$$
## Translating to python
The method is exactly the same as in 2D, but with an extra $y$ and $\dot{y}$:
```math
U_i = \begin{pmatrix} x_i \\ \dot{x}_i \\ y_i \\ \dot{y}_i \end{pmatrix}
```
```math
\dot{U}_i = \begin{pmatrix} \dot{x}_i \\ \ddot{x}_i \\ \dot{y}_i \\ \ddot{y}_i \end{pmatrix}
```
We again write $\dot{U}_i$ as:
```math
\dot{U}_i = \frac{U_{i+1}-U_i}{dt}
```
giving the same recurrence relation as before:
$$U_{i+1} = dt \cdot \dot{U}_i + U_i$$

Using the initial conditions $x_0$, $\dot{x}_0$, $y_0$, $\dot{y}_0$, we will again all values for $x$, $\dot{x}$, $y$, $\dot{y}$
