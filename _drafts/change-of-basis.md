---
layout: post
title: Change of Basis
meta: Describes what a basis is, and how to change from one vector space to another using a transition matrix. Pays special attention to rotation matrices.
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

One of the things I knew well enough to pass an exam on, but not well enough to actually understand what it meant was the concept of changing basis in linear algebra. This is an attempt to remedy that.

A **basis** for a vector space $$V$$ of dimension $$n$$ is a sequence of $$n$$ vectors $$(v_1, v_2, \dots, v_n)$$ such that all vectors in $$V$$ can be uniquely expressed as linear combinations of the basis vectors. Often calculations in one basis can be simplified if we change our basis to something else.

For example, if we wish to work with a vector $$\vec v$$ with respect to the standard basis vectors $$\vec x = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$, $$\vec y = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$$ and $$\vec z = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$, we know how to do that. Here's a graph of some random vector $$\vec v$$.

<img class="centered" src="{{ "/assets/posts/change-of-basis/standard-basis.svg" | prepend: site.baseurl }}" alt="vector v wrt the standard basis">

What if we want to rotate our coordinate system by some [Euler angles](https://en.wikipedia.org/wiki/Euler_angles) $$\alpha$$, $$\beta$$, and $$\gamma$$? This is what changing the basis really is. To rotate a vector $$\vec v$$ given some Euler angles, multiply $$\vec v$$ by the following transition matrix $$P$$ taken from the $$Z_1 Y_2 X_3$$ entry of [this](https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix) table. [Source](http://tex.stackexchange.com/questions/67573/tikz-shift-and-rotate-in-3d).

$$P = \begin{pmatrix}
    \cos \alpha \cos \beta & \cos \alpha \sin \beta \sin \gamma - \sin \alpha \cos \gamma & \cos \alpha \sin \beta \cos \gamma + \sin \alpha \sin \gamma \\
    \sin \alpha \cos \beta & \sin \alpha \sin \beta \sin \gamma + \cos \alpha \cos \gamma & \sin \alpha \sin \beta \cos \gamma - \cos \alpha \sin \gamma \\
    - \sin \beta & \cos \beta \sin \gamma & \cos \beta \cos \gamma
\end{pmatrix}$$

With the Euler angles from the following diagram:

<img class="centered" src="https://upload.wikimedia.org/wikipedia/commons/a/a1/Eulerangles.svg" alt="Euler angles">

We get a new vector $$v' = P v$$ that, with respect to the new coordinate system, is the same as $$\vec v$$.

<img class="centered" src="{{ "/assets/posts/change-of-basis/new-basis.svg" | prepend: site.baseurl }}" alt="vector v' wrt the new rotated basis">

In the first image, $$\vec x$$, $$\vec y$$, and $$\vec z$$ form the basis for the vector space. In the second image, $$\vec{x'}$$, $$\vec{y'}$$, and $$\vec{z'}$$ form the basis for the new, rotated, vector space.

### In general

To convert a vector $$\vec v$$ w.r.t. the standard basis to a vector $$\vec{v'}$$ w.r.t. a new basis $$\{\vec{u_1}, \vec{u_2}, \dots, \vec{u_n}\}$$ we multiply $$\vec v$$ by the matrix $$U$$ formed by $$U = (\vec{u_1}, \vec{u_2}, \dots, \vec{u_n})$$. That is,

$$\vec{v'} = U \cdot \vec v$$

---

To convert a vector $$\vec v$$ w.r.t. a basis $$\{\vec{u_1}, \vec{u_2}, \dots, \vec{u_n}\}$$ to the standard basis, we multiply $$\vec v$$ by the matrix $$U^{-1}$$. That is,

$$\vec{v'} = U^{-1} \cdot \vec v$$

---

In general, to convert a vector $$\vec v$$ w.r.t. a basis $$V$$ to a vector $$\vec{v'}$$ in a basis $$U$$ formed by $$U = (\vec{u_1}, \vec{u_2}, \dots, \vec{u_n})$$ and $$V = (\vec{v_1}, \vec{v_2}, \dots, \vec{v_n})$$, we multiply $$\vec v$$ by the **transition matrix** $$U^{-1} V$$. That is,

$$\vec{v'} = U^{-1} V \cdot \vec v$$

---

In particular, we can use [rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix) as transition matrices to rotate our basis by some angle(s). The real trick is to find an appropriate transition matrix, the actual change of basis isn't too bad.
