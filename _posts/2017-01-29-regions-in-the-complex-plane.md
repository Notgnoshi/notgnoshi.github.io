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

Consider the set $$\displaystyle{Z_n = \left\{\frac{i}{n} : n \in \mathbb N\right\}}$$ illustrated below

<img class="centered" src="{{ "/assets/posts/regions-in-the-complex-plane/accumulation-example.svg" | prepend: site.baseurl }}" alt="accumulation point example">

Note that 0 is not contained in this set. We can get as close as we like to 0, but we can never quite get there. That means that 0 is a boundary point of $$Z_n$$.

Also note that every point is not an interior point, as any neighborhood of any point is not entirely contained in $$Z_n$$.

Let us now consider the deleted neighborhood of 0. No matter what $$\varepsilon$$ we pick, we can *always* find an element of $$Z_n$$ that is within the deleted neighborhood. This means that *every* deleted neighborhood of 0 contains at least one point of $$Z_n$$, so 0 is an accumulation point of $$Z_n$$. We can also see that 0 is the *only* accumulation point of $$Z_n$$, because no matter what point we pick, there will always be some distance between the point we pick and its neighbors that is not in $$Z_n$$.

Also note that 0 is $$Z_n$$'s only boundary point, so $$\operatorname{Cl}(Z_n) = \{Z_n, 0\}$$
