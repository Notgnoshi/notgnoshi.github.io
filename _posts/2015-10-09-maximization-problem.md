---
layout: post
title: Area Maximization Problem
---

At the most recent math club meeting on campus we solved the following problem. It was a group effort, though largely just the work of our president was what was helpful. One of the professors asked me to write up our solution, which I will duplicate here. This is slightly more polished than what I first submitted because both the club president and our faculty advisor proposed changes. Enough rambling.

### The Problem:

Given the following arrangement of rectangle $$R$$ and $$S$$, and triangle $$T$$, maximize the ratio

$$ \Theta = \frac{A(R) + A(S)}{A(T)} $$

where $$A(T)$$, $$A(R)$$, and $$A(S)$$ represents the area of triangle $$T$$ and rectangles $$R$$ and $$S$$ respectively. Let $$h$$ and $$b$$ be real numbers, and let $$0 < s < r < 1$$. We define our shapes by the following diagram.

<img src="{{ "/assets/maximization-problem/fig1.png"  | prepend: site.baseurl }}" alt="Triangle T" style="margin-left:auto; margin-right:auto; display:block;"/>

The general outline of our problem solving strategy will be:

* Find functions of $$h$$, $$r$$, $$s$$, $$b$$, and $$c$$ for the widths of rectangles $$R$$ and $$S$$.
* Find equations for the areas of rectangles $$R$$ and $$S$$.
* Simplify and substitute these equations into the ratio $$\Theta$$.
* Simplify and cancel anything possible in ratio $$\Theta$$.
* If ratio $$\Theta$$ simplifies to a function of two variables, take the partial derivatives of $$\Theta$$.
* Set partial derivatives equal to zero and solve for the two variables.

First, the triangles $$T$$ and $$T_s$$ are similar.

<img src="{{ "/assets/maximization-problem/fig2.png"  | prepend: site.baseurl }}" alt="Triangles T and T_s" style="margin-left:auto; margin-right:auto; display:block;"/>

This means that we can represent $$s_w$$ using a ratio. Specifically, we have

$$ \frac{s_w}{b} = \frac{h-sh}{h} = 1 - s $$

We can then solve for $$s_w$$. We repeat the same for $$r_w$$, getting the following for $$r_w$$ and $$s_w$$.

$$ s_w = b(1-s) $$

$$ r_w = b(1-r)	$$

Then we use these values to find the areas of the rectangles.

$$ A(S) = b h s (1 - s) $$

$$ A(R) = b(rh-sh)(1-r) = b h (r - s) (1 - r) $$

The area of the triangle is simply

$$ A(T) = \frac{1}{2} b h $$

Substituting these into the ratio $$\Theta$$ we get

$$\Theta = \frac{A(R) + A(S)}{A(T)} \\
	       = \frac{2 \left(bhs(1-s) + bh(r-s)(1-r)\right) }{b h}\\
		   = 2\left(s(1-s) + (r-s)(1-r)\right)\\
		   = 2(s - s^2 + r - s - r^2 + rs)\\
		   = 2(r + rs - s^2 - r^2)
$$

We want to maximize

$$ \Theta = -2s^2 - 2r^2 + 2r + 2rs	$$

Taking the partial derivatives of $$\Theta$$

$$ \Theta_s  = -2s + r ~,~~~ \Theta_{ss} = -2\\
	\Theta_r  = -2r + 1 + s ~,~~~ \Theta_{rr} = -2\\
	\Theta_{rs} = \Theta_{sr} = 1
$$

Since $$\Theta_{ss} < 0$$ and $$\Theta_{ss}\Theta_{rr} - \Theta_{rs}^2 = (-2)(-2) - 1 = 3 > 0$$, a maximum value exists at the point obtained by setting the first partial derivatives to zero and solving for $$r$$ and $$s$$ (Second-Derivative Test in two dimensions).

$$ \begin{cases}
	r-2s &= 0 \\
	s+1-2r &= 0
	\end{cases}
$$

$$ r = 2s\\
    s+1-4s = 0\\
    3s = 1
$$


We get $$s = \frac{1}{3}$$ and $$r = \frac{2}{3}$$. These correspond to a maximum value for $$\Theta$$ of $$\frac{2}{3}$$. The results make intuitive sense because if we let let $$h=b=1$$, then rectangle $$R$$ is a square with dimensions $$\frac{1}{3}$$-by-$$\frac{1}{3}$$. The rectangle $$S$$ is just two of these squares stuck together. This seems to suggest that the best way to approximate the area of a triangle with $$n$$ inscribed rectangles is to fill it with $$\frac{n(n-1)}{2}$$ squares of dimension $$\frac{1}{n+1}$$, where each inscribed rectangle on level $$i$$ starting from the base, with $$0 \leq i < n$$, is constructed from $$n - i$$ of these squares. Moreover, the ratio $$\Theta$$ has maximum $$\frac{n}{n+1}$$.
