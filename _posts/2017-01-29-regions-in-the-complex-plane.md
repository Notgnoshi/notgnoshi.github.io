---
layout: post
title: Regions in the Complex Plane
meta: The topological definitions that form the foundation for the development of limits and consideration of regions in the complex plane in complex analysis
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

Before we can rigorously develop a good foundation for the concepts of functions and limits we need some set theoretic definitions that will presumably come in handy later.

**Defn.** An *$$\varepsilon$$-neighborhood* of a point $$z_0$$, often denoted as $$N_\varepsilon (z_0)$$ is the set of all points $$z$$ lying inside but not on a circle of radius $$\varepsilon$$ centered at $$z_0$$.

$$N_\varepsilon (z_0) = \{z \in \mathbb C : \vert z - z_0 \vert < \varepsilon\}$$

It is understood that when we speak of a *neighborhood* we are speaking of an $$\varepsilon$$-neighborhood. Also note that the value of $$\varepsilon$$ is unspecified -- it could be 0.1, 1000, or 42 -- whatever we need for the current circumstance.

Topologists are fond of calling these structures *open balls*.

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/e-neighborhood.svg" | prepend: site.baseurl }}" alt="Epsilon Neighborhood">

**Defn.** A *deleted neighborhood*, also called a *punctured disk* of a point $$z_0$$ is an $$\varepsilon$$-neighborhood of $$z_0$$ that does not contain $$z_0$$. In set-theoretic notation we can write the deleted neighborhood of $$z_0$$ as $$N_\varepsilon (z_0) \setminus \{z_0\}$$

**Defn.** An *interior point* is a point $$z_0$$ of a set $$S$$ such that there exists some neighborhood of $$z_0$$ that is entirely contained in $$S$$. Or, $$\exists \varepsilon  > 0$$ such that $$N_\varepsilon (z_0) \subseteq S$$

**Defn.** An *exterior point* is a point $$z_0$$ such that there exists some neighborhood of $$z_0$$ containing no points in $$S$$. Or, $$\exists \varepsilon > 0$$ such that $$N_\varepsilon (z_0) \not\subseteq S$$

**Defn.** A *boundary point* is a point $$z_0$$ of a set $$S$$  that is neither an interior point of $$S$$ or an exterior point of $$S$$. Equivalently, a boundary point is a point $$z_0$$ such that every neighborhood of $$z_0$$ contains at least one point in $$S$$ and at least one point not in $$S$$.

Or, $$\forall \varepsilon > 0,\, \exists p_1, p_2 \in N_\varepsilon (z_0)$$ such that $$p_1 \in S$$ and $$p_2 \not\in S$$.

**Defn.** The *boundary* of a set $$S$$ is the set of all the boundary points of $$S$$.

**Defn.** An *open set* is a set that contains none of its boundary points. A set is open if and only if each of its points is an interior point.

**Defn.** A *closed set* is a set that contains all of its boundary points.

---

Note that not being open *does not imply* being closed! E.g. if a set contains a *single* boundary point it is not open, but is not closed either. Also note that a set can be *both* open *and* closed. For example, $$\mathbb C$$ has no boundary points, so it contains all of them, yet each of its points is an interior point, so it is both open *and* closed. A tongue in cheek name for such sets is *clopen*.

---

**Defn.** The *closure* of a set is the closed set consisting of all points in $$S$$ together with the boundary of $$S$$, denoted by $$\operatorname{Cl}(S)$$. The closure can be thought of as an operation to a set.

**Defn.** A *connected set* is an open set $$S$$ such that any pair of points $$z_1, z_2 \in S$$ can be joined by a polygonal line that lies entirely in $$S$$.

**Defn.** A *polygonal line* is a finite number of line segments joined end to end.

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/connected-set.svg" | prepend: site.baseurl }}" alt="A connected set">

**Defn.** A *domain* is a nonempty, open, connected set. Note that any neighborhood is a domain.

**Defn.** A *region* is a domain together with none, some, or all of its boundary points.

**Defn.** A set is *bounded* if every point in $$S$$ lies inside some circle $$\vert z \vert = R$$ with some finite radius $$R$$. Otherwise, $$S$$ is *unbounded*.

**Defn.** An *accumulation point* of a set $$S$$ is a point $$z_0$$ such that every deleted neighborhood of $$z_0$$ contains at least one point of $$S$$. Note that closed sets contain all of their accumulation points.

---

### Examples

Is the set $$S = \{z \in \mathbb C : \operatorname{Re}z \geq 1, \text{ and } \operatorname{Im}z > 2\}$$ illustrated below, open, closed, or neither? How can a set be neither open or closed??

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/not-open-closed.svg" | prepend: site.baseurl }}" alt="A set that is neither open nor closed">

We ask ourselves, does $$S$$ contain any of its boundary points (is it open?) No, $$S$$ contains at least one of its boundary points, so it is therefore *not* open.

Does $$S$$ contain *all* of its boundary points (is it closed?) No, $$S$$ is missing a part of its boundary -- namely the $$\operatorname{Im}z = 2$$ boundary. So therefore $$S$$ is *not* closed.

We can then see that the definitions of open and closed are *not* opposites -- A set can be neither open nor closed.

---

Now consider the set $$\mathbb C$$. First, we ask if $$\mathbb C$$ has any boundary points. It doesn't. Does $$\mathbb C$$ contain all of its 0 boundary points? Yes. Also, $$\mathbb C$$ *doesn't* contain its 0 boundary points -- because they don't exist!

$$\mathbb C$$ is therefore *both* open *and* closed!

What about $$\emptyset$$? It certainly does not contain any of its boundary points -- namely because it contains absolutely nothing! However, as there are no boundary points to contain, it contains all of them. So the empty set is *both* empty *and* closed!

---

Now what about $$S = \{z \in \mathbb C : \operatorname{Re}z \geq 1, \text{ and } \operatorname{Im}z \geq 2, z \neq 0\}$$ illustrated below?

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/not-open-closed-2.svg" | prepend: site.baseurl }}" alt="Another set that is neither open nor closed">

Again, there's *a* boundary point that is not in $$S$$, so $$S$$ is not closed, but it's also not open, as $$S$$ does contain *some* of its boundary points.

---

Now what if we take $$T = S \cup \{0\}$$, or rather, include 0 in the above set?

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/closed-set.svg" | prepend: site.baseurl }}" alt="Finally a set that's closed">

Now, $$T$$ *does* contain *all* of its boundary points, so $$T$$ is closed! We also ask ourselves again if $$T$$ is open, but because it contains at least one of its boundary points, $$T$$ is not open.

---

Finally, consider the set $$S = \{z \in \mathbb C : \operatorname{Re}z > 1, \text{ and } \operatorname{Im}z > 2\}$$.

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/open-set.svg" | prepend: site.baseurl }}" alt="An open set for completeness sake">

This set is *open* because it does not contain *any* of its boundary points.

---

Now consider the set $$S = \{z \in \mathbb C : \operatorname{Im}z > 1\}$$ drawn below

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/domain.svg" | prepend: site.baseurl }}" alt="An example of a simple domain">

We ask ourselves a series of questions about $$S$$.

* Is it open? Yes. It contains none of its boundary points.
* Is it bounded? No. The set goes on forever in the positive $$y$$ direction and along the real axis.
* Is it connected? Yes. Every pair of points in $$S$$ can be joined by a polygonal line.
* Is it a domain? Yes, it's nonempty, open, and connected.

---

Now consider the region bounded by the inequality

$$\vert z - 4 \vert \geq \vert z \vert$$

Graphing certainly makes interpreting regions in the complex plane easier, so we work on simplifying the above inequality into something we can work with.

First, we use the definition of the modulus of complex numbers

$$\sqrt{(x - 4)^2 + y^2} \geq \sqrt{x^2 + y^2}$$

Since the modulus is by definition positive, we can square both sides without committing a mathematical sin

$$\begin{align*}
(x - 4)^2 + y^2 &\geq x^2 + y^2\\
(x - 4)^2 + \cancel{y^2} &\geq x^2 + \cancel{y^2}\\
x^2 - 8x + 16 &\geq x^2\\
\cancel{x^2} - 8x + 16 &\geq \cancel{x^2}\\
16 &\geq 8x\\
2 &\geq x\\
\end{align*}$$

In other words, we are dealing with the set $$S = \{z \in \mathbb C : \operatorname{Re}z \leq 2\}$$

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/region-1.svg" | prepend: site.baseurl }}" alt="An example of a simple region">

This set is closed, not open, not a domain, and not bounded.

---

What about $$\displaystyle S = \left\{z \in \mathbb C : z \neq 0, 0 \leq \operatorname{arg}z \leq \frac{\pi}{4}\right\}$$?

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/region-2.svg" | prepend: site.baseurl }}" alt="An example of a simple region">

This set is not open, not closed ($$z \not\in S$$), not a domain, not bounded, but is connected.

---

Now consider the region of the complex plane defined by the inequality $$\vert \operatorname{Re}z \vert < \vert z \vert$$. Using our brains (gasp) we might be able to convince ourselves that this inequality is true unless $$z \in \mathbb R$$. However, to make sure we perform the algebra.

$$\begin{align*}
\vert \operatorname{Re}z \vert &< \vert z \vert\\
\vert x \vert &< \sqrt{x^2 + y^2}\\
\vert x \vert^2 &< x^2 + y^2\\
\cancel{\vert x \vert^2} &< \cancel{x^2} + y^2\\
0 &< y^2\\
0 &< \pm y\\
\end{align*}$$

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/unbounded.svg" | prepend: site.baseurl }}" alt="An example of an unbounded set">

Another way of defining this region might be $$S = \left\{z \in \mathbb C : \operatorname{Im}z \neq 0\right\}$$. Note that $$\operatorname{Cl}(S) = \mathbb C$$

---

Consider the set $$\displaystyle{Z_n = \left\{\frac{i}{n} : n \in \mathbb N\right\}}$$ illustrated below

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/accumulation-example.svg" | prepend: site.baseurl }}" alt="accumulation point example">

Note that 0 is not contained in this set. We can get as close as we like to 0, but we can never quite get there. That means that 0 is a boundary point of $$Z_n$$.

Also note that every point is not an interior point, as any neighborhood of any point is not entirely contained in $$Z_n$$.

Let us now consider the deleted neighborhood of 0. No matter what $$\varepsilon$$ we pick, we can *always* find an element of $$Z_n$$ that is within the deleted neighborhood. This means that *every* deleted neighborhood of 0 contains at least one point of $$Z_n$$, so 0 is an accumulation point of $$Z_n$$. We can also see that 0 is the *only* accumulation point of $$Z_n$$, because no matter what point we pick, there will always be some distance between the point we pick and its neighbors that is not in $$Z_n$$.

Also note that 0 is $$Z_n$$'s only boundary point, so $$\operatorname{Cl}(Z_n) = \{Z_n, 0\}$$

---

Now consider the set $$Z_n = \{i^n : n \in \mathbb N\} = \{i, -1, i , 1\}$$ illustrated below.

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/accumulation-example-2.svg" | prepend: site.baseurl }}" alt="accumulation point example 2">

This set has *no* accumulation points.

---

Consider the set $$\displaystyle Z_n = \left\{\frac{i^n}{n} : n \in \mathbb N\right\}$$

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/accumulation-example-3.svg" | prepend: site.baseurl }}" alt="accumulation point example 3">

Note how the sequence spirals closer and closer to 0, but never actually hits it. It's very similar to the first accumulation point example. $$0 \not\in Z_n$$, but no matter what $$\varepsilon$$ we pick around 0, we can *always* find a point within that $$\varepsilon$$. Therefore 0 is an accumulation point, and is actually the *only* accumulation point of this set.

---

Lastly, consider the set

$$\displaystyle Z_n = \left\{(-1)^n(1 + i)\frac{n - 1}{n} : n \in \mathbb N\right\} = \left\{-0,\, \frac{1}{2}(1 + i),\, \frac{-2}{3}(1 + i),\, \frac{3}{4}(1 + i),\, \frac{-4}{5}(1 + i),\, \dots\right\}$$

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/accumulation-example-4.svg" | prepend: site.baseurl }}" alt="accumulation point example 4">

$$1 + i$$ and $$-(1 + i)$$ are the only accumulation points of $$Z_n$$, but are *not in* $$Z_n$$.

Also note that for a little bit of intuition, points *accumulate* at the *accumulation* points -- though not necessarily from one direction.
