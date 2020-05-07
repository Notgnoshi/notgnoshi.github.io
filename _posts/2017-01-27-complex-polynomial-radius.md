---
layout: post
title: Complex Polynomial Inequality Verification
meta: The verification of a complex polynomial inequality as stated in my Complex Analysis textbook
redirect_to: https://agill.xyz/blog/complex-polynomial-inequality-verification
---

**Defn.** For $$z, a_i \in \mathbb C$$ and $$n \in \mathbb R^+$$

$$P(z) = a_0 + a_1 z + a_2 z^2 + \dots + a_n z_n$$

with $$a_n \neq 0$$ (i.e. has a $$n$$th term) is called a *polynomial* of degree $$n$$.

**Inequality.**

$$\left\vert\frac{1}{P(z)}\right\vert < \frac{2}{\vert a_n\vert R^n}$$

whenever $$\vert z\vert > R$$ for some $$R \in \mathbb R^+$$. In other words, $$\left\vert\frac{1}{P(z)}\right\vert$$ is bounded above by $$\frac{2}{\vert a_n \vert R^n}$$ when $$z$$ is sufficiently large.

**Verification.**

Let $$\displaystyle{w = \frac{a_0}{z^n} + \frac{a_1}{z^{n-1}} + \frac{a_2}{z^{n-2}} + \dots + \frac{a_{n-1}}{z}}$$, then $$P(z) = (a_n+ w)z^n$$. Also note that $$\vert P(z)\vert = \vert a_n + w \vert \cdot \vert z^n \vert$$. Since $$\vert z^n \vert = \vert z \vert ^n$$, we can write $$\vert P(z)\vert = \vert a_n + w \vert \cdot \vert z \vert ^n$$.

We see that

$$wz^n = a_0 + a_1 z + a_2 z^2 + \dots + a_{n-1}z^{n-1}$$.

So by the general triangle inequality

$$\vert w \vert \vert z \vert ^n \leq \vert a_0 \vert + \vert a_1 \vert \vert z \vert + \vert a_2 \vert \vert z \vert ^2 + \dots + \vert a_{n-1} \vert \vert z \vert ^{n-1}$$

or,

$$\vert w \vert \leq \frac{\vert a_0 \vert}{\vert z \vert ^ {n}} + \frac{\vert a_1 \vert}{\vert z \vert ^ {n - 1}} + \frac{\vert a_2 \vert}{\vert z \vert ^ {n - 2}} + \dots + \frac{\vert a_{n - 1}\vert}{\vert z \vert}$$

Certainly, if we pick a large enough $$z$$, the following is true:

$$\vert w \vert < \vert a_n \vert$$

For some reason, the above will not be nearly as useful to us as the following, so that will be what we will work with.

$$\vert w \vert < \frac{\vert a_n \vert}{2}$$

That is, the $$a_n z^n$$ term asymptotically dominates the rest - for a large enough $$z$$.

So by the triangle inequality,

$$\vert a_n + w \vert \geq \left\vert \vert a_n \vert - \vert w \vert \right\vert$$

Since $$\vert w \vert < \frac{\vert a_n \vert}{2}$$, then $$\left\vert \vert a_n \vert - \vert w \vert \right\vert > \frac{\vert a_n \vert}{2}$$ -- that is, taking away less than half of $$\vert a_n \vert$$ leaves more than half of $$\vert a_n \vert$$. So we then have

$$\vert a_n + w \vert \geq \left\vert \vert a_n \vert - \vert w \vert \right\vert > \frac{\vert a_n \vert}{2}$$

All provided that $$z$$ is of sufficient size. Since $$\vert a_n + w \vert \cdot \vert z \vert^n > \frac{\vert a_n \vert}{2} \cdot \vert z \vert ^n$$, we have

$$\vert P(z) \vert = \vert a_n + w \vert \cdot \vert z \vert^n > \frac{\vert a_n \vert}{2} \cdot \vert z \vert^n$$

Then, if $$\vert z \vert > R$$, we have

$$\vert P(z) \vert > \frac{\vert a_n \vert}{2} \cdot \vert z \vert ^n > \frac{\vert a_n \vert}{2} \cdot R^n$$

or,

$$\left\vert \frac{1}{P(z)}\right\vert < \frac{2}{\vert a_n \vert R^n}$$

And thus the inequality is verified.

---

I apologize for the readability of $$\left\vert \vert a \vert \pm \vert b \vert \right\vert$$ -- MathJax does not allow for making the outermost `\vert`s bigger with `\left\vert`/`\right\vert` or `\big\vert` like a normal $$\LaTeX$$ document would.
