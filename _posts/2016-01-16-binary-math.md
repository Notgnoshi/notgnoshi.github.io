---
layout: post
title: 03 Binary Math
category: finite
---

We can represent **AND**, **OR**, and **NOT** using algebraic addition, negation, and multiplication.

We represent $$A$$ **AND** $$B$$ simply as $$AB$$.

We represent $$A$$ **OR** $$B$$ as $$A + B$$.

**NOT** $$A$$ is typically denoted by $$\overline{A}$$ in the context of **Boolean Algebra**.

Using this notation, we can rewrite some logical statement $$A \land B \lor \neg C$$ as $$AB + \overline{C}$$ (keeping in mind operator precedence), or $$\neg (A \lor B) \land C$$ as $$(\overline{A + B})C$$. We can easily evaluate these expressions with the following rules.

$$1 \cdot 1 = 1$$

$$1 \cdot 0 = 0$$

$$0 \cdot 1 = 0$$

$$0 \cdot 0 = 0$$

These multiplication rules intuitively make sense, $$0$$ multiplied with anything is $$0$$. However, the binary addition isn't quite as nice.

$$1 + 1 = 1$$

$$1 + 0 = 1$$

$$0 + 1 = 1$$

$$0 + 0 = 0$$

In **base 2** math, $$1 + 1 = 10$$, but I have it listed above as $$1$$. That isn't a mistake. You might try to justify it by saying $$1 + 1 = 10$$ and $$1 + 0 = 1$$, but that leaves much to be desired. I'll just say that in the context of Boolean Algebra, $$1 + 1$$ is *defined* to be $$1$$.

So given some expression and a set of input values of the individual component propositions, we can easily determine the output truth value of the entire compound proposition for those input values.
