---
layout: post
title: 01 Systems of Linear Equations
categories: [notes, linear]
---

A **linear equation in $$n$$ unknowns** is an equation of the form

$$a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b$$

Where $$a_1, a_2, ..., a_n$$ and $$b$$ are real numbers and $$x_1, ..., x_n$$ are variables. A **linear system** of **$$m$$** equations in **$$n$$** unknowns is a system of the form

$$\begin{cases}a_{11} x_1 + a_{12} x_2 + \dots + a_{1n} x_n = b_1 \\ a_{21} x_1 + a_{22} x_2 + \dots + a_{2n} x_n = b_2 \\ \vdots \\ a_{m1} x_1 + a_{m2} x_2 +  \dots + a_{mn} x_n = b_m \end{cases}$$

Where the $$a_{ij}$$'s and the $$b_i$$'s are real numbers. We refer to systems in this form as $$m \times n$$ linear systems.

By a solution of an $$m \times n$$ system, we mean an ordered $$n$$-tuple of numbers $$(x_1, x_2, \dots , x_n)$$ that simultaneously satisfy all of the equations of the system.

If a system has no solutions, it is called **inconsistent**. If the system has at least one solution, it is called **consistent**. The set of all solutions of a linear system is called the **solution set** of the system.

Graphically, there are three cases a $$2 \times 2$$ system can be. If each linear system can be graphed as a line, the solutions represent the point of intersection of the lines. The lines can intersect exactly once (they intersect), not at all (the lines are parallel), or everywhere (the lines are parallel and on top of each other). The last case is where there are infinite solutions to a system of linear equations.

These three cases occur for all $$m \times n$$ systems. The system is either consistent or inconsistent. If it is consistent, it will have either one solution or infinite solutions.

Two systems of equations involving the same variables are said to be **equivalent** if they have the same solution set.

There are three operations that can be used on a system to obtain and equivalent system:

* The order in which any two equations are written may be interchanged
* Both sides of an equation may be multiplied by the same non-zero real number
* A multiple of one equation may be added to another.

A system is said to be in **strict triangular form** if, in the $$k$$th equation, the coefficients of the first $$k-1$$ variables are all zero and the coefficient of $$x_k$$ is nonzero $$(k = 1, \dots , n)$$.

For example, the following system is in strict triangular form.

$$\begin{cases} 3x_1 + 2x_2 + x_3 = 1 \\ x_2 - x_3 = 2 \\ 2x_3 = 4\end{cases}$$

Given a system of linear equations, we can represent the system as a matrix.

$$\begin{cases} x_1 + 2x_2 + x_3 = 3 \\ 3x_1 - x_2 - 3x_3 = -1 \\ 2x_1 + 3x_2 + x_3 = 4 \end{cases} \,\,\,\cong\,\,\, \left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 3 & -1 & -3 & -1 \\ 2 & 3 & 1 & 4 \end{array}\right)$$

If just the matrix of coefficients is given, the matrix is referred to as the **coefficient matrix** of the system. When both the coefficients and the numbers on the right hand side of the system is given, the matrix is called an **augmented matrix**. An $$m \times n$$ matrix is said to be **square** if it has the same number of row and columns, that is, if $$m = n$$.

Systems of linear equations can be solved by performing **row operations** on the system's augmented matrix. There are three such row operations that can be applied to an augmented matrix.

* Interchange two rows
* Multiply a row by a nonzero real number
* Replace a row with its sum with a multiple of another row

These operations correspond to the given operations on systems of linear equations given above.

In general, if an $$n \times n$$ linear system can be reduced to **strictly triangular form** by elementary matrix row operations, then it will have a unique solution.
