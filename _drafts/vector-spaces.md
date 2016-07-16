---
layout: post
title: Vector Spaces
---

I'd like to do a little Linear Algebra review to make sure I understand many of the concepts before I go back to school this fall. I'll start with the idea of a *vector space*

---

A **vector space** consists of a set $$V$$ along with two operations '$$+$$' and '$$\cdot$$' defined on $$V$$ subject to the following conditions for all elements of $$V$$ (called *vectors*) $$\bar v, \bar w, \bar u \in V$$ and all *scalars* $$r, s \in \mathbb{R}$$:

1. The set $$V$$ is *closed* under vector addition. That is, $$\bar v + \bar w \in V$$
2. The set $$V$$ is closed under scalar multiplication. That is, $$r \cdot \bar v \in V$$
3. Vector addition is commutative, $$\bar v + \bar w = \bar w + \bar v$$
4. Vector addition is associative, $$(\bar v + \bar w) + \bar u = \bar v + (\bar w + \bar u)$$
5. There exists a *zero vector* $$\bar 0 \in V$$ such that $$\bar v + \bar 0 = \bar v$$ for all $$\bar v \in V$$. This element is called the *additive identity*, or the neutral element of $$V$$ under vector addition
6. There exists an *additive inverse* $$\bar w \in V$$ for every $$\bar v \in V$$ such that $$\bar w + \bar v = \bar 0$$
7. Scalar addition is *distributive* over scalar multiplication, $$(r + s) \cdot \bar v = r \cdot \bar v + s \cdot \bar v$$
8. Scalar multiplication is distributive over vector addition, $$r \cdot ( \bar v + \bar w ) = r \cdot \bar v + r \cdot \bar w$$
9. Ordinary multiplication of scalars is *associative* with scalar multiplication of vectors, $$(rs) \cdot \bar v = r \cdot (s \cdot \bar v)$$
10. Multiplication by the scalar $$1$$ (not the identity element $$I$$ or $$e$$) is the identity operation, $$1 \cdot \bar v = \bar v$$

---

Note that these vector elements of $$V$$ have not been defined. They could be the normal column vectors we're used to like $$\bar x = \left(\begin{array}{c} x_1 \\ x_2 \\ x_3 \end{array}\right)$$, matrices, polynomials, sinusoids, kittens, etc. They could be anything as long as they obey the above rules. Note also that we can redefine the operations $$+$$ and $$\cdot$$ to be whatever we want, and as long as the space still obeys the above rules, it forms a vector space. However, there are still normal scalar addition and multiplication involved, like in the left hand sides of conditions $$7$$ and $$9$$.

There are three additional properties that follow from the definition of a vector space:

1. $$0 \cdot \bar x = \bar 0$$.
2. $$(-1) \cdot \bar v = - \bar v$$ or, equivalently $$- \bar v + \bar v = \bar 0$$.
3. $$r \cdot \bar 0 = \bar 0$$.

In my linear algebra course, the third property was $$\bar x + \bar y \Rightarrow \bar y = - \bar x$$.

---

If a set $$V$$ is a vector space, and we show $$S \subset V$$ is closed under addition and multiplication, we show that $$S$$ is in itself a vector space, called a **subspace** of $$V$$. Every subspace $$S$$ of a vector space $$V$$ must contain the same zero element as $$V$$ and be defined with the same operations $$+$$ and $$\cdot$$ as $$V$$. The subspace is said to **inherit** the operations.

For a nonempty subset $$S$$ of a vector space $$V$$, under the inherited operations of $$V$$ the following are equivalent statements

1. $$S$$ is a subspace of $$V$$
2. $$S$$ is closed under linear combinations of pairs of vectors: for any vectors $$\bar s_1, \bar s_2 \in S$$ and scalars $$r_1, r_2$$, the vectors $$r_1 \bar s_1 + r_2 \bar s_2$$ is in $$S$$
3. $$S$$ is closed under linear combinations of any number of vectors: for any vectors $$\bar s_1, \dots, \bar s_n \in S$$ and scalars $$r_1, \dots, r_n$$ the vector $$r_1 \bar s_1 + \dots + r_n \bar s_n$$ is in $$S$$

---

### Miscellaneous properties and definitions

The **span** of a subspace $$S$$ is the set of all linear combinations of vectors from $$S$$. That is

$$\operatorname{span}(S) = \{ c_1 \bar s_1 + \dots + c_n \bar s_n | c_1, \dots, c_n \in \mathbb{R} \text{ and } \bar s_1, \dots, \bar s_n \in S\}$$

---

In any vector space, the span of any subset is a subspace.

---

If $$V$$ is a vector space and $$\operatorname{span}(v_1, \dots, v_n) = V$$, then $$\{v_1, \dots, v_n \}$$ is called the **spanning set** of $$V$$.

---

Let $$\operatorname{N}(A)$$ denote the set of all solutions to the system $$A \bar x = \bar 0$$.

$$\operatorname{N}(A) = \{\bar x \in \mathbb{R}^n | A \bar x = \bar 0\}$$

$$\operatorname{N}(A)$$ is called the **nullspace** of the matrix $$A$$.

---

If $$A \bar x = \bar b$$ is consistent, and $$\bar x$$ is a particular solution and $$\bar y = \bar x + \bar z$$, then $$\bar y$$ is a solution if and only if $$\bar z \in \operatorname{N}(A)$$.

---

$$\bar v_1, \dots \bar v_n$$ are **linearly independent** if $$c_1 \bar v_1 + \dots + c_n \bar v_n$$ implies that $$c_1 = c_2 = \dots = c_n = 0$$

---

Let $$\bar x_1, \bar x_2, \dots, \bar x_n \in \mathbb{R}^n$$ and let the matrix $$X$$ be the row vector composed of the column vectors $$\bar x_1, \dots, \bar x_n$$, or $$X = (\bar x_1, \bar x_2, \dots, \bar x_n)$$ The vectors $$\bar x_1, \dots, \bar x_n$$ are **linearly dependent** if and only if the determinant of $$X$$ is 0.

---

Where $$V$$ is a vector space, $$S$$ is a subset of that space, and $$\bar v$$ is an element of $$V$$, then $$\operatorname{span}(S \cup \{\bar v \}) = \operatorname{span}(S)$$ if and only if $$\bar v \in \operatorname{span}(S)$$.
