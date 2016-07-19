---
layout: post
title: Geometry
subtitle: Preliminary notes
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

I picked up a [book](https://amzn.com/0486658120) on geometry a while ago. These are my notes as I work through reading it.

### The Euclidean Plane

This is the "normal" familiar plane of ordinary geometry. We study the Euclidean plane algebraically, and describe it in terms of real numbers. We use two properties of real numbers:

* They form a [field](https://en.wikipedia.org/wiki/Field_(mathematics))
* They are ordered

---

**Points** on the Euclidean plane are given by ordered pairs of real numbers $$(x_1, x_2)$$. The distance between two points (called the Euclidean [norm](https://en.wikipedia.org/wiki/Norm_(mathematics))) $$P = (x_1, x_2)$$ and $$Q = (y_1, y_2)$$ is given by the usual

$$\operatorname{d}(P, Q) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$$

Note that it does not matter in which order you apply to function to the points $$P$$ and $$Q$$; both $$\operatorname{d}(P, Q)$$ and $$\operatorname{d}(Q, P)$$ are the same.

---

**Lines** on the Euclidean plane are sets of points that satisfy equations of the form

$$ax + by + c = 0$$

or equivalently $$y = mx + b$$; found by solving for $$y$$ in the above equation.

We can construct a coordinate system on any given line in $$\mathbb{R}^2$$ so that for any two points $$A$$ and $$B$$, with coordinates $$x_A$$ and $$x_B$$ respectively, then

$$|x_B - x_A | = \operatorname{d}(A, B)$$

This means that if we set up a 1-dimensional coordinate system on any line in $$\mathbb{R}^2$$, the distance between any two points on that line can be easily calculated by ignoring the 2-dimensional aspect of the two points and taking the difference of the point's coordinates in the line's new 1-dimensional coordinate system.

---

The points $$A$$ and $$C$$, together with all points $$B$$ between $$A$$ and $$C$$ form the *segment* $$AC$$.

A point $$B$$ is *between* points $$A$$ and $$C$$, where $$A \neq C$$ if

$$\operatorname{d}(A, B) + \operatorname{d}(B, C) = \operatorname{d}(A, C)$$

Not that this implies a point $$B$$ can only be between the points $$A$$ and $$C$$ if it lies on the segment $$AC$$.

If $$A$$, $$B$$, and $$C$$ are three distinct points, the three segments $$AB$$, $$BC$$, and $$CA$$ form a *triangle* $$ABC$$ with *sides* $$AB$$, $$BC$$, and $$CA$$ with the *vertices* $$A$$, $$B$$, and $$C$$. If $$A$$, $$B$$, and $$C$$ are on the same line, the triangle is called *degenerate*. Otherwise it is a *proper* triangle.

If $$ABC$$ is a proper triangle, the sum of the lengths of any two sides is always greater than the length of the third. This is called the *triangle inequality*. We can generalize this to any three points $$A$$, $$B$$, and $$C$$ to

$$\operatorname{d}(A, B) + \operatorname{d}(B, C) \geq \operatorname{d}(A, C)$$

with equality holding *if and only if* the point $$B$$ lies on the segment $$AC$$.

An *angle* is formed by three ordered points $$A$$, $$O$$, and $$B$$, where $$A \neq O$$ and $$B \neq O$$. The point $$O$$ is the *vertex* of the angle. The segments $$m = OA$$ and $$n = OB$$, through any point $$O$$ can be put into 1-to-1 correspondence with the real numbers such that if $$a_m$$ corresponds to $$m$$ and $$a_n$$ to $$n$$, then the *measure* of $$AOB$$, denoted $$\sphericalangle AOB$$ is $$a_n - a_m$$ (mod $$2 \pi$$). Intuition-wise, this distance $$a_n - a_m$$ is equivalent to the length of the arc from $$a_n$$ to $$a_m$$.

<img class="centered" src="{{ "/assets/posts/geometry/angles/angles.svg" | prepend: site.baseurl }}" alt="Definition of an angle">

Note that with this definition, $$\sphericalangle AOB \neq \sphericalangle BOA$$ and that $$\sphericalangle AOB = - \sphericalangle BOA$$. We call these angles *sensed*, *oriented*, or *signed* angles.

In Euclidean geometry, for any triangle $$ABC$$

$$\sphericalangle BCA + \sphericalangle CAB + \sphericalangle ABC = \pi (\operatorname{mod} 2\pi)$$

---

Triangles $$ABC$$ and $$A'B'C'$$ are called *similar* if for some constant $$k > 0$$

$$\operatorname{d}(A', B') = k \operatorname{d}(A, B), \quad \operatorname{d}(B', C') = k \operatorname{d}(B, C), \quad \operatorname{d}(C', A') = k \operatorname{d}(C, A)$$

If, in two triangles $$ABC$$ and $$A'B'C'$$, we have $$\operatorname{d}(A', B') = k \operatorname{d}(A, B)$$, $$\operatorname{d}(A', C') = k \operatorname{d}(A, C)$$, and $$\sphericalangle B'A'C' = \pm \sphericalangle BAC$$, then the triangles are similar (SAS). If $$k = 1$$, the triangles are *congruent*.

---

A point $$O$$ on a line $$\ell$$ is the vertex of two *rays*. We can assign positive coordinates to one half of the line, and negative coordinates to the other half, with $$O$$ as the origin. If $$A$$ and $$B$$ are any two points on $$\ell$$, we can define the directed segment $$AB$$ as $$\overline{AB} = x_B - x_A$$. Then we have $$\overline{AB} = - \overline{BA}$$. (In a sense, $$\overline{AB}$$ is the magnitude of $$AB$$).

If $$A$$, $$B$$, and $$P$$ are distinct points on $$\ell$$ (called *collinear* points), we can define the ration that $$P$$ divides the segment $$AB$$ to be $$\frac{\overline{AP}}{\overline{PB}}$$. This ratio does not depend on where you choose your origin $$O$$, and does not depend on which half of the line has positive coordinates, and which has negative.

Let $$r = \frac{\overline{AP}}{\overline{PB}}$$. If $$P$$ lies between $$A$$ and $$B$$, the division is *internal* and $$r > 0$$, otherwise the division is *external* and $$r < 0$$. If $$P$$ lies on the ray from $$B$$ in the direction of $$A$$, then $$-1 < r < 0$$; if $$P$$ lies between $$A$$ and $$B$$ then $$0 < r < \infty$$. If $$P$$ lies on the ray from $$A$$ in the direction of $$B$$, then $$- \infty < r < -1$$. (This all has to do with the magnitudes of the numerator and denominator).

For any given $$r$$ between $$-\infty$$ and $$\infty$$, the point $$P$$ is uniquely defines, so there is a 1-to-1 correspondence between the position of $$P$$ on the line and the real numbers.

---

In Euclidean plane geometry, two distinct points determine a unique line, two lines intersect at a single unique point or not at all; in which case they are *parallel*. Through any point not on a line, there is exactly one line parallel to the given line.

An *ideal* point $$\mathscr{P}$$ is the *set of lines parallel to a given line*. We say that $$\mathscr{P}$$ lies on a given line $$l$$ if and only if $$l$$ is a member of the set of parallel lines that define $$\mathscr{P}$$.

If $$Q$$ is an ordinary point, then there is a unique line that contains both $$Q$$ and $$\mathscr{P}$$, since there is now a unique parallel through $$Q$$ to the lines defining $$\mathscr{P}$$. This implies that two lines *always* intersect, either at an ordinary point, or at an ideal point. We call the set of ideal points *the line at infinity*.

---

The area of a triangle $$ABC$$ is given by the determinant

$$\frac{1}{2}\left| \begin{array}{ccc} x_1 & x_2 & 1 \\ y_1 & y_2 & 1 \\ z_1 & z_2 & 1 \end{array}\right|$$

where $$A = (x_1, x_2)$$, $$B = (y_1, y_2)$$, and $$C = (z_1, z_2)$$. If the triangle is a right triangle, we can dispense with the determinant and use the familiar formula $$\alpha = \frac{1}{2}bh$$ where $$b$$ is the length of the base and $$h$$ is the length of the upright with the triangle oriented appropriately. This determinant is positive if the rotation from the $$x$$ axis to the $$y$$ axis is counterclockwise, and negative otherwise. This allows us to compare the orientation of triangles.

### The [affine plane](https://en.wikipedia.org/wiki/Affine_plane_(incidence_geometry))

We can consider a plane in which the points are ordered pairs of real numbers $$(x, y)$$, and the line joining two points $$P = (x_1, y_1)$$ and $$Q = (x_2, y_2)$$ is defined by the set of points $$R$$ given by

$$R = \left\{ \frac{k_2 x_1 + k_1 x_2}{k_1 + k_2}, \quad \frac{k_2 y_1 + k_1 y_2}{k_1 + k_2} \right\}$$

where $$k_1$$ and $$k_2$$ vary over all real values with $$k_1 \neq -k_2$$. We find that the coordinates $$(x, y)$$ of $$R$$ satisfy a linear equation of the form

$$ax + by + c = 0$$

If we take the values $$(0, 1)$$ and $$(1, 0)$$ of $$9k_1, k_2$$, we find that the set $$R$$ contains both $$P$$ and $$Q$$, and we can call that line *the line $$PQ$$*

There is no general formula for the distances between points under this definition.

The two lines $$ax + by + c = 0$$ and $$ax + by + d$$ with $$c \neq d$$ have *no* point of intersection, and are parallel.

### Complex numbers

We can associate every point $$(a, b)$$ in the Euclidean plane with a complex number $$a + bi$$ where $$i^2 = -1$$.

We can also use complex numbers as ordered pairs $$(a, b)$$ of real numbers with $$a$$ as the real part, and $$b$$ as the imaginary part of the complex number. We say two complex numbers $$(a, b)$$ and $$(c, d)$$ are equal if and only if $$a = c$$ and $$b = d$$. We define addition as

$$(a, b) + (c, d) = (a + c, b + d)$$

and scalar multiplication with a real $$k$$ as

$$k(a, b) = (ka, kb)$$

We define the multiplication of two complex numbers as

$$(a, b) \cdot (c, d) = (ac - bd, ad + bc)$$

---

With these rules, we can begin to examine the usual laws of algebra (associativity, commutativity, etc.). The obvious zero element is $$(0, 0)$$ giving

$$(a, b) + (0, 0) = (a, b)$$

and

$$(a, b) \cdot (0, 0) = (0, 0)$$

If we define $$-(a, b)$$ as $$(-a, -b)$$, we have

$$(a, b ) - (a, b) = (0, 0)$$

If $$(a, b) \neq (0, 0)$$, we can find an *inverse*, or, a number $$(c, d)$$ such that $$(a, b) \cdot (c, d) = (1, 0)$$. We use $$(1, 0)$$ as out identity element because $$(a, b) \cdot (1, 0) = (a, b)$$. The inverse of $$(a, b)$$ is given by

$$\left(\frac{a}{a^2 + b^2}, \quad \frac{-b}{a^2 + b^2}\right)$$

If we consider complex numbers with an imaginary part of 0, we can see that $$(a, 0)$$ is isomorphic to $$a$$. We therefore consider the complex numbers an extension of the field of real numbers.

### [Argand diagrams](https://en.wikipedia.org/wiki/Complex_plane)

If we consider complex numbers to be ordered pairs of real numbers, it makes sense to represent complex numbers as points in $$\mathbb{R}^2$$. This representation is known as an *Argand diagram*.

We often use a single symbol $$z$$ to represent a complex number $$(a, b)$$ with $$z = a + bi = (a, b)$$. We can plot $$z$$ 's Argand diagram like so

<img class="centered" src="{{ "/assets/posts/geometry/argand/argand.svg" | prepend: site.baseurl }}" alt="Argand diagram">

We use the notation $$\mid z \mid$$ to denote the magnitude of the vector from the origin to the point $$(a, b)$$ defined by $$z$$. In this way, we can think of complex numbers as vectors.

---

If $$z = a + bi$$, we define the *complex conjugate* of $$z$$, written as $$\bar z$$ as

$$\bar z = a - bi$$

Intuitively speaking, $$\bar z$$ is the reflection of $$z$$ about the $$x$$ axis. It is clear then, that $$\overline{\overline{z}} = a + bi = z$$.

We can also see that

$$\overline{(z_1 + z_2)} = \overline{z_1} + \overline{z_2}$$

and

$$\overline{(z_1 \cdot z_2)} = \overline{z_1} \cdot \overline{z_2}$$

Note that

$$z \cdot \overline{z} = (a + bi)(a - bi) = a^2 - i^2 b^2 = a^2 + b^2$$

which is the square of the distance from the origin to the point $$(a, b)$$. We then define the magnitude of $$z$$, written as $$\mid z \mid$$ to be $$\sqrt{a^2 + b^2}$$, so we have that

$$z \cdot \overline{z} = \mid z \mid ^2$$


Since we have that

$$\mid z_1 \cdot z_2 \mid ^2 = (z_1\cdot z_2) \overline{(z_1 \cdot z_2)} = (z_1 \cdot z_1)(\overline{z_1}) (\overline{z_2}) = (z_1 \cdot \overline{z_1})(z_2 \cdot \overline{z_2}) = \mid z_1 \mid ^2 \mid z_2 \mid ^2$$

we arrive at the relation

$$\mid z_1 \cdot z_2 \mid = \mid z_1 \mid \mid z_2 \mid$$

Note that $$\mid z \mid > 0$$ if $$z \neq (0, 0)$$. We can therefore find the inverse of a complex number easily:

$$z ^{-1} = \frac{\overline{z}}{\mid z \mid ^2} = \frac{a}{a^2 + b^2} - \frac{ib}{a^2 + b^2}$$

### The triangle inequality with complex numbers

We have the basic inequality

$$\mid z_1 + z_2 \mid \ \leq \ \mid z_1 \mid + \mid z_2 \mid$$

which can be written as

$$\mid z_2 \mid \ \geq \ \mid z_1 + z_2 \mid - \mid z_1 \mid$$

which can be written as

$$\mid z_1 + z_2 - z_1 \mid \ \geq \ \mid z_1 + z_2 \mid - \mid z_1 \mid$$

If we rename our complex numbers, we can achieve some trickery. Let $$p = z_1 + z_2$$ and $$q = z_1$$. Then we have

$$\mid p - q \mid \ \geq \ \mid p \mid - \mid q \mid$$

Since $$\mid p - q \mid = \mid q - p \mid$$ we also must necessarily have

$$\mid p - q \mid \ \geq \ \mid q \mid - \mid p \mid$$

All of this information together can be assimilated into the inequality

$$\mid p - q \mid \ \geq \ \mid \mid p \mid - \mid q \mid \mid$$

Remember that if $$z_1 = (a, b)$$ and $$z_2 = (c, d)$$, then the distance between the points $$(a, b)$$ and $$(c, d)$$ is simply $$\mid z_2 - z_1 \mid$$.

### De Moivre's theorem

Above, when I discussed the Argand diagram, I stated that it was natural to interpret complex numbers as vectors. We can represent vectors in polar coordinates. Let $$z = a + bi$$, and let the length of $$z$$ be denoted by $$r$$. Then if the vector from the origin to the point $$(a, b)$$ makes the angle $$\phi$$ with the positive $$x$$ axis, we have

$$a = r \cos \phi$$

and

$$b = r \sin \phi$$

such that

$$z = a + bi = r (\cos \phi + i \sin \phi)$$

<img class="centered" src="{{ "/assets/posts/geometry/polar/polar.svg" | prepend: site.baseurl }}" alt="polar coordinates">
