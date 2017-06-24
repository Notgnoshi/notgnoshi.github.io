---
layout: post
title: Limits of Complex Functions
meta: A definition of the limit of a complex-valued function using the definitions of epsilon and deleted neighborhoods.
---

$$\newcommand{\ddz}{\displaystyle \frac{d}{dz}}$$
$$\newcommand{\limdz}{\displaystyle \lim_{\Delta z \to 0}}$$
$$\newcommand{\limz}{\displaystyle \lim_{z \to z_0}}$$

**Defn.** The *limit* of a function $$f$$ at a point $$z_0$$, denoted by $$\displaystyle \limz f(z) = w_0$$ means that for every $$\varepsilon > 0$$ there exists a $$\delta > 0$$ such that

$$\vert f(z) - w_0 \vert < \varepsilon \text{ whenever }0 < \vert z - z_0 \vert < \delta$$

Or rather, that for every $$\varepsilon$$-neighborhood of $$w_0$$ there exists a deleted $$\delta$$-neighborhood of $$z_0$$ whose points $$z$$ map to a point $$w$$ in the $$\varepsilon$$-neighborhood of $$w_0$$.

---

**Thm.** Limits, if they exist at a point $$z_0$$, are unique.

**Pf.** Suppose $$\limz f(z) = w_0$$ and $$\limz f(z) = w_1$$ for some function $$f$$. Then for all $$\varepsilon > 0$$ there exist $$\delta_0, \delta_1 > 0$$ such that

$$\vert f(z) - w_0 \vert < \varepsilon \text{ whenever } 0 < \vert z - z_0 \vert < \delta_0$$

and

$$\vert f(z) - w_1 \vert < \varepsilon \text{ whenever } 0 < \vert z - z_0 \vert < \delta_1$$

So, if $$0 < \vert z - z_0 \vert < \delta$$ where $$\delta = \min\{\delta_0, \delta_1\}$$ we see that

$$\vert w_1 - w_0 \vert = \big\vert [f(z) - w_0] - [f(z) - w_1] \big\vert \leq \vert f(z) - w_0 \vert + \vert f(z) - w_1 \vert < \varepsilon + \varepsilon$$

Or,

$$\vert w_1 - w_0 \vert < 2 \varepsilon$$

Since $$\varepsilon$$ is arbitrarily small, $$\vert w_1 - w_0 \vert$$ must be 0. Thus, $$w_1 = w_0$$.

---

**Thm.** Suppose $$f(z) = u(x, y) + i v(x, y)$$ where $$z = x + iy$$, $$z_0 = x_o + i y_0$$, and $$w_0 = u_0 + i v_0$$. Then $$\limz f(z) = w_0$$ if and only if

$$\displaystyle \lim_{(x, y) \to (x_0, y_0)} u(x, y) = u_0$$

and

$$\displaystyle \lim_{(x, y) \to (x_0, y_0)} v(x, y) = v_0$$

**Pf $$[\Longleftarrow]$$.** Assume $$\displaystyle \lim_{(x, y) \to (x_0, y_0)} u(x, y) = u_0$$ and $$\displaystyle \lim_{(x, y) \to (x_0, y_0)} v(x, y) = v_0$$. That is, for all $$\varepsilon > 0$$ there exist $$\delta_1, \delta_2 > 0$$ such that

$$\vert u - u_0 \vert < \frac{\varepsilon}{2} \text{ whenever } 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta_1$$

and

$$\vert v - v_0 \vert < \frac{\varepsilon}{2} \text{ whenever } 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta_2$$

Let $$0 < \delta < \delta_1, \delta_2$$. Since

$$\underbrace{\big\vert(u + i v) - (u_0 + iv_0)\big\vert}_{\vert w - w_0 \vert} = \big\vert(u - u_0) + i(v - v_0)\big\vert \leq \vert u - u_0 \vert + \vert v - v_0 \vert$$

by the triangle inequality, and

$$\sqrt{(x - x_0)^2 + (y - y_0)^2} = \big\vert(x - x_0) + i(y - y_0)\big\vert = \underbrace{\big\vert(x + iy) - (x_0 + i y_0)\big\vert}_{\vert z - z_0 \vert}$$

It follows that

$$\big\vert (u + iv) - (u_0 + iv_0) \big\vert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} \text{ whenever } 0 < \big\vert(x + iy) - (x_0 + i y_0)\big\vert < \delta$$

**Pf $$[\Longrightarrow]$$.** Assume $$\limz f(z) = w_0$$ holds. Then we know that for all $$\varepsilon > 0$$ there exists a $$\delta > 0$$ such that

$$ \big\vert (u + iv) - (u_0 - iv_0)\big\vert < \varepsilon \text{ whenever } 0 < \big\vert(x + iy) - (x_0 - iy_0)\big\vert < \delta$$

But we know $$\operatorname{Re}z \leq \vert z \vert$$, so

$$ \vert u - u_0 \vert \leq \big\vert (u - u_0) + i(v - v_0) \big\vert = \big\vert(u + iv) - (u_0 + iv_0)\big\vert$$

$$ \vert v - v_0 \vert \leq \big\vert (u - u_0) + i(v - v_0) \big\vert = \big\vert(u + iv) - (u_0 + iv_0)\big\vert$$

and

$$\big\vert(x + iy) - (x_0 + iy_0)\big\vert - \big\vert(x - x_0) + i(y - y_0)\big\vert = \sqrt{(x - x_0)^2 + (y - y_0)^2}$$

It then follows that

$$\vert u - u_0\vert < \varepsilon \text{ and } \vert v - v_0 \vert < \varepsilon$$

whenever

$$0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta$$

---

**Thm.** Let $$\limz f(z) = w_1$$ and $$\limz g(z) = w_2$$. Then

1. $$\limz \big[f(z) + g(z)\big] = \limz f(z) + \limz g(z)$$,
2. $$\limz \big[f(z) \cdot g(z)\big] = \limz f(z) \cdot \limz g(z)$$, and
3. $$\limz\left[\frac{f(z)}{g(z)}\right] = \frac{\limz f(z)}{\limz g(z)}$$.

**Pf (1).** Let $$\varepsilon > 0$$. Then

$$\big\vert f(z) - w_1\big\vert < \frac{\varepsilon}{2} \text{ whenever } 0 < \vert z - z_0 \vert < \delta_1$$

and

$$\big\vert g(z) - w_2\big\vert < \frac{\varepsilon}{2} \text{ whenever } 0 < \vert z - z_0 \vert < \delta_2$$

We wish to show there exists a $$\delta > 0$$ such that

$$\big\vert(f(z) + g(z)) - (w_1 + w_2)\big\vert < \varepsilon \text{ whenever } 0 < \vert z - z_0 \vert < \delta$$

So we then consider $$\big\vert(f(z) + g(z)) - (w_1 + w_2)\big\vert$$.

$$\big\vert(f(z) + g(z)) - (w_1 + w_2)\big\vert = \big\vert (f(z) - w_1) + (g(z) + w_2)\big\vert \leq \vert f(z) - w_1\vert + \vert g(z) - w_2\vert$$

So,

$$\big\vert(f(z) + g(z)) - (w_1 + w_2)\big\vert \leq \vert f(z) - w_1 \vert + \vert g(z) - w_2 \vert$$

Since $$\vert f(z) - w_1 \vert < \frac{\varepsilon}{2}$$ whenever $$0 < \vert z - z_0 \vert < \delta_1$$ and $$\vert g(z) - w_2 \vert < \frac{\varepsilon}{2}$$ whenever $$0 < \vert z - z_0 \vert < \delta_2$$, then

$$\big\vert(f(z) + g(z)) - (w_1 + w_2)\big\vert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} \text{ whenever } 0 < \vert z - z_0 \vert < \delta_1, \delta_2$$

So to meet the requirement that $$0 < \vert z - z_0 \vert$$ be less than both $$\delta_1$$ *and* $$\delta_2$$, we let $$\delta = \min\{\delta_1, \delta_2\}$$. Then

$$\big\vert(f(z) + g(z)) - (w_1 + w_2)\big\vert < \varepsilon \text{ whenever } 0 < \vert z - z_0 \vert < \delta$$

And thus the statement is proved.

**Lemma.**

Consider $$\limz g(z) = w_2$$. Since $$\varepsilon$$ is arbitrary, we pick a convenient $$\varepsilon$$, say, $$\varepsilon = 1$$. Then there exists a specific $$\hat \delta > 0$$ such that

$$\vert g(z) - w_2 \vert < 1 \text{ whenever } 0 < \vert z - z_0 \vert < \hat \delta$$

Then

$$\begin{align*}
\vert g(z) \vert &= \vert g(z) - w_2 + w_2 \vert\\
\vert g(z) \vert &\leq \vert g(z) - w_2 \vert + \vert w_2 \vert\\
\vert g(z) \vert &< 1 + \vert w_2 \vert\\
\vert g(z) \vert &\leq M \text{ for some } M \in \mathbb N\\
\end{align*}$$

whenever $$\vert z - z_0 \vert < \hat \delta$$.

That is, $$\displaystyle S = \big\{ g(z) : \vert z - z_0 \vert < \hat\delta\big\} = g\left(N_{\hat\delta}(z_0)\right)$$ is a bounded set of radius at most $$M$$.

**Pf (2).** We wish to show that for all $$\varepsilon > 0$$ there exists a $$\delta > 0$$ such that

$$\big\vert f(z) \cdot g(z) - w_1 \cdot w_2 \big\vert < \varepsilon \text{ whenever } 0 < \vert z - z_0 \vert < \delta$$

Let $$\varepsilon > 0$$,

$$\vert f(z) - w_1 \vert < \frac{\varepsilon}{2M} \text{ whenever } 0 < \vert z - z_0 \vert < \delta_1$$

and

$$\vert g(z) - w_2 \vert < \frac{\varepsilon}{2(1 + \vert w_1 \vert)} \text{ whenever } 0 < \vert z - z_0 \vert < \delta_2$$

with $$1 + \vert w_1 \vert$$ in the denominator to protect ourselves from division by zero. Then let $$\delta = \min\{\delta_1, \delta_2, \hat\delta\}$$.

We wish to manipulate $$\big\vert f(z)\cdot g(z) - w_1 w_2 \big\vert$$ so that $$\vert f(z) - w_1\vert$$ and $$\vert g(z) - w_1 \vert$$ appear. So,

$$\begin{align*}
\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert &= \big\vert f(z)g(z) - w_1 f(z) + w_1 f(z) - w_1 w_2 \big\vert\\
\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert &= \big\vert \big(f(z) - w_1\big) g(z) + w_1 \big(g(z) - w_2\big) \big\vert\\
\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert &\leq \big\vert f(z) - w_1 \big\vert \cdot \big\vert g(z)\big\vert + \big\vert w_1 \big\vert\cdot \big\vert g(z) - w_2 \big\vert\\
\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert &< \frac{\varepsilon}{2M} \cdot \big\vert g(z) \big\vert + \vert w_1 \vert \cdot \frac{\varepsilon}{2(1 + \vert w_1 \vert)}\\
\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert &< \frac{\varepsilon}{2} \cdot \frac{\big\vert g(z) \big\vert}{M} + \frac{\varepsilon}{2} \cdot \frac{\vert w_1 \vert}{(1 + \vert w_1 \vert)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2}\\
\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert &< \varepsilon\\
\end{align*}$$

Therefore, we have

$$\big\vert f(z) \cdot g(z) - w_1 w_2 \big\vert < \varepsilon \text{ whenever } 0 < \vert z - z_0 \vert < \delta$$

**Lemma.** $$\limz \frac{1}{g(z)} = \frac{1}{w_2}$$ for $$w_2 \neq 0$$.

**Pf.** Since $$\varepsilon$$ is arbitrary, we can pick a specific $$\varepsilon$$ to work with, say $$\displaystyle \varepsilon = \frac{\vert w_2 \vert}{2}$$ and find the specific $$\tilde\delta > 0$$ such that

$$\big\vert g(z) - w_2 \big\vert < \frac{\vert w_2 \vert}{2} \text{ whenever } 0 < \vert z - z_0 \vert < \tilde\delta$$

We let $$\delta = \min\{\delta_2, \tilde\delta\}$$. Then

$$\begin{align*}
\vert w_2 \vert &= \vert w_2 - g(z) + g(z) \vert\\
\vert w_2 \vert &\leq \vert w_2 - g(z) \vert + \vert g(z) \vert\\
\vert w_2 \vert &\leq \vert g(z) - w_2 \vert + \vert g(z) \vert\\
\vert w_2 \vert &< \frac{\vert w_2 \vert}{2} + \vert g(z) \vert\\
\frac{\vert w_2 \vert}{2} &< \vert g(z) \vert\\
\end{align*}$$

whenever $$0 < \vert z - z_0 \vert < \delta$$. Note that $$\frac{\vert w_2 \vert}{2} < \vert g(z) \vert$$ implies that $$\frac{1}{\vert g(z) \vert} < \frac{2}{\vert w_2 \vert}$$ whenever $$0 < \vert z- z_0 \vert < \delta$$.

Now consider $$\displaystyle \left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert$$.

$$\begin{align*}
\left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert &= \left\vert\frac{w_2 - g(z)}{w_2 g(z)}\right\vert\\
\left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert &= \frac{\big\vert g(z) - w_2 \big\vert}{\vert w_2 \vert \cdot \vert g(z) \vert}\\
\left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert &= \frac{1}{\vert w_2 \vert} \cdot \frac{1}{\vert g(z) \vert} \cdot \big\vert g(z) - w_2 \big\vert\\
\left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert &< \frac{1}{\vert w_2 \vert} \cdot \frac{2}{\vert w_2 \vert} \cdot \big\vert g(z) - w_2 \big\vert
\end{align*}$$

We know that $$\displaystyle \big\vert g(z) - w_2 \big\vert < \frac{\varepsilon \vert w_2 \vert^2}{2}$$ (some very specific $$\varepsilon$$) whenever $$0 < \vert z - z_0 \vert < \delta$$

Therefore,

$$\left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert < \frac{2}{\vert w_2 \vert^2} \cdot \frac{\varepsilon \vert w_2 \vert^2}{2}$$

or,

$$\left\vert \frac{1}{\vert g(z) \vert} - \frac{1}{w_2}\right\vert < \varepsilon$$

whenever $$0 < \vert z - z_0 \vert < \delta$$.

And thus $$\limz \frac{1}{g(z)} = \frac{1}{w_2}$$ for $$w_2 \neq 0$$.

**Pf (3).** We wish to show that $$\limz \left[\frac{f(z)}{g(z)}\right] = \frac{\limz f(z)}{\limz g(z)}$$.

So we consider $$\limz \left[\frac{f(z)}{g(z)}\right]$$.

$$\begin{align*}
\limz \left[\frac{f(z)}{g(z)}\right] &= \limz f(z) \cdot \frac{1}{g(z)}\\
&= \limz f(z) \cdot \limz \frac{1}{g(z)}\\
&= \limz f(z) \cdot \frac{1}{\limz g(z)}\\
&= \frac{\limz f(z)}{\limz g(z)}\\
\end{align*}$$

And thus $$\limz \left[\frac{f(z)}{g(z)}\right] = \frac{\limz f(z)}{\limz g(z)}$$.

---
