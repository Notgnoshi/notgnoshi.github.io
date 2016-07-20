---
layout: post
title: Norms
---
<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

The norm of a mathematical object is a quantity that in some way describes the size, length, magnitude, or some other metric of the object. I will describe norms in terms of real or complex numbers, vectors, matrices, and polynomials.

### Definition

A **norm** on a vector space $$V$$ is a function $$p: V \to \mathbb{R}$$ with the following properties for all $$z \in \mathbb{C}$$ and all $$\vec u, \vec v \in V$$

1. $$p(z \vec v) = \mid z \mid p(\vec v)$$ (absolute scalability)
2. $$p(\vec u + \vec v) \leq p(\vec u) + p(\vec v)$$ (triangle inequality)
3. If $$p(\vec v) = 0$$ then $$\vec v$$ is the zero vector in $$V$$

We usually denote the norm $$p: V \to \mathbb{R}$$ on a vector $$\vec v$$ by enclosing it in double lines $$\Vert \vec v \Vert = p(\vec v)$$. On vectors in Euclidean space, it is also common to use single lines $$\vert \vec v \vert$$.

The most common norm is the **absolute value** of a real or complex number. For a real number $$x$$, the absolute value is defined as

$$\vert x \vert = x \operatorname{sgn}(x) = \begin{cases}-x & \text{ for } x \leq 0 \\ x & \text{ for } x \geq 0\end{cases}$$

where $$\operatorname{sgn}(x)$$ is the sign function that returns the sign of $$x$$. The absolute value of a complex number $$z = a + bi$$, also called the complex modulus, is defined as

$$\vert z \vert = \sqrt{a^2 + b^2}$$

### Vector norms

Given some vector $$\vec v$$, how might we go about describing its magnitude? A completely natural description might be the vector's length. We know from high school mathematics that the length of a vector is the sum of the squares of its elements. This is the **Euclidean norm**, often simply referred to as "the norm" of a vector. However, this isn't the only way we have of describing a vector's magnitude. The most useful norms (aside from the Euclidean norm) are **$$p$$-norms** given by the following formula for some set $$p$$

$$\Vert \vec v \Vert_p = \left( \sum_i \vert v_i \vert^p \right)^{\frac{1}{p}}$$

Note that for $$p=2$$, this *is* the Euclidean norm, or the **$$2$$-norm**. Other common $$p$$-norms are the **$$1$$-norm**

$$\Vert \vec v \Vert_1 = \sum_i \vert v_i \vert$$

and the **$$\infty$$-norm**

$$\Vert \vec v \Vert_\infty = \max_i \vert v_i \vert$$

The $$1$$-norm is often called the **taxicab norm** because in $$\mathbb{R}^2$$, if we call the destination of a taxi the tip of a vector, then the $$1$$-norm is the distance the taxi must drive, as long as the streets are rectangular.

### Matrix norms

We can also take norms of matrices. The $$p$$-norm of a matrix $$A$$ and a real number $$1 \leq p \leq \infty$$ is defined as

$$\Vert A \Vert_p = \max_{\vec x \text{ s.t. } \Vert \vec x \Vert_p = 1} \Vert A \vec x \Vert_p$$

where $$\Vert \vec x \Vert_p$$ is a vector norm. Common matrix norms are the $$1$$, $$2$$, $$\infty$$, and "Frobenius" norms.

The **$$1$$-norm**, also called the **"maximum absolute column sum norm"** is defined as

$$\Vert A \Vert_1 = \max_j \sum_{i = 1}^{n} \vert a_{ij} \vert$$

where $$n$$ is the width of the matrix $$A$$. The **$$2$$-norm**, also called the **spectral norm** is defined as

$$\Vert A \Vert_2 = \sqrt{\text{maximum eigenvalue of } A^H A} = \max_{\Vert \vec x \Vert_2 \neq 0} \frac{\Vert A \vec x \Vert_2}{\Vert \vec x \Vert_2}$$

where $$A^H$$ is the *conjugate transpose* of $$A$$, that is, $$A^H = \overline{A}^T$$ where $$\overline{A}$$ denotes the conjugate matrix of $$A$$, with all elements $$A_{ij}$$ replaced with their complex conjugate. The spectral norm is often called "the" matrix norm.

The **$$\infty$$ norm**, also called the **"maximum absolute row sum norm"** is defined as

$$\Vert A \Vert_\infty = \max_i \sum_{j = 1}^{n} \vert a_{ij} \vert$$

where $$n$$ is the height of the matrix $$A$$.

The $$1$$, $$2$$, and $$\infty$$ matrix norms satisfy the following inequality.

$$\Vert A \Vert_{2}^{2} \leq \Vert A \Vert_1 \Vert A \Vert_\infty$$

There's one more common matrix norm, the **Frobenius norm**. The Frobenius norm of an $$m \times n$$ matrix $$A$$ is defined as

$$\Vert A \Vert_F = \sqrt{ \sum_{i=1}^{m} \sum_{j=1}^{n} \vert a_{ij} \vert^2}$$

intuition-wise, the Frobenius norm is the square root of the sum of the squares of its elements. The Frobenius norm is sometimes also called the Euclidean norm for this reason. It is also equal to the square root of the trace of $$A A^H$$, where $$A^H$$ is the conjugate transpose of $$A$$ as above.

$$\Vert A \Vert_F = \sqrt{\operatorname{tr}(A A^H)}$$

### Polynomial norms

For a polynomial $$P = \sum_{k = 0}^{n} a_k z^k$$, the **$$\ell_p$$-norm** is defined as

$$\Vert P \Vert_p = \left( \sum_{k = 0}^{n} \vert a_k \vert^p \right)^{\frac{1}{p}}$$

for $$p \geq 1$$ with special cases $$p = 1, 2, \text{ and } \infty$$. We have the **$$1$$-norm** defined as

$$\Vert P \Vert_1 = \sum_j \vert a_k \vert$$

The **$$2$$-norm** defined as

$$\Vert P \Vert_2 = \sqrt{\sum_k \vert a_k \vert^2}$$

and the **$$\infty$$-norm** defined as

$$\Vert P \Vert_\infty = \max_k \vert a_k \vert$$

We also have **$$L^p$$-norms** defined by

$$\Vert P \Vert_{L_p} = \left[ \int_{0}^{2 \pi} \left\vert P ( e^{i \theta}) \right\vert^p \frac{d \theta}{2 \pi} \right] ^{\frac{1}{p}}$$

for $$p \geq 1$$ with special cases $$p = 1, 2, \text{ and } \infty$$. We have the **$$1$$-norm** defined as

$$\Vert P \Vert_{L^1} = \int_{0}^{2 \pi} \left\vert P ( e^{i \theta}) \right\vert \frac{d \theta}{2 \pi}$$

the **$$2$$-norm** defined as

$$\Vert P \Vert_{L^2} = \sqrt{\int_{0}^{2 \pi} \left\vert P ( e^{i \theta}) \right\vert^2 \frac{d \theta}{2 \pi}}$$

and the **$$\infty$$-norm** defined as

$$\Vert P \Vert_{L^\infty} = \sup_{\vert z \vert = 1} \left\vert P(z) \right\vert$$

where $$\sup$$ represents the **supremum** of a subset $$S$$ of a partially ordered set $$T$$ is the least element in $$T$$ that is greater than or equal to all the elements of $$S$$. The supremum is also called the **least upper bound**.

There are also **Bombieri $$p$$-norms** of polynomials, defined as

$$[P]_p = \left[\sum_{i = 0}^{n} \binom {n}{i}^{1-p} \vert a_i \vert^p\right]^\frac{1}{p}$$

An important feature of Bombieri norms is that given polynomials $$R$$ and $$S$$ such that $$RS = Q$$, then the following inequality holds

$$[R]_2 [S]_2 \leq \sqrt{\binom {n}{m}} [Q]_2$$

where $$n$$ is the degree of $$Q$$ and $$m$$ is the degree of either $$R$$ or $$S$$.
