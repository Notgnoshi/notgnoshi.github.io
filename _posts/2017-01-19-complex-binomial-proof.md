---
layout: post
title: Proof of the Complex Binomial Formula
meta: A proof the the binomial formula for complex numbers as presented in my Complex Analysis class
redirect_to: https://agill.xyz/blog/proof-of-the-complex-binomial-formula
---

This is a presentation of the proof for the binomial formula for complex numbers. The intent is to provide a clear example of an inductive proof.

**Thm.** Let $$z_1, z_2 \in \mathbb C$$ and $$n \in \mathbb N$$. Then

$$(z_1 + z_2)^n = \sum_{k=0}^n \binom{n}{k}z_1^k z_2^{n-k}$$

**Pf.** By induction on $$n$$.

* Base Case: ($$n = 1$$)

    $$\begin{align*}
    \sum_{k = 0}^1 \binom{1}{k} z_1^k z_2^{1 - k} &\stackrel{?}{=} (z_1 + z_2)^1\\
    \underbrace{\binom{1}{0} z_1^0 z_2^{1-0}}_{k = 0} + \underbrace{\binom{1}{1} z_1^1 z_2^{1 - 1}}_{k = 1} &\stackrel{?}{=} z_1 + z_2\\
    1 \cdot 1 \cdot z_2 + z \cdot z_1 \cdot 1 &\stackrel{?}{=} z_1 + z_2\\
    z_2 + z_1 &\stackrel{\checkmark}{=} z_1 + z_2\\
    \end{align*}$$

    Thus the base case is true.

* Assume the statement is true for $$n$$, we wish to show that the statement is true for $$n + 1$$.

    Consider $$(z_1 + z_2)^{n + 1}$$, we wish to show that $$\displaystyle{(z_1 + z_2)^{n + 1} = \sum_{k = 0}^{n + 1} \binom{n + 1}{k}z_1^k z_2^{n + 1 - k}}$$.

    $$(z_1 + z_2)^{n + 1} = (z_1 + z_2) \cdot (z_1 + z_2)^n$$

    $$(z_1 + z_2)^{n + 1} = (z_1 + z_2) \cdot \left(\sum_{k = 0}^n \binom{n}{k} z_1^k z_2^{n - k}\right)$$

    Multiplying $$(z_1 + z_2)$$ through the sum we get

    $$\sum_{k = 0}^n \binom{n}{k} z_1 ^{k + 1} z_2^{n - k} + \sum_{k = 0}^n \binom{n}{k} z_1^k z_2^{n + 1 - k}$$

    We reindex the first summation $$k \to j - 1$$. Note that $$k = j - 1$$ and $$ k + 1 = j$$.

    $$\sum_{j = 1}^{n + 1} \binom{n}{j - 1} z_1^j z_2^{n + 1 - j} + \sum_{k = 0}^n \binom{n}{k} z_1^k z_2^{n + 1 - k}$$

    We split off the first term of the last summation and the last term of the first summation.

    $$\underbrace{\binom{n}{n} z_1^{n + 1} z_2^0}_{j = n+1} + \sum_{k = 1}^n \left[\binom{n}{k - 1} + \binom{n}{k}\right] z_1^k z_2^{n + 1 - k} + \underbrace{\binom{n}{0} z_1^0 z_2^{n + 1}}_{k = 0}$$

    Note that $$\binom{n}{k - 1} + \binom{n}{k} = \binom{n + 1}{k}$$. This is proved as a lemma later. We then have

    $$1 \cdot z^{n + 1} \cdot z_2^0 + \sum_{k = 1}^n \binom{n + 1}{k} z_1^k z_2^{n + 1 - k} + 1 \cdot z_1^0 \cdot z_2^{n + 1}$$

    Noting that $$\binom{n}{n} = 1$$ and $$\binom{n}{0} = 1$$ we have

    $$\underbrace{\binom{n + 1}{n + 1} \cdot z^{n + 1} \cdot z_2^0}_{\text{$k = n+1$ term}} + \sum_{k = 1}^n \binom{n + 1}{k} z_1^k z_2^{n + 1 - k} + \underbrace{\binom{n + 1}{0} \cdot z_1^0 \cdot z_2^{n + 1}}_{\text{$k = 0$ term}}$$

    We then have the following

    $$\sum_{k = 0}^{n + 1} \binom{n + 1}{k}z_1^k z_2^{n + 1 - k}$$

    Which is precisely what we wanted to show $$(z_1 + z_2)^{n + 1}$$ is equal to. Therefore, the statement is true for $$n + 1$$ and thus for all $$n$$.

---

**Lemma.** $$\displaystyle{\binom{n + 1}{k} = \binom{n}{k} + \binom{n}{k - 1}}$$

**Pf.** Label one of the $$n + 1$$ objects as $$*$$. We can either choose $$*$$ as one of our $$k$$ objects or not. These are two distinct and disjoint cases, and are all that are possible.

* If we choose $$*$$, we are left to choose $$k - 1$$ objects from $$n$$ objects. This can be done in $$\binom{n}{k - 1}$$ ways.

* If we don't choose $$*$$, then we are left to choose $$k$$ objects from $$n$$ objects. This can be done $$\binom{n}{k}$$ ways.

Therefore, $$\displaystyle{\binom{n + 1}{k} = \binom{n}{k} + \binom{n}{k - 1}}$$.

---

Note this lemma could be proved using the definition of $$\binom{n}{k} = \frac{n!}{k!(n - k!)}$$, but would require more algebra than is pleasant.

Also note that this proof of the binomial formula for complex numbers exemplifies the three parts of an induction proof:

* Prove the base case is true.
* Assume the statement is true for $$n$$.
* Show that it follows the statement is also true for $$n + 1$$.

These three parts together show that the statement is true for all $$n$$.

It's also a good idea in proof-writing to be extremely clear both in what proof method you're using and which part of the proof you're currently working on.
