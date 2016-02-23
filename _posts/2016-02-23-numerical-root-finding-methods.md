---
layout: post
title: Numerical Root-Finding Methods
---
<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

Root-finding methods are split into roughly two categories: **bracketed** and **open** methods. Bracketed methods examine a function over a closed interval, and use information about sign change to determine the location of a root. Open methods attempt to make more sophisticated guesses using information about $$f(x)$$ and $$f'(x)$$ to find a root.

### **Bisection:**

Given an interval $$[x_{low}, x_{up}]$$, in which the root is known to be, we iteratively cut the interval in half and set the new interval to be one side or another of the old interval. Note that if $$x_{low}x_{up} < 0$$, it implies that exactly one of the two values is negative.

* $$x_{root}$$ is calculated each iteration by $$x_{root} = \frac{x_{low} + x_{up}}{2}$$
* If $$f(x_{low})f(x_{root}) < 0$$, then set $$x_{up} = x_{root}$$
* If $$f(x_{low})f(x_{root}) > 0$$, then set $$x_{low} = x_{root}$$
* If $$f(x_{low})f(x_{root}) = 0$$, then we're done.
* Repeat.

### **False Position** (Regula Falsi):

<img class="centered" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/False_position_method.svg/351px-False_position_method.svg.png" alt="false position">

Using similar triangles

$$\frac{f(x_{low})}{x_{root} - x_{low}} - \frac{f(x_{up})}{x_{up} - x_{root}}$$

We can solve for $$x_{root}$$ and determine what side of the line the root is on by monitoring the sign of $$f(x_{low})f(x_{root})$$. Graphically, $$x_{root}$$ is where the line from $$f(x_{low})$$ to $$f(x_{up})$$ intersects with the $$x$$-axis.

* $$x_{root}$$ is calculated each iteration by $$ x_{root} = x_{up} - \frac{f(x_{up})(x_{low} - x_{up})}{f(x_{low}) - f(x_{up})}$$
* If $$f(x_{low})f(x_{root}) < 0$$, then set $$x_{up} = x_{root}$$
* If $$f(x_{low})f(x_{root}) > 0$$, then set $$x_{low} = x_{root}$$
* If $$f(x_{low})f(x_{root}) = 0$$, then we're done.
* Repeat.

There are a number of pros and cons of bracketed methods. With bracketed methods, the root is always bracketed by an upper and lower bound. The interval also decreases with every step, and bracketed methods are guaranteed to converge on *a* root, though sometimes very slowly.

Bracketed methods are sometimes slow, and can miss multiple roots, especially with functions with even multiplicity (e.g. a parabola where the tip touches the $$x$$-axis exactly once). Bracketed methods also need *a priori* knowledge, such as the number of roots, and the interval the root occurs on.

### **Fixed Point** (Successive Substitution):

<img class="centered" src="http://www.physics.arizona.edu/~restrepo/475A/Notes/sourcea-/img570.png" alt="fixed point">

* Solve the function for $$x$$
* Let $$x = g(x)$$
* Make an initial guess $$x_0$$
* Let $$x_{i + 1} = g(x_i)$$
* Repeat

Sometimes with the Fixed Point method, the manner in which you solve for $$x$$ in step 1 can affect whether the method converges or not. For this method, the slope of $$g(x)$$ near the root should be less than 1.

### **Newton-Raphson's Method**:

* Make an initial guess $$x_0$$
* Use $$f(x_i)$$ and $$f'(x_i)$$ to draw the tangent line at $$x_i$$
* Use the point where the tangent line crosses the $$x$$-axis as the new guess $$x_{i+1}$$.

In particular, $$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$. Due to how the Taylor Series derivation works out, this method has quadratic convergence/divergence. Wherever this method goes, it gets there fast.

Newton's Method (sorry Raphson) has a handful of cons. It can converge slowly, or not at all. If $$f'(x_i) = 0$$ we divide by zero and the universe explodes. Even if $$f'(x_i)$$ is a small value, that corresponds to the tangent line intersecting with the $$x$$-axis very far away from the root. Newton's Method is also sensitive to your initial guess. The biggest con though, is that Newton's Method requires the derivative, which can be hard to calculate. Sometimes you might even be trying to find a root of a non-analytic function (raw data).

### **Secant Method**:

This is the same as Newton's Method, but with $$f'(x_i)$$ replaced by $$f'(x_i) = \frac{f(x_{i-1}) - f(x_i)}{x_{i - 1} - x_i}$$.

We can then find $$x_{i+1}$$ by $$x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)}$$

This method is still sensitive to $$x_0$$, and requires two previous data points to compute the next $$(x_{i-1}, x_i)$$.

### **Modified Secant Method**:

We can remove the requirement to keep $$x_{i-1}$$ in our computations by using the other definition of a derivative.

$$x_{i+1} = x_i - \frac{\delta x_i f(x_i)}{f(x_i + \delta x_i) - f(x_i)}$$ where $$\delta$$ is some small number relative in size to the root.


Maybe someday I'll come back to this and create some better graphics.