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

<img class="centered" src="{{ "/assets/posts/geometry/angles/angles.svg" | prepend: site.baseurl }}" alt="number line holes">

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

### The affine plane

We can consider a plane in which the points are ordered pairs of real numbers $$(x, y)$$, and the line joining two points $$P = (x_1, y_1)$$ and $$Q = (x_2, y_2)$$ is defined by the set of points $$R$$ given by

$$R = \left\{ \frac{k_2 x_1 + k_1 x_2}{k_1 + k_2}, \quad \frac{k_2 y_1 + k_1 y_2}{k_1 + k_2} \right\}$$

where $$k_1$$ and $$k_2$$ vary over all real values with $$k_1 \neq -k_2$$. We find that the coordinates $$(x, y)$$ of $$R$$ satisfy a linear equation of the form

$$ax + by + c = 0$$

If we take the values $$(0, 1)$$ and $$(1, 0)$$ of $$9k_1, k_2$$, we find that the set $$R$$ contains both $$P$$ and $$Q$$, and we can call that line *the line $$PQ$$*

There is no general formula for the distances between points under this definition
