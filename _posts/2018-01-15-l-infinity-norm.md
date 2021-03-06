---
layout: post
title: An infinity norm proof
meta: My Deep Learning professor thought it would be a great idea to jump his class with a limit proof of lim p -> infty L_p = L_infty
redirect_to: https://agill.xyz/blog/an-infinity-norm-proof
---

$$\newcommand{\norm}[1]{\left\lVert#1\right\rVert}$$

The $$L^p$$ norm is formally defined as

$$\norm{x}_p = \left( \sum_i \vert x_i \vert ^p \right) ^ \frac{1}{p}$$

The $$L^p$$ norm has several special cases that supposedly arise often in linear algebra, numerical analysis, and machine learning.

* The $$L^1$$ norm, commonly called the "taxicab" norm:

  $$\norm{x}_1 = \sum_i \vert x_i \vert$$
* The $$L^2$$ norm, commonly called the "Euclidean" norm:

  $$\norm{x}_2 = \sqrt{\sum_i x_i^2}$$
* The $$L_\infty$$ norm:

  $$\norm{x}_\infty = \max_i \vert x_i \vert$$

---

It can be shown that this definition of the $$L^\infty$$ norm is equivalent to taking the limit as $$p \to \infty$$ of the $$L^p$$ norm:

**Proof.** Let $$\displaystyle\norm{x}_\infty = \max_i \vert x_i \vert$$ and $$\displaystyle\norm{x}_p = \left( \sum_i \vert x_i \vert ^p \right) ^ \frac{1}{p}$$. We wish to show that $$\displaystyle\lim_{p \to \infty} \norm{x}_p = \norm{x}_\infty$$.

We have that

$$\begin{align*}
\norm{x}_p &= \norm{x}_\infty \frac{\left( \sum_i \vert x_i \vert ^ p \right)^\frac{1}{p}}{\norm{x}_\infty}\\
&= \norm{x}_\infty \left(\sum_i \frac{\vert x_i \vert ^p}{\norm{x}_\infty^p} \right)^\frac{1}{p}\\
&= \norm{x}_\infty \left(\sum_i \left(\frac{\vert x_i \vert}{\norm{x}_\infty}\right)^p\right)^\frac{1}{p}\\
&\leq \norm{x}_\infty n^\frac{1}{p}
\end{align*}$$

We arrive at the last item because $$\displaystyle\left(\frac{\vert x_i \vert}{\norm{x}_\infty}\right)^p \leq 1$$ for every $$i$$ (because $$\norm{x}_\infty \geq \vert x_i \vert$$ for each $$i$$). Thus we have

$$\norm{x}_\infty \leq \norm{x}_p \leq \norm{x}_\infty n^\frac{1}{p}$$

so, taking a limit as $$p \to \infty$$, we have

$$\norm{x}_\infty \leq \lim_{p \to \infty} \norm{x}_p \leq \norm{x}_\infty \cdot \lim_{p \to \infty} n ^ \frac{1}{p} = \norm{x}_\infty$$

In other words, we have $$\lim_{p \to \infty} \norm{x}_p$$ sandwiched between $$\norm{x}_\infty$$ and $$\norm{x}_\infty$$, implying equality. Therefore $$\displaystyle\lim_{p \to \infty} \norm{x}_p = \norm{x}_\infty = \max_i \vert x_i \vert$$.

---

Consider also this proof:

**Proof.** Let $$\displaystyle\norm{x}_p = \left( \sum_i \vert x_i \vert ^p \right) ^ \frac{1}{p}$$. Observe that for all $$x$$ we have that

$$\max_i \vert x_i \vert \leq \norm{x}_p$$

and that

$$\norm{x}_p \leq \left(\sum_i \max_i \vert x_i \vert^p\right)^\frac{1}{p}$$

Thus,

$$\max_i \vert x_i \vert \leq \norm{x}_p \leq \left(\sum_i \max_i \vert x_i \vert ^p\right)^\frac{1}{p}$$

but then,

$$\left(\sum_i \max_i \vert x_i \vert ^p\right)^\frac{1}{p} = \left(n \cdot \max_i \vert x_i \vert ^ p\right)^\frac{1}{p} = n^\frac{1}{p} \cdot \max_i \vert x_i \vert$$

Thus

$$\max_i \vert x_i \vert \leq \norm{x}_p \leq n^\frac{1}{p} \cdot \max_i \vert x_i \vert$$

however, $$\displaystyle\lim_{p \to \infty} n^\frac{1}{p} = 1$$, so

$$\max_i \vert x_i \vert \leq \lim_{p \to \infty}\norm{x}_p \leq \max_i \vert x_i \vert$$

or rather, that $$\displaystyle\norm{x}_\infty = \lim_{p \to \infty} \norm{x}_p = \max_i \vert x_i \vert$$.
