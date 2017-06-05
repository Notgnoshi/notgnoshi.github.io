---
layout: post
title: Linear Programming
subtitle: A geometric understanding
meta: A geometric explanation of linear programs, and Karmarkar's Algorithm implemented in Python.
---

<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">
<link rel="stylesheet" href="{{ "/assets/styles/lp.css" | prepend: site.baseurl }}">

## Introduction

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

Now we have a geometric understanding of what points are *possible*, but now we need to find the point in the feasible set that *maximizes* our objective function. Currently, everything we've graphed relate to the LP constraints, and not the objective function. Recall the concept of [Level Curves](https://en.wikipedia.org/wiki/Level_set) from Calculus III. Level curves are curves of fixed $$z$$ values. The following is a graph of several level curves of $$z$$ superimposed on the graph of the feasible set.

<img class="centered" src="{{ "/assets/posts/linear-programming/level-curves.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

See how we can immediately pick out the point that maximizes the value of the objective function? Apparently the **optimal solution** - that maximizes the value of the objective function is directly related to the *slope* of the objective function.

In short, we're going to pick a random point on the interior of the feasible set, and move in the direction that maximizes the change in the objective function. In our 2-dimensional example above this means moving in the direction perpendicular to the level curves illustrated in red below.

<img class="centered" src="{{ "/assets/posts/linear-programming/level-curves-perpendicular.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

We can immediately see that we'll run into a problem however. If we naively go in the red direction, we won't always hit the point on the edge of the feasible set that maximizes our objective function. We're going to have to do something different. True to form, linear algebra comes to our rescue.

---

## Standard Form

First however, we must introduce the idea of LP problems in **standard form**. Problems in standard form are of the form

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = \vec c^T \vec x$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\displaystyle A \vec x = \vec b$$</td></tr>
</table>

This is subtly different than the first form of the LP problem. This one requires that our constraints are that of equality. If not for an algebra trick, this would put a dampener on our plans of <strike>world domination</strike> solving LP problems efficiently.

We will solve our problems by introducing more variables to our problem. Our goal is to reduce an incredibly flexible problem into the standard form of an LP. That way we can develop just one strategy that will solve all of our problems. Here's a list of special cases.

* A $$\leq$$ constraint.
    - Add a **slack variable** $$s_i$$ that can take on any positive value in order to take up the slack required to turn a $$\leq$$ constraint into an $$=$$ constraint.
    - Suppose we have the constraint

      $$4x_1 + 5x_2 \leq 42$$

      We add the slack variable $$s_1$$ to turn the above constraint into

      $$4x_1 + 5x_2 + s_1 = 42$$

      We also append $$s_1$$ to the end of $$\vec x$$ and append a $$0$$ to the end of the cost vector $$\vec c$$.
* A $$\geq$$ constraint.
    - Add an **excess variable** $$e_i$$ that can take on any positive value in order to soak up the excess required to turn a $$\geq$$ constraint into an $$=$$ constraint.
    - Suppose we have the constraint

      $$4x_1 + 5x_2 \geq 42$$

      We add the excess variable $$e_1$$ to turn the above constraint into

      $$4x_1 + 5x_2 - e_1 = 42$$

      We also append $$e_1$$ to the end of $$\vec x$$ and a $$0$$ to the end of $$\vec c$$.
* A constraint with a negative right hand side.
    - Multiply both sides by $$-1$$ and flip inequality to turn into one of the above cases.
    - Suppose we have the constraint

      $$4x_1 + 5x_2 \leq -42$$

      We multiply by negative one

      $$-4x_1 - 5x_2 \geq 42$$

      Then add an excess variable as dictated above

      $$-4x_1 - 5x_2 - e_1 = 42$$
* The problem states to **minimize** the objective function.
    - We maximize the negative of the objective function.
    - Suppose we wish to minimize the function

      $$z = 2x_1 + 3x_2$$

      This is equivalent to maximizing the function

      $$z' = -z = -2x_1 - 3x_2$$

The following cases are for constraints on decision variables. Normally we just have $$\vec x \geq 0$$ elementwise. This is analogous to restricting the feasible set to the first quadrant in 2-dimensions, and its equivalent in $$n$$-dimensions.

* One of the decision variables is constrained to be greater than or equal to some constant $$c$$.
    - Suppose that, rather than all variables being greater than or equal to zero, we have some decision variable $$x_j$$ with the constraint $$x_j \geq c$$. We replace $$x_j$$ by $$x_j' = x_j - c$$, or rather replace $$x_j$$ with $$x_j' - c$$ so that $$x_j \geq 0$$.
    - Note that we also replace this variable in the objective function, which will add an additive constant. This is *not* standard form, and needs to be fixed.
    - Suppose we now have the objective function

      $$z = 30x_1 - 4x_2' + 40$$

      We replace $$z$$ with $$z' + 40$$ and are left with the objective function

      $$z' = 30x_1 - 4x_2$$
* One of the decision variables is **unrestricted in sign**, denoted *urs*.
    - Suppose that the decision variable $$x_j$$ has *no sign restriction* -- it can take on *any* value.

      We define $$x_j = x_j' - x_j''$$ where $$x_j', x_j'' \geq 0$$ and replace all occurrences of $$x_j$$ in our problem with $$x_j' - x_j''$$.

**Example.** Suppose we have the problem

<table class="lp">
    <tr class="text"><td>Minimize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = 2x_1 + 3x_2$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\begin{align*}x_1 - x_2 &\geq -1\\x_1 + 3x_2 &\geq 20\\x_1 + x_2 &= 10\\x_1, x_2 &\geq 0\end{align*}$$</td></tr>
</table>

that we wish to reduce to standard form. First we note this is a minimization problem, so we negate the objective function to get

$$-z = -2x_1 -3x_2$$

Then, taking one constraint at a time, we multiply the first by $$-1$$ to get

$$-1x_1 + x_2 \leq 1$$

to which we add a slack variable $$s_1$$

$$-1x_1 + x_2 + s_1 = 1$$

Then we take the second constraint and add an excess variable $$e_1$$ to get

$$x_1 + 3x_2 - e_1 = 20$$

We get the last constraint for free, as it's already in standard form.

Putting this all together we get the LP in standard form

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle -z = -2x_1 - 3x_2$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\begin{align*}-x_1 + x_2 + s_1 &= 1\\x_1 + 3x_2 -e_1 &= 20\\x_1 + x_2 &= 10\\x_1, x_2 &\geq 0\end{align*}$$</td></tr>
</table>

which we can represent concisely with

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = \vec c^T\vec x$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\begin{align*}A\vec x &= \vec b\\\vec x &\geq 0\end{align*}$$</td></tr>
</table>

where $$\vec c = \begin{pmatrix}-2\\-3\\0\\0\end{pmatrix}$$, $$\vec x = \begin{pmatrix}x_1\\x_2\\s_1\\e_1\end{pmatrix}$$, $$A = \begin{pmatrix}-1 & 1 & 1 & 0\\1 & 3 & 0 & 1\\1 & 1 & 0 & 0\end{pmatrix}$$, and $$\vec b = \begin{pmatrix}1\\20\\10\end{pmatrix}$$.

---

## [Karmarkar's Algorithm](https://en.wikipedia.org/wiki/Karmarkar%27s_algorithm)

How do we describe the direction of greatest change in an $$n$$-dimensional setting. Recall the concept of the **gradient vector** $$\displaystyle \vec \nabla f = \left\langle \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right\rangle$$ which is an $$n$$-dimensional vector of the partial derivatives of $$f$$ that points in the direction of greatest change of the value of $$f$$.

For the function $$f(\vec x) = \vec c^T \vec x$$, the gradient vector $$\vec \nabla f = \vec c$$.

A naive algorithm might therefore be: pick a point in the feasible set and travel in the direction of the gradient vector. However, it is possible (and even likely) that the gradient vector *does not live inside the feasible set*. Therefore, we work with the **projection** of $$\vec c$$ onto the feasible set.

---

### Projections

Suppose we have a vector $$\vec c = (3, 2, 4)$$ that we wish to project onto the $$x_1, x_2$$ plane, illustrated below.

<img class="centered" src="{{ "/assets/posts/linear-programming/projection.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

This is equivalent to the linear algebra problem of projecting onto the solution set (null space) of the system $$A \vec x = \vec 0$$. In this particular example, we wish to project from three dimensions onto two dimensions. This means we need the matrix $$A = \begin{pmatrix}0 & 0 & 1\end{pmatrix}$$ so that in the above system $$x_3$$ gets mapped to $$0$$.

We ultimately wish to find a **projection matrix** $$P$$ such that the projected vector $$\vec c_p = P \vec c$$. We do this by the nightmarish formula $$P = I - A^T(A A^T)^{-1}A$$.

---

**Example.** Consider the problem

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = x_1 + 2x_2$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$x_1 + x_2 \leq 8$$</td></tr>
</table>

Converting to standard form we get the problem

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = x_1 + 2x_2 + 0s_1$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$x_1 + x_2 + s_1 = 8$$</td></tr>
</table>

However, for geometric intuition's sake, I'm going to call $$s_1$$, $$x_3$$ instead:

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = x_1 + 2x_2 + 0x_3$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$x_1 + x_2 + x_3 = 8$$</td></tr>
</table>

Or, rather

<table class="lp">
    <tr class="text"><td>Maximize:</td></tr>
    <tr class="math"><td>$$\displaystyle z = \begin{pmatrix}1 & 2 & 0\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}$$</td></tr>
    <tr class="text"><td>Subject to:</td></tr>
    <tr class="math"><td>$$\begin{pmatrix}1 & 1 & 1\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} = 8$$</td></tr>
</table>

The feasible set and optimal solution are shown below.

<img class="centered" src="{{ "/assets/posts/linear-programming/plane.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

Now we calculate $$\vec \nabla z$$, which, as a consequence of their linearity, for every problem will be $$\vec c$$. Notice how $$\vec c$$ is not within the feasible set.

<img class="centered" src="{{ "/assets/posts/linear-programming/plane-c.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

This means we need to calculate the projection of $$\vec c$$ onto the feasible set $$A$$ in order to move a point $$\vec x_\text{old}$$ to its new home $$\vec x_\text{new}$$ shown below.

<img class="centered" src="{{ "/assets/posts/linear-programming/plane-cp.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

---

### The Algorithm

This is an iterative algorithm. It will take in a starting point $$\vec x$$ and output our next starting point $$\vec x_\text{new}$$. After some unknown number of iterations, it will converge to the optimal solution. This algorithm will work for $$n$$ dimensions, but for sake of notation I will only use 3. Note that all vectors are column vectors.

1. Define a scaling matrix $$D = \begin{pmatrix}x_1 & 0 & 0\\0 & x_2 & 0\\0 & 0 & x_3\end{pmatrix}$$ and its inverse $$D^{-1} = \begin{pmatrix}\frac{1}{x_1} & 0 & 0\\0 & \frac{1}{x_2} & 0\\0 & 0 & \frac{1}{x_3}\end{pmatrix}$$.
    * Use $$D$$ to scale $$\vec x$$ to $$\begin{pmatrix}1\\1\\1\end{pmatrix}$$. This calculation can effectively be ignored, just redefine $$\vec x = \vec 1$$.
    * Compute scaled versions of $$A$$ and $$\vec c$$, call them $$\tilde A$$ and $$\tilde c$$ by

      $$\begin{align*}\tilde A &= AD\\ \tilde c &= D\vec c\end{align*}$$
2. Compute the projection matrix $$P = I - \tilde A^T(\tilde A \tilde A^T)^{-1}\tilde A$$.
    * Compute $$\tilde c_p = P\tilde c$$
3. Compute $$\tilde x_\text{new} = \begin{pmatrix}1\\1\\1\end{pmatrix} + k \tilde c_p$$ where $$k > 0$$ is chosen to take us halfway between where we are and the edge of the feasible set.
    * That is, let $$\displaystyle k = \frac{-\frac{1}{2}}{\min\left\{\tilde c_p\right\}}$$
    * $$k$$ should always be positive -- and $$\min\{\tilde c_p\}$$ should always be negative, and could be read "most negative".
4. Convert $$\tilde x_\text{new}$$ back into original (unscaled) coordinate system by $$\vec x_\text{new} = D \tilde x_\text{new}$$
    * If $$\vec x_\text{new}$$ has changed by less than some defined tolerance, we're done and $$\vec x_\text{new}$$ is within some epsilon of the optimal solution.
    * Otherwise, go back to step 1.

---

Here is a graph of first few iterations of the above example.

<img class="centered" src="{{ "/assets/posts/linear-programming/karmarkar.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

---

Karmarkar's Algorithm is still not *the* standard LP solver algorithm, that title lies firmly in the hands of the [Simple Algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm). There are some edge cases that give us *very* poor performance. However, for very large problems, it offers good performance most of the time. See [here](https://en.wikipedia.org/wiki/Linear_programming#Algorithms) for a description of various LP solver algorithms.

---

### Python Implementation

One of the benefits of Karmarkar's Algorithm, is that it is easy to implement. Here's a first crack at a Python implementation.

Note all vectors must be row vectors for the matrix multiplication dimensions to work out. This is different than the description above, but was necessary for simpler programming.

```python
{% include snippets/linear_program.py %}
```

```python
{% include snippets/karmarkar.py %}
```

Running the `karmarkar.py` script, we get the following output

```
Solution: [[  2.97874012e-06   7.99999553e+00   1.48937006e-06]]
	Tolerance: 5.57390111055e-06
	Iterations: 21
```

Which we can see in the following image.

<img class="centered" src="{{ "/assets/posts/linear-programming/karmarkar-full.svg" | prepend: site.baseurl }}" alt="A Basic Linear Program">

Thanks for <strike>skimming through</strike> reading, I hope you enjoyed it!
