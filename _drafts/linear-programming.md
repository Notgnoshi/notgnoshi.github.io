---
layout: post
title: Linear Programming
subtitle: A geometric understanding
meta: A geometric explanation of linear programs, Karmarkar's Algorithm, and the Simplex Algorithm.
---

<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">
<link rel="stylesheet" href="{{ "/assets/styles/lp.css" | prepend: site.baseurl }}">

A **Linear Program** (LP) is a problem of the form

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = \vec c^T \vec x$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\displaystyle A \vec x \leq \vec b$$</td></tr>
</table>

Where the inequality is element-wise.

---

**Ex.** Consider the following problem

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = 3 x_1 + 2 x_2$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\begin{align*}2x_1 + x_2 &\leq 100\\x_1 + x_2 &\leq 80\\x_1 &\leq 40\\x_1, x_2 &\geq 0\end{align*}$$</td></tr>
</table>

We wish to maximize the value of the **objective function**

$$z = 3x_1 + 2x_2$$

Subject to the constraints

$$\begin{align*}
    2x_1 + x_2 &\leq 100\\
    x_1 + x_2 &\leq 80\\
    x_1 &\leq 40\\
    x_1, x_2 &\geq 0\\
\end{align*}$$

The last constraint, stating that $$x_1, x_2 \geq 0$$ is called the **non-negativity constraint** and is typically not stated for basic problems. We call the components $$x_1, x_2$$ of the vector $$\vec x$$ the LP **decision variables**, and the coefficients of the objective function $$3$$ and $$2$$ components of the **cost vector** $$\vec c$$.

Note that we can represent the constraints in one fell swoop using the matrix inequality

$$\begin{pmatrix}2 & 1\\1 & 1\\1 & 0\\\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix} \leq \begin{pmatrix}100\\80\\40\end{pmatrix}$$

We call the points $$x_1, x_2, \dots, x_n$$ that satisfy all of the given constraints **feasible points** and the set of all feasible points the **feasible set**.

The feasible set for this example problem (that's conveniently 2-dimensional) is illustrated below. Note that these problems don't have to be 2-dimensional, and in fact, most are not. Sadly though, it's really hard to draw a 4,732-dimensional feasible set to gain some geometric intuition. The challenge of solving these problems comes from their size.

<img class="centered" src="{{ "/assets/posts/linear-programming/basic.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

Now we have a geometric understanding of what points are *possible*, but now we need to find the point in the feasible set that *maximizes* our objective function. Currently, everything we've graphed relate to the LP constraints, and not the objective function. Recall the concept of [Level Curves](https://en.wikipedia.org/wiki/Level_set) from Calculus III. The following is a graph of several level curves of $$z$$, in increasing order, superimposed on the graph of the feasible set.

<img class="centered" src="{{ "/assets/posts/linear-programming/level-curves.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

See how we can immediately pick out the point that maximizes the value of the objective function? Apparently the **optimal solution** - that maximizes the value of the objective function is directly related to the *slope* of the objective function. However, recall that we're trying to find solutions to these problems in much higher dimensions, in which we do not have a concept of slope. We therefore use the idea of the **gradient vector** from Calculus III.
