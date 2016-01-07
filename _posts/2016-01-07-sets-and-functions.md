---
layout: post
title: Sets and Functions
---

Sometime in early high school the concept of a function was first introduced. It might have even been earlier than that. However, not even having a lot of higher math I can say that there's a bit more to functions than what was introduced in Pre-Algebra. What I'd like to do here is introduce the idea of functions using [sets](https://en.wikipedia.org/wiki/Set_(mathematics)), but in order to do that, I have to first talk a little bit about sets.

---

The idea of a set is a very elementary concept in mathematics. Often I think that a set is one of the undefined terms in mathematics. In a word, a set is a collection of objects, but a set is an object in and of itself, so one could conceivably have a set of sets. The objects should be distinct and well-defined. Oftentimes there is a rule that defines what items are considered **elements** of a set, and other times a set is defined by listing all of the elements in a set. For example, $$\mathbb{R}$$ is defined as the set of all real numbers, which would take a while to list.

We typically use capital letters to represent sets, and lowercase letters to represent members of a set. The statement $$x \in A$$ means $$x$$ is a member, or an element of $$A$$. The statement $$x \not\in A$$ is read "$$x$$ is is not an element of $$A$$."

A set can be defined by listing its elements if it contains a finite number of them. For example, if $$P$$ is the set of the first five prime numbers, we say $$P = \{3, 5, 7, 11, 13 \}$$. Otherwise, some kind of rule must be given to define a set, such as the set $$\mathbb{R}$$ already mentioned above. We would explicitly define $$\mathbb{R}$$ as follows

$$\mathbb{R} = \{x \mid x \text{ is a real number}\}$$

We read this as "$$\mathbb{R}$$ is the set of all $$x$$ such that $$x$$ is a real number."

---

Recall from above that the $$\in$$ means that an *element* is a member of a specified set, but what about subsets? We use the notation $$A \subset B$$ to mean $$A$$ is a *subset* of $$B$$. This means if ever member of a set $$A$$ is also a member of a set $$B$$, then $$A$$ is called a **subset** of $$B$$, and we write $$A \subset B$$. Note that every set is a subset of itself, i.e. the set of integers is a subset of the set of integers.

Consider for a moment all subsets of a given set $$U$$ (called the universal set). Included in $$U$$ are the set $$U$$ itself, and the **empty set** $$\emptyset$$, which is defined as the set that contains to members.

---

Two subsets $$X$$ and $$Y$$ are considered equal if and only if they contain identically the same elements. In other words, $$X = Y$$ if $$X \subset Y$$ and $$Y \subset X$$.

We define two set operations (there are many more, but I'll only give a few here) **union** and **intersection** of two subsets. $$X \cup Y$$ is read $$X$$ union $$Y$$, and $$X \cap Y$$ is read $$X$$ intersects $$Y$$, and are defined respectively as follows

$$ X \cup Y = \{ \text{set of all elements that belong to $X$ or $Y$ or both} \} $$

$$ X \cap Y = \{ \text{set of all elements that belong to both $X$ and $Y$} \}$$

These operations are similar to $$\text{AND}$$ and $$\text{OR}$$ from boolean algebra, where $$\text{OR}$$ is non-exclusive.

A third set operation $$\sim A$$ is called the **complement** of $$A$$. If $$A \subset U$$, then the set $$\sim A$$ consists of all elements of $$U$$ not contained in $$A$$. From this definition we can glean the following properties.

$$A \cup \left( \sim A \right) = U$$

$$A \cap \left( \sim A \right) = \emptyset$$

$$ \sim \left( \sim A \right) = A$$

---

There are a number of properties these operations have that are quite similar to the rules of addition and multiplication learned in grade school.

There are the **Commutative Laws**

$$A \cup B = B \cup A$$

$$A \cap B = B \cap A$$

The **Associative Laws**

$$( A \cup B ) \cup C = A \cup ( B \cup C) $$

$$( A \cap B ) \cap C = A \cap ( B \cap C) $$

The **Distributive Law**

$$ A \cap ( B \cup C ) = (A \cap B ) \cup (A \cap C) $$

And the **Identity Laws**

$$A \cup \emptyset = A$$

$$A \cap U = A$$

$$ A \cup U = U $$

$$ A \cap \emptyset = \emptyset $$

It is possible to use these laws to prove [DeMorgan's laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws), which are very important in boolean algebra.

$$ \sim ( A \cup B ) = (\sim A) \cap (\sim B)$$

$$ \sim ( A \cap B ) = (\sim A) \cup (\sim B) $$

---

The usage of *variables* comes up extremely often in mathematics. A **variable** is an alphabetic character (the *name* of the variable) that represents some arbitrary value, called the **value** of the variable which can be known or unknown.

The **scope** of a variable is the set of all values a variable can take on. For example, if we say "let $$x$$ be an arbitrary real number" the scope of $$x$$ is the set of real numbers.

A variable whose scope is a set consisting of exactly one element is called a **constant**.

---

Now to get on to the meat of the matter: functions. A function is one of the most far-reaching and important ideas in mathematics. The idea is an abstraction of the many familiar situations in which two changing quantities are related by some kind of rule. If one value is given, we can determine the second. In this way, we can consider a function to be a rule to map one value to another.

In terms of sets let's now work on a definition.

Let $$A$$ and $$B$$ be sets. Suppose there is a rule that associates with each element of $$A$$ a member of $$B$$, and each member of $$B$$ is associated by this rule with at least one member of $$A$$. These two sets together with the rule of association comprise a **function**.

The set $$A$$ is called the **domain** of the function, and the set $$B$$ is called the **range** of the function.

A symbol whose scope is the domain of the function is called an **independent variable**; a symbol whose scope is the range of a function is called a **dependent variable**.

Note that if the domain and the rule are given, then we can determine the range of a function. Often, we call just the rule a function, but a function is not completely defined unless the domain is either explicitly or implicitly specified.

A function is typically denoted (or named) by a single letter such as $$f, g, F,$$ etc. If the letter $$f$$ represents the name of a definite function, then $$f(x)$$ represents the element in the range associated with the element $$x$$ in the domain. The statement $$f(x) = x^2$$ would be the **definition** of $$f$$, and $$f(a)$$ is called the **value** of $$f$$ at $$a$$.

Note that a function with assign each element in the domain a single unique element in the range. But a given element in the range of a function may be the value corresponding to more than one element in the domain. When each element in the range is a value of the function corresponding to *only one* element in the domain, the correspondence is called **one-to-one**.

---

There is one last piece of notation that I want to introduce. The notation $$ f : A \to B $$ comes up frequently in higher mathematics.

 If we say $$ f : A \to B $$, we say that $$f$$ is a function from $$A$$ to $$B$$. We call $$A$$ the **domain** and $$B$$ the **codomain** of $$f$$. This symbolism means that for all $$ x \in A$$, there is an $$f(x) \in B$$. In simple terms for example, $$ f : \mathbb{R} \to \mathbb{R} $$ means that for every real input to $$f$$ there is a real output.

---

There are many directions one can go with functions. A particularly useful one would be to graphically represent the values a function takes on over its domain, but I think we've all had enough experience with graphs of functions that I don't feel the need to write any more about it. Anyways, I think this is a pretty good length for a post.
