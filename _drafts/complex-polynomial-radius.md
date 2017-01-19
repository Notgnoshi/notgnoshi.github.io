---
layout: post
title: Complex Polynomial Inequality Verification
meta: The verification of a complex polynomial inequality as stated in my Complex Analysis textbook
permalink: polynomials/
---

**Defn.** For $$z, a_i \in \mathbb C$$ and $$n \in \mathbb R^+$$

$$P(z) = a_0 + a_1 z + a_2 z^2 + \dots + a_n z_n$$

with $$a_n \neq 0$$ (i.e. has a $$n$$th term) is called a *polynomial* of degree $$n$$.

**Inequality.**

$$\left\vert\frac{1}{P(z)}\right\vert < \frac{2}{\vert a_n\vert R^n}$$

whenever $$\vert z\vert > R$$ for some $$R \in \mathbb R^+$$. In other words, $$\left\vert\frac{1}{P(z)}\right\vert$$ is bounded above by $$\frac{2}{\vert a_n \vert R^n}$$ when $$z$$ is sufficiently large.

**Verification.**

Let $$\displaystyle{w = \frac{a_0}{z^n} + \frac{a_1}{z^{n-1}} + \frac{a_2}{z^{n-2}} + \dots + \frac{a_{n-1}}{z}}$$, then $$P(z) = (a_n+ w)z^n$$. Also note that $$\vert P(z)\vert = \vert a_n + w \vert \vert z^n \vert$$. Since $$\vert z^n \vert = \vert z \vert ^n$$, we can write $$\vert P(z)\vert = \vert a_n + w \vert \vert z \vert ^n$$.

We see that

$$wz^n = a_0 + a_1 z + a_2 z^2 + \dots + a_{n-1}z^{n-1}$$.

So by the general triangle inequality

$$\vert w \vert \vert z \vert ^n \leq \vert a_0 \vert + \vert a_1 \vert \vert z \vert + \vert a_2 \vert \vert z \vert ^2 + \dots + \vert a_{n-1} \vert \vert z \vert ^{n-1}$$

mod
