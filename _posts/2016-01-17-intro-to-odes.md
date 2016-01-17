---
layout: post
title: 01 ODEs
categories: [notes, diff]
---

A **differential equation** is an equation that relates a function to its derivatives. **ODE**s are differential equations in one **dependent** variable.

The **order** of a DE (differential equation) is the highest derivative that occurs in that DE. For example, the order of $$y'' - y' + 6y = 0$$ is 2.

A **linear** DE is one that can be put in the form $$a_n(x)y^{(N)} + a_{n-1}(x)y^{(n-1)} + ... + a_0(x)y = f(x)$$ where $$a(x)$$ is some arbitrary function of $$x$$. Any differential equation that cannot be put into this form is **nonlinear**.

For **linear** differential equations we can usually answer the following questions.

* Does the DE have a solution?
* Is the solution unique?
* How do you find the solution?

The answers to these questions are much harder to find for **nonlinear** differential equations.

A **solution** of a differential equation is a function that makes the DE true. For this example, show that $$y = e^{2x}$$ (picked via magic) is a solution to the differential equation $$y'' + y' - 6y = 0$$.

$$y = e^{2x}$$

$$y' = 2e^{2x}$$

$$y'' = 4e^{2x}$$

$$4e^{2x} + 2e^{2x} - 6e^{2x} = 0$$

Using the same ideas as above, we can show that $$y = e^{2x} + 7$$ is not a solution, and that $$y = 7e^{2x}$$ *is* a solution. It turns out that $$y = Ce^{2x}$$ is a solution for all real constant multiples $$C$$. $$y = Ce^{-3x}$$ can also be shown to be a solution. These two solutions are typically referred to as $$y_1$$ and $$y_2$$, with the **general** solution to $$y'' + y' - 6y = 0$$ being $$y = C_1 y_1 + C_2 y_2$$.
