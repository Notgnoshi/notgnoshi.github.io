---
layout: post
title: 02 More about ODEs
categories: [notes, diff]
---

*Observation:* A function $$y(x)$$ containing parameters $$c_1, c_2, ...$$ is the **general solution** of a linear differential equation if it has two properties:

* Every choice of constants produces a solution
* Every solution can be obtained by an appropriate choice of constants

*Observation:* An $$n$$th order differential equations has $$n$$ terms in its general solution.

Given **initial values** for a differential equation, it is possible to find the values of the constants, giving what is called the **particular solution**.

#### Separable Differential Equations:

Given a differential equation $$\frac{dy}{dx} - \frac{x^2 + 3}{y} = 0$$, the solution can be found by separating the $$x$$ and $$y$$ terms and their derivatives as follows.

$$ \frac{dy}{dx} = \frac{x^2 + 3}{y} $$

$$ y\,dy  = (x^2 + 3) \,dx $$

$$ \int{y\,dy} = \int{(x^2 + 3)\,dx} $$

$$ \frac{1}{2}y^2 + C_1 = \frac{1}{3}x^3 + 3x + C_2 $$

$$ \frac{1}{2}y^2 = \frac{1}{3}x^3 + 3x + C_0 $$

$$ y = \pm \sqrt{ \frac{2x^3}{3} + 6x + 2C_0 } $$

$$ y = \pm \sqrt{ \frac{2x^3}{3} + 6x + C } $$

Note that **derivatives are not fractions** and *should not be broken up like they are fractions* but we are because it is convenient.
