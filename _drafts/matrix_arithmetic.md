---
layout: post
title: 03 Matrix Notation and Arithmetic
categories: [notes, linear]
---

A **scalar** is any single real *or* complex number.

Matrices are usually denoted by capital letters $$A, B, C, \dots$$. In general, $$a_{ij}$$ will denote the entry in the matrix $$A$$ that is in the $$i$$th row and the $$j$$th column. Often, the entire matrix $$A$$ will be referred to as $$(A_{ij})$$.

Matrices with a single column or row are called **vectors**. They are of special interest because they can be used to represent solutions of linear systems. A solution of a system of $$m$$ linear equations and $$n$$ unknowns is an **$$n$$-tuple** of real numbers. We refer to an $$n$$-tuple as a **vector**. If a vector is represented in terms of a $$1 \times n$$ matrix, it is a **row vector**. If it is represented by a $$n \times 1$$ matrix, it is a **column vector**.

The set of all $$n \times 1$$ matrices of real numbers is called **Euclidean $$n$$-space** and is usually denoted by $$\mathbb{R}^n$$.

The standard notation for a column vector is a boldface lowercase letter.

$$\mathbf{x} = \left(\begin{array}{c} x_1 \\ x_2 \\ \vdots \\ x_n \end{array}\right)$$

Bold faced variable are hard to write by hand, so we also use $$\underline{x}$$ to mean a column vector.

The standard notation for a row vector is a boldface lowercase letter with an arrow over it.

$$\vec{\mathbf{x}} = (x_1, x_2, \dots , x_n)$$

I will dispense with boldface fonts, and use purely $$\vec{x}$$ to represent a row vector.

We can refer to the $$j$$th column of a matrix $$A$$ by $$\underline{a}_j$$, and the $$i$$th row of a matrix $$A$$ by $$\vec{a}_i$$.

Two $$m \times n$$ matrices are considered to be **equal** if they are equal element-wise, that is $$a_{ij} = b_{ij}$$ for each $$i$$ and $$j$$.

A matrix can be multiplied by a scalar element-wise. That is, if $$A$$ is an $$m \times n$$ matrix and $$\alpha$$ is a scalar, then $$\alpha A$$ is the $$m \times n$$ matrix whose $$(i, j)$$ entry is $$\alpha a_{ij}$$. Matrices can be added together element-wise if they have the same dimensions. That is, if $$A = (a_{ij})$$ and $$B = (b_{ij})$$ are both $$m \times n$$ matrices, then the **sum** $$A + B$$ is the $$m \times n$$ matrix whose $$(i, j)$$ entry is $$a_{ij} + b_{ij}$$ for each ordered pair $$(i, j)$$. Matrix subtraction can be defined by these two rules as $$A - B = A + (-1)B$$.

We refer to an all zero matrix $$\underline{\underline{0}}$$ as the **zero matrix**.

**TODO: Matrix Multiplication (dot product)** pg 30
