---
layout: post
title: Supremum, Infimum, Minimum, and Maximum
subtitle: A mum's tale
meta: An explanation of the differences between the supremum, infimum, minimum, and maximum of sets.
---

## Definitions:

---

Let $$S \subseteq \mathbb R$$, and $$m, m_0, M, M_0, \hat m, \hat M \in \mathbb R$$. These definitions may also work on sets besides $$\mathbb R$$, as long as there is some sense of size on such sets.

* If every $$x \in S$$ satisfies $$x \leq M$$, we say $$M$$ is an **upper bound** of $$S$$.
* If every $$x \in S$$ satisfies $$x \geq m$$, we say $$m$$ is a **lower bound** of $$S$$.

Note that upper and lower bounds are non-unique.

* We say $$M_0$$ is a **least upper bound** of $$S$$ if:
    - $$M_0$$ is an upper bound of $$S$$
    - If $$M$$ is any upper bound of $$S$$, we have $$M_0 \leq M$$
* We say $$m_0$$ is the **greatest lower bound** of $$S$$ if:
    - $$m_0$$ is a lower bound of $$S$$
    - If $$m$$ is any lower bound of $$S$$, we have $$m_0 \geq m$$

The least upper bound may be written $$\operatorname{lub}(S)$$, and is most often called the **supremum** of $$S$$, written as $$\sup(S)$$. Likwise, the greatest lower bound may be written $$\operatorname{glb}(S)$$, and is most often caleld the **infimum** of $$S$$, written as $$\inf(s)$$.

It is tempting to call the supremum of a set the set's maximum value, and the infimum the set's minimum value. *This is incorrect.*

* We call $$\hat M$$ the **maximum** of $$S$$ if:
    - $$\hat M \in S$$.
    - $$\forall x \in S: x \leq \hat M$$.
* We call $$\hat m$$ the **minimum** of $$S$$ if:
    - $$\hat m \in S$$.
    - $$\forall x \in S: x \geq \hat m$$.

There is no requirement for the supremum and infimum to be a part of $$S$$, but the maximum and minimum *must* be a part of $$S$$.

* We say $$S$$ is **bounded** if $$S$$ has both an upper and lower bound.

## Examples

---

I think these ideas are best understood with graphical examples, so consider the set

$$\displaystyle S = \left\{ \frac{1}{n} \mid n \in \mathbb N \right\}$$

pictured below:

<img class="centered" src="{{ "/assets/posts/sup-inf-max-min/example1.svg" | prepend: site.baseurl }}" alt="1 / n">

Note that this set contains $$1$$, but not $$0$$.
* Does this set have an upper bound?
    - Yes! This set is *bounded above* by any number 1 or higher.
* Does this set have a lower bound?
    - Yes! This set is *bounded below* by any number 0 or lower.
* Does this set have a supremum, and if so, what is it?
    - Yes! The least upper bound for this set is $$1$$.
    - $$\sup(S) = 1$$.
* Does this set have an infimum, and if so, what is it?
    - Yes! The greatest lower bound for this set is $$0$$.
    - $$\inf(S) = 0$$.
* Does this set have a maximum, and if so, what is it?
    - Yes! The maximum for this set is $$1$$.
    - $$\max(S) = 1$$.
* Does this set have a minimum, and if so, what is it?
    - No! *This set does not have a minimum value!* No matter how close of a number you pick to $$0$$, there will always be a smaller number to pick! This is an important concept in set theory and real analysis.
    - $$\min(S) =$$<img class="inline" src="{{ "/assets/skull.svg" | prepend: site.baseurl }}" alt="death">
* Is this set bounded?
    - Yes! It is bounded above and bounded below.

---

Now consider the set $$\displaystyle S = \mathbb Q \cap [-\pi, \pi]$$, which can be read as the rational numbers between $$-\pi$$ and $$\pi$$. Answer the following questions:

* Is the set bounded above? Below?
* Does the set have a supremum? Infimum?
* Does the set have a minimum? Maximum?
