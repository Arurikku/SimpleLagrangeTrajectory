# Simple Lagrange Trajectory
Provides coordinates for a particle moving along a function curve (2D, 3D or even N dimension) using simple Lagrangian Mechanics.\
The principle of Lagrangian Mechanics is least action, which makes it incredibly easy to find a differential equation which accurately describes our system.\
The coordinates can be used very easily in the [2D Desmos Graphing Calculator](https://www.desmos.com/calculator) and the [3D Desmos Graphing Calculator](https://www.desmos.com/3d).

# 2D Version
The 2D version is a special case of the 3D one, so it is much easier to compute.
## Building the 2D Lagrangian
Let $f$ be a continuous differentiable (not actually needed) function on our desired interval.\
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

Using the initial conditions $x_0$ and $\dot{x}_0$, we now have all values for $x$ and $\dot{x}$\
Here is an example:\
![sin_friction](https://github.com/Arurikku/SimpleLagrangeTrajectory/assets/61802068/fcf62808-9235-48d1-8bbe-f79664733920)

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

Using the initial conditions $x_0$, $\dot{x}_0$, $y_0$, $\dot{y}_0$, we will again have all values for $x$, $\dot{x}$, $y$, $\dot{y}$\
Here is an example:\
![3D_half_pipe_friction](https://github.com/Arurikku/SimpleLagrangeTrajectory/assets/61802068/779e7e92-215c-429d-83ae-9b57307d7fa7)

# Usage with Desmos
After entering all the necesseray information in the python script, the console will print a list of the coordinates taken by the point.\
You can check out [this Desmos example](https://www.desmos.com/calculator/jnyqaxwpyq) for how to graph the 2D version.\
And [this example](https://www.desmos.com/3d/b1bd241470) for how to graph the 3D version.

You can edit the script to print out the values for the absolute speed of the particle, and using some simple colours you can graph some nice visuals like this:\
![colourHSV_test](https://github.com/Arurikku/SimpleLagrangeTrajectory/assets/61802068/fc06d799-58fc-49bd-b124-74c89cd7e40a)


# N Dimensions Version
As per usual in science, let's generalise even if what we're describing makes no sense physically.\
After 2D comes 3D, and after that comes the absurdity of N dimensions.\
## Notation:
We place ourselves in an N dimension cartesian coordinate system, meaning our point $A$ is now $A = (a_0, a_1, a_2, \ldots, a_{n+1})$ with $a_{n+1}$ the "height" of our point.\
/!\ Note that this means our system is actually in (n+1) dimensions, as $a_{n+1} = f(a_0, a_1, a_2, \ldots, a_n)$.\
We write $\overrightarrow{r} = (a_0, a_1, a_2, \ldots, a_n)$ so that we can write compactly:\
$$f(a_0, a_1, a_2, \ldots, a_n) = f(\overrightarrow{r})$$\
We also write the graident of $f$ as $\nabla f$ where:
```math
\nabla f=\begin{bmatrix} \frac{\partial f}{\partial a_0} \\ \frac{\partial f}{\partial a_1} \ \ \\ \vdots \\ \frac{\partial f}{\partial a_n} \end{bmatrix}
```
## Reminder:
We need to keep in mind the following result:\
$$\frac{d}{dt}f = \nabla f \cdot \overrightarrow{\dot{r}} = \sum_{k=0}^{n} \dot{a_k} \frac{\partial f}{\partial a_k}$$

## Building the Lagrangian
We have the potential energy: $E_p = mgf(\overrightarrow{r})$.\
And the kinetic energy: $E_k = \frac{1}{2}\cdot mv^2$.\
Since we are still in cartesian coordinates, we have:
$$v^2 = \dot{a_0}^2 + \dot{a_1}^2 + \ldots + \dot{a_{n+1}}^2)$$
$$\iff v^2 = \dot{a_0}^2 + \dot{a_1}^2 + \ldots + \dot{a_{n}}^2 + \bigl(\frac{d}{dt} f(\overrightarrow{r})\bigr)^2$$
$$\iff v^2 = \sum_{k=0}^{n} \dot{a_{k}}^2 + \Bigl(\sum_{k=0}^{n} \dot{a_k} \frac{\partial f}{\partial a_k}\Bigr)^2$$
Hence,
$$L = \frac{1}{2} m \Bigl(\sum_{k=0}^{n} \dot{a_{k}}^2 + \Bigl(\sum_{k=0}^{n} \dot{a_k} \frac{\partial f}{\partial a_k}\Bigr)^2\Bigr) - mgf(\overrightarrow{r})$$
## Using the principle of least action
In the end, we know that we will need to derive with respect to each coordinate to be able to get our final result, so let's just do the general case.\
Let $w \in ⟦0, n ⟧$ 
$$\frac{\partial L}{\partial \dot{a_w}} = m\Bigl(\dot{a_w} + \frac{\partial f}{\partial a_w}\sum_{k=0}^{n} \dot{a_k} \frac{\partial f}{\partial a_k}\Bigr)$$
$$\frac{d}{dt}\Bigl(\frac{\partial L}{\partial \dot{a_w}}\Bigr) = m\Bigl(\ddot{a_w}+\sum_{k=0}^n\sum_{j=0}^n\dot{a_k}\dot{a_j}\frac{\partial f}{\partial a_j}\frac{\partial^2 f}{\partial a_w \partial a_k} + \frac{\partial f}{\partial a_w}\sum_{k=0}^n\ddot{a_k}\frac{\partial f}{\partial a_k}+\frac{\partial f}{\partial a_w}\sum_{k=0}^n\sum_{j=0}^n\dot{a_k}\dot{a_j}\frac{\partial^2 f}{\partial a_k \partial a_j}\Bigr)$$
$$\frac{\partial L}{\partial a_w} = m\Bigl(\dot{a_w}\frac{\partial^2 f}{\partial a_w^2}\sum_{k=0}^n\ddot{a_k}\frac{\partial f}{\partial a_k} - g\frac{\partial f}{\partial a_w}\Bigr)$$
We apply the principle of least action, giving us:\
$$\ddot{a_w}+\sum_{k=0}^n\sum_{j=0}^n\dot{a_k}\dot{a_j}\frac{\partial f}{\partial a_j}\frac{\partial^2 f}{\partial a_w \partial a_k} + \frac{\partial f}{\partial a_w}\sum_{k=0}^n\ddot{a_k}\frac{\partial f}{\partial a_k}+\frac{\partial f}{\partial a_w}\sum_{k=0}^n\sum_{j=0}^n\dot{a_k}\dot{a_j}\frac{\partial^2 f}{\partial a_k \partial a_j} = \dot{a_w}\frac{\partial^2 f}{\partial a_w^2}\sum_{k=0}^n\ddot{a_k}\frac{\partial f}{\partial a_k} - g\frac{\partial f}{\partial a_w}$$
To simplify the writing, we'll package every term that doesn't depend on a second order time derivative into one big constant $C_w$:\
$$C_w = \dot{a_w}\frac{\partial^2 f}{\partial a_w^2}\sum_{k=0}^n\ddot{a_k}\frac{\partial f}{\partial a_k} - g\frac{\partial f}{\partial a_w} - \sum_{k=0}^n\sum_{j=0}^n\dot{a_k}\dot{a_j}\frac{\partial f}{\partial a_j}\frac{\partial^2 f}{\partial a_w \partial a_k} - \frac{\partial f}{\partial a_w}\sum_{k=0}^n\sum_{j=0}^n\dot{a_k}\dot{a_j}\frac{\partial^2 f}{\partial a_k \partial a_j}$$
We need to rewrite this with all of the $\ddot{a_w}$ terms together to rewrite this as a nice system of equations, which gives us:\
$$\ddot{a_w}\Bigl(1+\Bigl(\frac{\partial f}{\partial a_w}\Bigr)^2\Bigr) + \frac{\partial f}{\partial a_w}\sum_{{k=0} \atop{k \neq w}}^n\ddot{a_k}\frac{\partial f}{\partial a_k} = C_w$$
We now package more terms into constants:\
$$\lambda_w = \Bigl(1+\Bigl(\frac{\partial f}{\partial a_w}\Bigr)^2\Bigr) \ , \ H_k = \ddot{a_k}\frac{\partial f}{\partial a_k}$$
Leaving us with\
$$\forall w \in ⟦0, n ⟧, \ \lambda_w\ddot{a_w} + \frac{\partial f}{\partial a_w}\sum_{{k=0} \atop{k \neq w}}^n H_k = C_w$$
We now have the system of equations:
```math
\begin{cases}
\lambda_0\ddot{a_0} + \frac{\partial f}{\partial a_0}H_1 + \frac{\partial f}{\partial a_0}H_2 + \ldots + \frac{\partial f}{\partial a_0}H_n = C_0 \\
\lambda_1\ddot{a_1} + \frac{\partial f}{\partial a_1}H_0 + \frac{\partial f}{\partial a_1}H_1 + \ldots + \frac{\partial f}{\partial a_1}H_n = C_1 \\
\vdots \\
\lambda_n\ddot{a_n} + \frac{\partial f}{\partial a_n}H_0 + \frac{\partial f}{\partial a_n}H_1 + \ldots + \frac{\partial f}{\partial a_{n}}H_{n-1} = C_n \\
\end{cases}
```
Which can be rewritten with matrices:
```math
\begin{pmatrix}
\lambda_0 \ \ \frac{\partial f}{\partial a_0}\frac{\partial f}{\partial a_1} \ \ \frac{\partial f}{\partial a_0}\frac{\partial f}{\partial a_2} \ \ \ldots \ \ \frac{\partial f}{\partial a_0}\frac{\partial f}{\partial a_n} \\
\frac{\partial f}{\partial a_1}\frac{\partial f}{\partial a_0} \ \ \lambda_1 \ \ \frac{\partial f}{\partial a_1}\frac{\partial f}{\partial a_2} \ \ \ldots \ \ \frac{\partial f}{\partial a_1}\frac{\partial f}{\partial a_n} \\
\vdots \\
\frac{\partial f}{\partial a_n}\frac{\partial f}{\partial a_0} \ \ \frac{\partial f}{\partial a_n}\frac{\partial f}{\partial a_1} \ \ \frac{\partial f}{\partial a_n}\frac{\partial f}{\partial a_2} \ \ \ldots \ \ \lambda_n
\end{pmatrix}  \begin{pmatrix}\ddot{a_0} \\ \ddot{a_1} \\ \vdots \\ \ddot{a_n} \end{pmatrix} = \begin{pmatrix}C_0 \\ C_1 \\ \vdots \\ C_n \end{pmatrix}
```
All in all, we end up with:
```math
\begin{pmatrix}\ddot{a_0} \\ \ddot{a_1} \\ \vdots \\ \ddot{a_n} \end{pmatrix} = \begin{pmatrix}
\lambda_0 \ \ \frac{\partial f}{\partial a_0}\frac{\partial f}{\partial a_1} \ \ \frac{\partial f}{\partial a_0}\frac{\partial f}{\partial a_2} \ \ \ldots \ \ \frac{\partial f}{\partial a_0}\frac{\partial f}{\partial a_n} \\
\frac{\partial f}{\partial a_1}\frac{\partial f}{\partial a_0} \ \ \lambda_1 \ \ \frac{\partial f}{\partial a_1}\frac{\partial f}{\partial a_2} \ \ \ldots \ \ \frac{\partial f}{\partial a_1}\frac{\partial f}{\partial a_n} \\
\vdots \\
\frac{\partial f}{\partial a_n}\frac{\partial f}{\partial a_0} \ \ \frac{\partial f}{\partial a_n}\frac{\partial f}{\partial a_1} \ \ \frac{\partial f}{\partial a_n}\frac{\partial f}{\partial a_2} \ \ \ldots \ \ \lambda_n
\end{pmatrix}^{-1} \begin{pmatrix}C_0 \\ C_1 \\ \vdots \\ C_n \end{pmatrix}
```
This is the same form as the 2D and 3D results, so it is very easy to input into the program. However, note that you need to specify eevry possible combination of mixed partial derivatives. The program expects an order like so:\
$$\frac{\partial^2 f}{\partial a_0^2} \ , \  \frac{\partial^2 f}{\partial a_0 \partial a_1} \ , \ \frac{\partial^2 f}{\partial a_0 \partial a_2} \ , \ldots \ , \frac{\partial^2 f}{\partial a_1 \partial a_0} \ , \ \frac{\partial^2 f}{\partial a_1^2} \ , \ \frac{\partial^2 f}{\partial a_1 \partial a_2} \ , \ldots \  , \frac{\partial^2 f}{\partial a_n^2}$$
Yes some terms are redundant, but it helps for the program's simplicity and is much easier to understand.
