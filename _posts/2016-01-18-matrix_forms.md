---
layout: post
title: 02 Row Echelon form
categories: [notes, linear]
---

If the reduction process described in the previous notes yield the following matrix

$$ \left(\begin{array}{ccccc|c} 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{array}\right) $$

Then the last two equations of the reduced system will be satisfied by any 5-tuple. So the solution set of the system will be the set of all 5-tuples satisfying the following equations

$$ \begin{cases} x_1 + x_2 + x_3 + x_4 + x_5 = 1 \\ x_3 + x_4 + 2x_5 = 0 \\ x_5 = 3\end{cases}$$

The variables corresponding to the first nonzero elements in each row of the reduced matrix are called the **lead variables**. For this example, $$x_1, x_3,$$ and $$x_5$$ are the lead variables. The remaining variables are called **free variables**. The $$n$$-tuples in the solution sets of a system of linear equations will have exactly one possible value for the value in the $$n$$-tuple corresponding to each of the lead variables, and infinite possible values for the values corresponding to each of the free variables.

A matrix is said to be in **row echelon form** if

* The first nonzero entry in each nonzero row is 1.
* If row $$k$$ does not consist of entirely zeroes, the number of leading zero entries in row $$k+1$$ is greater than the number of leading zero entries in row $$k$$.
* If there are rows whose entries are all zero, they are below the rows having nonzero entries.

The process of using elementary row operations to transform a linear system into one whose augmented matrix is in row echelon form is called **Gaussian elimination**.

Note that if there is a row of the form

$$\left( \begin{array}{cccc|c} 0 & 0 & \dots & 0 & 1 \end{array}\right)$$

The system is **inconsistent**. Otherwise, the system will be consistent. If the system is consistent and the nonzero rows of the row echelon form of the matrix form a **strictly triangular** system, the system will have a unique solution.

A system is said to be **overdetermined** if there are more equations than unknowns ($$m > n$$). Overdetermined systems are *usually* inconsistent, but not always.

A system of linear equations is said to be **underdetermined** of there are fewer equations than unknowns ($$m < n$$). Although it is possible for an underdetermined system to be inconsistent, they are usually consistent with infinitely many solutions. It is *not* possible for an underdetermined system to have a unique solution.

A matrix is said to be in **reduced row echelon form** if

* The matrix is in row echelon form
* The first nonzero entry in each row is the only nonzero entry in its column

The process of using elementary row operations to transform a matrix into reduced row echelon form is called **Gauss-Jordan reduction**.

A system of linear equations is said to be **homogeneous** if the constants on the right hand side are all zero. Homogenous systems are *always* consistent. It is a trivial matter to find a solution, just let all variable equal 0. Thus, if a homogeneous system has a unique solution, it *must* be the trivial solution $$(0, 0, \dots , 0)$$, otherwise there are *infinite* solutions.

**Theorem 1.2.1:** An $$m \times n$$ homogenous solution of linear equations has a nontrivial solution if $$n > m$$.
