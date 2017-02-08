---
layout: post
title: Complex-Valued Functions
meta: Functions of complex variables, covering topics such as injective, surjective, domain, range, image, preimage, etc.
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

**Defn.** A *function* $$f$$ defined on a set $$S \subseteq \mathbb C$$ is a *rule* that assigns to each $$z \in S$$ a complex number $$w$$, called the *value* of $$f$$ at $$z$$ and is denote by $$f(z)$$.

**Defn.** We call the set $$S$$ the *domain of definition* of $$f$$.

Note that both the domain of definition and the rule should be specified for a complete definition of a function. If the domain of definition is *not* given, it is assumed to be the largest possible set.

For example, the function $$w = f(z) = \frac{1}{z} = z^{-1}$$ is well defined except where $$z = 0$$, so the domain of definition is $$\mathbb C \setminus \{0\}$$.

---

Suppose we have a function $$w = f(z)$$ for $$z = x + iy$$ and $$w = u + iv$$. Then we have $$u + iv = f(x + iy)$$, so we can express the complex-valued function $$f$$ in terms of a pair of real-valued function of $$x$$ and $$y$$.

$$f(z) = u(x, y) + iv(x, y)$$

And if we use polar coordinates

$$f(re^{i\theta}) = u + iv$$

we then have

$$f(re^{i\theta}) = u(r, \theta) + iv(r, \theta)$$

For example, take the function $$f(z) = z^2$$. Then we have $$f(x + iy) = (x + iy)^2 = x^2 - y^2 + 2ixy$$. So then

$$u(x, y) = x^2 - y^2$$

and

$$v(x, y) = 2xy$$

If we use polar coordinates,

$$f(re^{i\theta}) = (re^{i\theta})^2 = r^2 e^{i2\theta} = r^2 \cos{2\theta} + ir^2 \sin{2\theta}$$

So

$$u(r, \theta) = r^2 \cos{2\theta}$$

and

$$v(r, \theta) = r^2 \sin{2\theta}$$

---

**Defn.** If $$v$$ every *always* equals 0, we call $$f$$ a *real-valued function* of a complex variable.

**Defn.** A *polynomial of degree $$n$$* is the function

$$P(z) = a_0 + a_1 z + a_2 z^2 + \dots + a_n z^n$$

for $$a_i \in \mathbb C, n \in \mathbb Z^+, \text{ and } a_n \neq 0$$. Note that the requirement of $$a_n \neq 0$$ simply means that the $$n$$th degreen polynomial *actually has an $$n$$th term*.

**Defn.** Quotients $$\displaystyle \frac{P(z)}{Q(z)}$$ are called *rational functions* and are defined for all $$z$$ such that $$Q(z) \neq 0$$.

---

Graphing complex functions is *hard*. We have 2 dimensional inputs, *and* 2 dimensional outputs. That means we're working with a 4 dimensional function -- *even for the simple ones.* Since $$w = f(z)$$ is a complex number, both $$z$$ and $$w$$ can be interpreted on points in a plane. Therefore, we can draw the $$z$$ and $$w$$ planes separately. We can therefore view a function $$w = f(z)$$ as a *transformation*, or a *mapping* from points in the $$z$$-plane to points in the $$w$$-plane.

We can describe these transformations with the terms *translation*, *rotation*, *reflection*, and *scaling*, or *stretching*.

---

**Defn.** The *image* of a point $$z_0$$ in the domain of definition $$S$$ of a function $$f$$ is the point $$w_0 = f(z_0)$$. The term *image* of $$z$$ is equivalent to the term *value* of $$f$$ at $$z$$.

We can also take images of *sets*. Let $$T \subseteq S$$, then the *image* of $$T$$ is the set of images of all the points in $$T$$. We denote this by $$f(T)$$.

**Defn.** The *range* of a function $$f$$ is the image of the domain of definition $$S$$. We denote this by $$f(S)$$.

**Defn.** The *inverse image*, or *preimage* of a point $$w$$ is the set of all $$z \in S$$ that have an image of $$w$$. Note that the preimage can have no, one, or many points in $$S$$. My professor denotes this as $$f^{-1}(\{w\})$$ to emphasize that this is *not* the inverse function of $$f$$, it's just a set.

**Defn.** A function $$f$$ is called *injective*, or *one-to-one* if whenever $$f(z_1) = f(z_2)$$, then $$z_1 = z_2$$.

**Defn.** A function $$f$$ is called *surjective*, or *onto* if for every $$w$$ in the range of $$f$$ there exists a $$z$$ in the domain of definition of $$f$$ such that $$f(z) = w$$.

Note that how we have defined the range of a function causes every function to be surjective. This is in conflict with most textbooks that also define something called a *codomain*, or which the range of $$f$$ is a subset. However, this is what my particular textbook uses, so it's what I will stick with here.

**TODO:** Example images of domain, range, and all that jazz here.

---

**Ex.** $$w = f(z) = z + 1 = (x + 1) + iy$$ is a function that *shifts*, or *translates* points one unit to the right.

**Ex.** Since we know that $$i = e^{i\frac{\pi}{2}}$$, the function $$f(z) = iz = ire^{i\theta} = e^{i\frac{\pi}{2}}re^{i\theta} = re^{i\theta + \frac{\pi}{2}}$$ actually rotates a point $$z$$ $$\frac{\pi}{2}$$ radians -- that is, rotates numbers 90 degrees counterclockwise.

**Ex.** The function $$f(z) = \bar z = x - iy$$ is a simple reflection about the real axis.

**Ex.** Now consider again the function $$f(z) = z^2$$. We can rewrite $$f$$ in terms of real-valued functions

$$u = x^2 - y^2$$

and

$$v = 2xy$$

And think of $$f$$ as a transformation from the $$x$$-$$y$$ plane to the $$u$$-$$v$$ plane. Because we're so unfamiliar with complex functions, even for a function so simple as $$z^2$$, we'll ask ourselves a series of questions about it.

*I wonder what maps to a constant?* Just for the heck of it, we'll set $$u = c$$ for some $$c > 0$$ and see what falls out.

That means we have points on the family of hyperbolas $$x^2 - y^2 = c$$, or $$\displaystyle \frac{x^2}{c} - \frac{y^2}{c} = 1$$ in the $$x$$-$$y$$ plane being mapped to points along the straight line $$u = c$$ in the $$u$$-$$v$$ plane.

<img class="centered-full" src="{{ "/assets/posts/complex-functions/hyperbola-1.svg" | prepend: site.baseurl }}" alt="Hyperbola">

Now what happens if we let $$u = -c$$? Then we have points on the family of hyperbolas $$x^2 - y^2 = -c$$, or $$\displaystyle \frac{y^2}{c} - \frac{x^2}{c} = 1$$

<img class="centered-full" src="{{ "/assets/posts/complex-functions/hyperbola-2.svg" | prepend: site.baseurl }}" alt="Hyperbola">

That all is if we fix $$u$$ to be some constant, what happens if we fix $$v$$ to be some positive constant? Then we have points along the $$2xy = c$$, or $$\displaystyle y = \frac{c}{2x}$$ family of hyperbolas in the $$x$$-$$y$$ plane being mapped to some positive $$v = c$$ in the $$u$$-$$v$$ plane.

<img class="centered-full" src="{{ "/assets/posts/complex-functions/hyperbola-3.svg" | prepend: site.baseurl }}" alt="Hyperbola">

Again, what if we pick a negative constant? Then we have $$\displaystyle y = \frac{-c}{2x}$$ being mapped to some negative constant $$v$$ in the $$u$$-$$v$$ plane.

<img class="centered-full" src="{{ "/assets/posts/complex-functions/hyperbola-4.svg" | prepend: site.baseurl }}" alt="Hyperbola">

We asked ourselves what maps to a constant, now we ask, what does a constant map to? That is, let $$x = c$$ and $$y$$ vary. Then $$u = c^2 - y^2$$ and $$v = 2cy$$ which combine to make $$\displaystyle u = c^2 - \frac{v^2}{4c^2}$$

<img class="centered-full" src="{{ "/assets/posts/complex-functions/hyperbola-5.svg" | prepend: site.baseurl }}" alt="Hyperbola">

**TODO:** look at how regions map.
