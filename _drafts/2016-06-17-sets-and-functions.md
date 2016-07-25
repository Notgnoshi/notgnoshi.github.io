---
layout: post
title: Sets and Functions
subtitle: A brief reminder
meta: A list of properties of sets and functions to serve as a quick reference for me in the future
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/images.css" | prepend: site.baseurl }}">

Sometime in early high school (or even earlier, I can't remember) the idea of sets and functions was introduced. What I'd like to do is give myself a reminder of the basic set and function definitions and operations that I've learned since then.

---

Oddly, the idea of a set (also the epsilon-relation $$\epsilon (a, A)$$, often written as $$a \in A$$, which we take to mean "$$a$$ is an element of $$A$$") is one of the undefined concepts in mathematics despite being one of its most fundamental ideas. Rather, they just *appear* through the use of the [Zermelo-Fraenkel](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) axioms. I'm not going to go through all the axioms, but they're quite interesting. Watch the following video (and I'd recommend the whole playlist) if you're interested.

<iframe class="centered" width="560" height="315" src="https://www.youtube.com/embed/AAJB9l-HAZs?list=PLPH7f_7ZlzxTi6kS4vCmv4ZKm9u8g5yic" frameborder="0" allowfullscreen></iframe>

Informally, a set is a collection of objects, but note that a set is an object in and of itself, so one could conceivably have a set of sets. We can get into some danger here, if we allow sets to contain other sets, especially if we try really hard to create *paradoxes*. The above video goes into more detail on this. The objects that make the **elements** of a set should be distinct and well-defined. Often there is a *rule* that defines what items are considered elements and what items are not, and other times a set is defined by listing every single element of a set. For infinitely large sets, like $$\mathbb{R}$$, listing every single element would take a while, so we define it by some kind of rule.

We typically use capital letters to represent sets, and lowercase letters to represent elements of a set. The statement $$a \in A$$ means $$a$$ is an element of $$A$$. The statement $$b \not\in A$$ means $$b$$ is not an element of $$A$$.

---

### Set Operations


We take $$A \subseteq B$$ to mean $$A$$ is a **subset** of $$B$$ This means that every element of $$A$$ is also an element of $$B$$. Note that this allows $$A$$ to equal $$B$$. If we wish to exclude this possibility, we write $$A \subset B$$ and say $$A$$ is a **proper subset** of $$B$$.

---

Consider the **universal set** $$U$$ that contains everything, and the **empty set** $$\emptyset$$ which contains nothing. Note that $$\emptyset$$ is an element of $$U$$ as it is an *object*, just with nothing inside.

We say two subsets of $$U$$, $$A$$ and $$Y$$ are **equal** if and only if they are equal elementwise, that is, they contain identically the same elements. In other words, $$X = Y$$ implies $$X \subset Y$$ and $$Y \subset X$$

---

We define $$X \cup Y$$ to mean "$$X$$ **union** $$Y$$" as $$ X \cup Y := \{ \text{set of all elements that belong to $X$ or $Y$ or both} \}$$

---

We define $$X \cap Y$$ to mean "$$X$$ **intersect** $$Y$$" as $$ X \cap Y := \{ \text{set of all elements that belong to both $X$ and $Y$} \}$$

---

These two operations are quite similar to **AND** and **OR** from Boolean Algebra. In fact, we can define a third operation similar to **NOT** called the **complement** of a set $$A$$. The complement has multiple notations that I've seen. The following are equivalent: $$\overline A$$, $$\sim A$$, and $$A^c$$. If $$A \subset U$$, then the set $$\overline A$$ consists of all elements of $$U$$ not contained in $$A$$. This implies the following properties

$$\overline U = \emptyset$$

$$A \cup (\overline A) = U$$

$$A \cap (\overline A) = \emptyset$$

$$\overline{(\overline A)} = ~ \sim (\sim A) = A$$

---

We say $$A$$ and $$B$$ are **disjoint** if $$A \cap B = \emptyset$$.

---

We define the **cartesian product** of $$A$$ and $$B$$ as $$A \times B := \{ (a, b) \mid a \in A \text{ and } b \in B\}$$, or in English, the set of all possible ordered pairs (called **2-tuples**) of elements from $$A$$ and $$B$$.

---

We define the **cardinality** of a set $$A$$ as the number of elements in $$A$$, written as $$\lvert A \rvert$$.

---

These set operations have a number of properties similar to those of addition and multiplication we all learned in grade school.

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

### Functions:

We now turn our attention to functions. Functions are one of the most far-reaching and important ideas in mathematics. The idea is an abstraction of the many familiar situations in which two changing quantities are related to each other by some sort of rule. In this way, we can consider a function as some kind of rule to map one value to another. There are two main (and equivalent) definitions of functions, and we pick whichever is most convenient for us to use.

---

*Definition 1:* If $$A$$ and $$B$$ are sets, then a **function** $$f: A \to B$$ is a *rule* or *mapping* that assigns to each element in $$A$$ exactly one element in $$B$$.

---

*Definition 2:* If $$A$$ and $$B$$ are sets, then a **function** $$f: A \to B$$ is a *set* of ordered pairs in $$A \times B$$ with the property that for each $$a \in A$$ there exists a unique $$b \in B$$ with $$(a, b) \in f$$.

---

If we say $$ f : A \to B $$, we say that $$f$$ is a function from $$A$$ to $$B$$. We call $$A$$ the **domain** and $$B$$ the **codomain** of $$f$$. This symbolism means that for all $$ x \in A$$, there is an $$f(x) \in B$$. For example, $$ f : \mathbb{R} \to \mathbb{R} $$ means that for every real input to $$f$$ there is a real output.

---

A **variable** is typically an alphabetic character (the **name** of the variable) that represents some arbitrary value, called the **value** of the variable which can be known or unknown.

The **scope** of a variable is the set of all values a variable can take on. For example, if we say "let $$x$$ be an arbitrary real number" the scope of $$x$$ is the set of real numbers.

A variable whose scope is a set consisting of exactly one element is called a **constant**.

---

A symbol whose scope is the domain of the function is called an **independent variable**; a symbol whose scope is the codomain (also called the **range**) of a function is called a **dependent variable**.

Note that if the domain and the rule are given, then we can determine the range of a function. Often, we call just the rule a function, but a function is not completely defined unless the domain is either explicitly or implicitly specified.

A function is typically denoted (or named) by a single letter such as $$f, g, F,$$ etc. If the letter $$f$$ represents the name of a definite function, then $$f(x)$$ represents the element in the range of $$f$$ associated with the element $$x$$ in the domain of $$f$$. The statement $$f(x) = x^2$$ is the **definition** of $$f$$, and $$f(a)$$ is called the **value** of $$f$$ at the point $$a$$.

In computer science, we often make a distinction between `=` and `==`. We use `x = 1` to *assign* the value `1` to the variable `x`, and we use `x == 1` to *test* whether the value of `x` is equal to `1`. In pseudocode, we often use the symbol `:=` to explicitly mean assignment or definition. In mathematics we often have similar symbols, though their usage varies. We can often use $$x = a$$ to mean we are testing whether $$x$$ and $$a$$ share the same value, but we also use it to mean we are giving the symbol $$x$$ the value $$a$$. Therefore, it is common in higher mathematics to use the symbol $$:=$$ to explicitly show that we are assigning a value to avoid confusion.

---

If we graph a mapping, we can use the **vertical line test** to determine if the mapping is a *function*. If the vertical line crosses the graph only once, then the mapping is indeed a function. We can use the **horizontal line test** to determine a property of functions called **injectivity**.

---

We say a function $$f: A \to B$$ is **injective** or **one-to-one** if for all $$x_1, x_2 \in A$$, $$f(x_1) = f(x_2)$$ implies $$x_1 = x_2$$.

---

We also say a function $$f: A \to B$$ is **surjective** or **onto** if for every $$b \in B$$ there exists an $$a \in A$$ such that $$f(a) = b$$.

---

If a function is *both* one-to-one and onto, we call it **bijective**.

---

Moving back to set theory for a moment, we say two sets $$A$$ and $$B$$ are **set-theoretically isomorphic** if there exists any bijection $$\phi: A \to B$$, and we write $$A \cong_\text{set} B$$. In other words, we are pairing up elements of $$A$$ and $$B$$. This also means that $$A$$ and $$B$$ have the same cardinality.

We say a set $$A$$ is

* **infinite** if there exists a *proper* subset $$B \subset A$$ that is isomorphic to A. Note that $$B$$ is a proper subset of $$A$$, implying that $$B \neq A$$. This leads to a contradiction if $$A$$ is **finite**. And
  - **countably infinite** if $$A \cong_\text{set} \mathbb{N}$$, that is, if we can *label* every element.
  - $$A$$ is **uncountably infinite** otherwise.
* **finite** otherwise, that is, $$A \cong_\text{set} \{1, 2, \dots, n\}$$ for some $$n \in \mathbb{N}$$, implying that $$\lvert A \rvert ~ = n$$.

---

If $$f: A \to B$$ and $$g: B \to C$$, then the **composite** function $$g \circ f: A \to C$$ is defined by $$(g \circ f)(x) := g(f(x))$$ for all $$x \in A$$.

---

If $$A$$ is *any* set, then the **identity function** $$i:A \to A$$ is given by $$i(x) := x$$ for all $$x \in A$$. Note that the identity function is bijective, meaning that $$f \circ i = f$$ and $$i \circ f = f$$.

---

Let $$f: A \to B$$. Then $$f^{-1}: B \to A$$ is said to be the **inverse** of $$f$$ if, for any $$y \in B$$ $$f^{-1}(y) = x$$ if and only if $$f(x) = y$$. Note that $$(f^{-1} \circ f)(x) = x$$ and $$f \circ f^{-1}(y) = y$$.

---

We say that a function $$f: a \to B$$ is **invertible** if there exists a function $$f^{-1}: B \to A$$ such that $$f^{-1} \circ f$$ is the identity map on $$A$$ and $$f \circ f^{-1}$$ is the identity map on $$B$$. In other words, a function is invertible if and only if it is bijective.

---

If $$f(x)$$ is a real-valued function, then $$f$$ is **even** if the following holds for all $$x$$ in the domain of $$f$$

$$f(x) = f(-x)$$

or

$$f(x) - f(-x) = 0$$

What this means geometrically, is that an even function is symmetric with respect to the $$y$$-axis, that is, we get the same graph if we reflect the graph about the $$y$$-axis.

---

If $$f(x)$$ is a real-valued function, then $$f$$ is **odd** if the following holds for all $$x$$ in the domain of $$f$$

$$-f(x) = f(-x)$$

or

$$f(x) + f(-x) = 0$$

Geometrically, the graph of an odd function has *rotational* symmetry with respect to the origin, meaning that the graph is unchanged if we rotate it 180 degrees about the origin.

---

### Properties of even and odd functions:

* If $$f$$ is both even and odd, then $$f(x) = 0$$ for all $$x$$.
* If $$f$$ is odd, then $$\lvert f \rvert$$ is even.
* Linear combinations of even functions are even.
* Linear combinations of odd functions are odd.
* The sum of an odd function with an even function is neither even nor odd, unless one of the functions is equal to zero over the given domain.
* The product of two even functions is an even function.
* The product of two odd functions is an even function.
* The product of an even function with an odd function is an odd function.
* The composition of two even functions is even.
* The composition of two odd functions is odd.
* The composition of an even function and an odd function is even.
* Every function $$f(x)$$ can be written uniquely as the sum of an even function and an odd function:

  $$f(x) = f_e(x) + f_o(x)$$,

  where

  $$f_e(x) = \frac{1}{2}[f(x) + f(-x)]$$

  is even and

  $$f_o(x) = \frac{1}{2}[f(x)-f(-x)]$$

  is odd.
* Odd functions are not closed under scalar multiplications, but even functions are.
* The derivative of an even function is odd.
* The derivative of an odd function is even.
* The integral of an odd function from $$-a$$ to $$a$$ is zero if there are no vertical asymptotes between $$-a$$ and $$a$$.
* The integral of an even function from $$-a$$ to $$a$$ is twice the integral from $$0$$ to $$a$$ if there are no vertical asymptotes between $$-a$$ and $$a$$.
* The Maclaurin series of an even function includes only even powers.
* The Maclaurin series of an odd function includes only odd powers.
* The Fourier series of an even periodic function includes only cosine terms.
* The Fourier series of an odd periodic function includes only sine terms.

Of these properties, I've found myself needing to use the integration properties the most.

---

Let's return to set theory again. We define the **power set** of a set $$A$$, denoted by $$\wp(A)$$, as the set whose elements are precisely all of the subsets of $$A$$.

---

The **image** of a set $$A$$ under a function $$f: A \to B$$ consists of all those $$y \in B$$ for which there is an $$x \in A$$ such that $$f(x) = y$$. This results in some confusion between the range, codomain, and image of a function. As far as I can tell, they are very nearly the same thing, and conventions differ.

---

Let $$f: A \to B$$ be *any* map. Then the **preimage** of a subset $$V \subset B$$ with respect to $$f$$ is the set $$\text{preim}_f(V) := \{ a \in A \mid f(a) \in V\}$$.

---

Let $$M$$ be a set and $$\sim$$ be a relation such that

* $$\forall m \in M: m \sim m$$ (reflexivity)
* $$\forall m, n \in M: m \sim n \Leftrightarrow n \sim m$$ (symmetry)
* $$\forall m, n, p \in M: m \sim n \text{ and } n \sim p \Rightarrow m \sim p$$ (transitivity)

Then $$\sim$$ is called an **equivalence relation** on $$M$$.

---

Let $$\sim$$ be an equivalence relation on $$M$$. Then for every $$m \in M$$, define the set $$[m] := \{ n \in M \mid m \sim n\}$$ called the **equivalence class** of $$m$$. Equivalence classes have two key properties

* $$a \in [m] \Rightarrow [a] = [m]$$, or in English, any element of an equivalence class can act as a representative.
* Either $$[m] = [n]$$ or $$[m] \cap [n] = \emptyset$$.

---

Let $$\sim$$ be an equivalence relation on $$M$$. We define the **quotient set** $$M \Big/_\sim := \{ [m] \mid m \in M\}$$.

---
